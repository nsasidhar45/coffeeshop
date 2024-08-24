# Generated by Django 4.2.3 on 2023-07-22 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_remove_order_item_order_items_delete_orderitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('item_name', models.CharField(max_length=100)),
                ('item_image', models.ImageField(upload_to='order_item_images/')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.order')),
            ],
        ),
    ]
