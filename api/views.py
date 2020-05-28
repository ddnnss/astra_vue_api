from django.http import JsonResponse
from .models import TemplateType
from .models import Template
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
            'url':t.url,

        })
    return JsonResponse(templates, safe=False)