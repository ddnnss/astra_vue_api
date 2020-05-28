from django.urls import path, include
from . import views

urlpatterns = [
    path("get_types/", views.get_type, name='user_phone'),
    path("get_templates/", views.get_templates, name='get_templates')
]