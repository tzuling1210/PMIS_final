# Generated by Django 2.0 on 2019-01-03 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0006_auto_20190103_1648'),
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
        migrations.DeleteModel(
            name='Transaction',
        ),
        migrations.DeleteModel(
            name='Transaction_product',
        ),
    ]