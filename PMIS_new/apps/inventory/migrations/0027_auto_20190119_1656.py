# Generated by Django 2.0 on 2019-01-19 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0026_auto_20190119_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='component',
            name='level',
        ),
        migrations.RemoveField(
            model_name='material',
            name='level',
        ),
        migrations.RemoveField(
            model_name='product',
            name='level',
        ),
    ]
