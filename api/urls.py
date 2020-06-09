from django.urls import path, include
from . import views

urlpatterns = [
    path("get_types/", views.get_type, name='user_phone'),
    path("get_templates/", views.get_templates, name='get_templates'),
    path("get_template/<uuid>", views.get_template, name='get_template'),
    path("add_to_cart/<uuid>/<token>", views.add_to_cart, name='add_to_cart'),
    path("get_cart/<token>", views.get_cart, name='get_cart'),
    path("del_cart/<id>", views.del_cart, name='del_cart'),
    path("new_order/<token>/<data>", views.new_order, name='new_order'),
    path("new_callback/<phone>", views.new_callback, name='new_callback')

]