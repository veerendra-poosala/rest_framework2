# Generated by Django 2.2 on 2021-08-24 17:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_mixins', '0002_auto_20210824_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermixinmodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 24, 23, 5, 25, 270086)),
        ),
    ]
