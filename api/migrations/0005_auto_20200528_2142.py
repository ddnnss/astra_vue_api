# Generated by Django 3.0.3 on 2020-05-28 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_cart_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='item',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Cart'),
        ),
    ]