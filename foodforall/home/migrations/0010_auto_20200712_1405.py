# Generated by Django 3.0.8 on 2020-07-12 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20200712_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fooddes',
            field=models.TextField(max_length=500),
        ),
    ]
