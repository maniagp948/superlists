# Generated by Django 5.1.3 on 2024-11-22 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_alter_item_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('id',)},
        ),
    ]
