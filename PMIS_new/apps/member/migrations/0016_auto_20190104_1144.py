# Generated by Django 2.0 on 2019-01-04 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0015_auto_20190104_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='member',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='products',
        ),
        migrations.RemoveField(
            model_name='transaction_product',
            name='product',
        ),
        migrations.RemoveField(
            model_name='transaction_product',
            name='transaction',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
        migrations.DeleteModel(
            name='Transaction_product',
        ),
    ]
