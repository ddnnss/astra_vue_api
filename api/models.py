from django.db import models
from pytils.translit import slugify

class TemplateType(models.Model):
    name = models.CharField('Тип шаблона', max_length=50,blank=False,null=True)
    name_slug = models.CharField('Тип шаблона', max_length=50,blank=True,null=True)

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(TemplateType, self).save(*args, **kwargs)

class Template(models.Model):
    type = models.ForeignKey(TemplateType,blank=False,null=True,verbose_name='Тип',on_delete=models.CASCADE)
    type_slug = models.CharField('Тип', max_length=50,blank=True,null=True)
    name = models.CharField('Название шаблона', max_length=50, blank=False, null=True)
    price = models.IntegerField('Цена', default=0)
    image = models.ImageField('Картинка',blank=False,null=True,upload_to='images/')
    url = models.CharField('URL',max_length=100,blank=False,null=True)

    def save(self, *args, **kwargs):
        self.type_slug = self.type.name_slug
        super(Template, self).save(*args, **kwargs)

class CartItem(models.Model):
    template = models.ForeignKey(Template,blank=True,null=True,on_delete=models.CASCADE)


class Cart(models.Model):
    item = models.ForeignKey(CartItem, blank=True, null=True,on_delete=models.CASCADE)
    is_need_domain = models.BooleanField(default=False)
    is_need_hosting = models.BooleanField(default=False)

class Order(models.Model):
    cart = models.ForeignKey(Cart,blank=False,null=True,verbose_name='Тип',on_delete=models.CASCADE)
    phone = models.CharField('Телефон', max_length=50, blank=False, null=True)
    email = models.CharField('Email', max_length=50, blank=False, null=True)
    pay = models.CharField('Оплата', max_length=50, blank=False, null=True)
    total_price = models.IntegerField('Цена', default=0)

