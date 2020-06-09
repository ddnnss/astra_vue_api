from django.contrib import admin
from .models import *


class ItemsInline (admin.TabularInline):
    model = CartItem
    extra = 0

class CartAdmin(admin.ModelAdmin):

    inlines = [ItemsInline]
    class Meta:
        model = Cart


admin.site.register(TemplateType)
admin.site.register(Template)
admin.site.register(CartItem)
admin.site.register(Cart,CartAdmin)
admin.site.register(Order)
admin.site.register(Callback)
# Register your models here.
