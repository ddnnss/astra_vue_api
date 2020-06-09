from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import *
import settings
import json
import json

def get_type(request):
    # request_unicode = request.body.decode('utf-8')
    # request_body = json.loads(request_unicode)
    types=[]

    all_types = TemplateType.objects.all()

    for t in all_types:
        types.append({
            'name':t.name,
            'id':t.name_slug
        })

    return JsonResponse(types, safe=False)


def get_templates(request):
    templates=[]
    all_templates = Template.objects.all()
    for t in all_templates:
        templates.append({
            'id':t.id,
            'title':t.name,
            'category':t.type_slug,
            'price':t.price,
            'image':t.image.url,
            'uuid':t.uuid,
        })
    return JsonResponse(templates, safe=False)

def get_template(request,uuid):
    t = get_object_or_404(Template, uuid=uuid)
    template = {
            'id':t.id,
            'url':t.url,
            'uuid':t.uuid
        }
    return JsonResponse(template, safe=False)


def add_to_cart(request,uuid,token):
    t = get_object_or_404(Template, uuid=uuid)
    cart,created = Cart.objects.get_or_create(token=token)
    new_item = CartItem.objects.create(cart=cart,template=t)
    return JsonResponse({'status':'ok'}, safe=False)


def get_cart(request,token):
    cart = get_object_or_404(Cart,token=token)
    cart_item=[]
    items = CartItem.objects.filter(cart=cart)
    for i in items:
        cart_item.append({
            'item_id':i.id,
            'id':i.template.id,
            'title':i.template.name,
            'category':i.template.type_slug,
            'price':i.template.price,
            'image':i.template.image.url,
            'uuid':i.template.uuid,
        })
    return JsonResponse(cart_item, safe=False)

def del_cart(request,id):
    CartItem.objects.get(id=id).delete()
    return JsonResponse({'result':'ok'}, safe=False)


def new_order(request,token,data):
    cart = get_object_or_404(Cart, token=token)
    info = json.loads(data)
    print(info['domain'])
    if info['domain']:
        print('1')
    else:
        print('0')
    neworder = Order.objects.create(cart=cart,phone=info['phone'],
                         pay=info['payment'],
                         is_need_domain=info['domain'],
                         is_need_hosting=info['hosting'])
    cart.token = '0'
    cart.save()
    msg_html = render_to_string('email/order.html', {
        'cart': CartItem.objects.filter(cart=neworder.cart),
        'phone': neworder.phone,
        'host': neworder.is_need_hosting,
        'domain': neworder.is_need_domain,
        'pay': neworder.pay,

        })

    send_mail(f'Заказ на caйт', None, 'no-reply@specsintez-pro.ru',
              [settings.SEND_TO_1],
              fail_silently=False, html_message=msg_html)
    return JsonResponse({'status': 'ok'}, safe=False)

def new_callback(request,phone):
    Callback.objects.create(phone=phone)
    msg_html = render_to_string('email/callback.html', {
        'phone': phone,
    })
    send_mail(f'Заказ звонка по поводу консультации', None, 'no-reply@specsintez-pro.ru',
              [settings.SEND_TO_1],
              fail_silently=False, html_message=msg_html)
    return JsonResponse({'status': 'ok'}, safe=False)