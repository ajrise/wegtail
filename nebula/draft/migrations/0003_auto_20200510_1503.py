# Generated by Django 3.0.6 on 2020-05-10 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draft', '0002_draftpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draftpage',
            name='ModDate',
            field=models.DateField(auto_now=True, verbose_name='moddate'),
        ),
    ]
