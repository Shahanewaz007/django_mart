# Generated by Django 4.2.3 on 2023-09-09 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_remove_order_order_status_order_is_ordered_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentGateWaySettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.CharField(blank=True, max_length=500, null=True)),
                ('store_pass', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]