# Generated by Django 2.2.7 on 2020-05-28 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='type_slug',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Тип'),
        ),
        migrations.AddField(
            model_name='templatetype',
            name='name_slug',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Тип шаблона'),
        ),
    ]