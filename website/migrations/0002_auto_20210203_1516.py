# Generated by Django 3.1.6 on 2021-02-03 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='address',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='phone',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
