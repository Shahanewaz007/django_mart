# Generated by Django 4.2.3 on 2023-09-09 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_order_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_status',
        ),
        migrations.AddField(
            model_name='order',
            name='is_ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='New', max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='ip',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_note',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(max_length=30),
        ),
    ]
