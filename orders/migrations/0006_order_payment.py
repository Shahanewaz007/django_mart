# Generated by Django 4.2.3 on 2023-09-09 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_paymentgatewaysettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(default='Null', on_delete=django.db.models.deletion.CASCADE, to='orders.payment'),
        ),
    ]
