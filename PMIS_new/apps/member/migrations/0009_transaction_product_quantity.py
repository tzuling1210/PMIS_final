# Generated by Django 2.0 on 2019-01-03 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0008_auto_20190103_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction_product',
            name='quantity',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
