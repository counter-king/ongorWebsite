# Generated by Django 3.1.6 on 2021-02-09 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_menuitem_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='quantity',
        ),
    ]
