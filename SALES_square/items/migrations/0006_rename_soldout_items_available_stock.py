# Generated by Django 5.2 on 2025-04-17 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_alter_items_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='soldout',
            new_name='Available_Stock',
        ),
    ]
