# Generated by Django 4.2.3 on 2023-07-22 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_order_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='item',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='restaurant.item'),
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
