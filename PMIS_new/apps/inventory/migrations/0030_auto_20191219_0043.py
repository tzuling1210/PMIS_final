# Generated by Django 2.2.5 on 2019-12-18 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0029_auto_20191219_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
