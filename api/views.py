from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import *

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
            'id':i.template.id,
            'title':i.template.name,
            'category':i.template.type_slug,
            'price':i.template.price,
            'image':i.template.image.url,
            'uuid':i.template.uuid,
        })
    return JsonResponse(cart_item, safe=False)
