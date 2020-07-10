# Generated by Django 3.0.8 on 2020-07-10 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_carosel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partnerimg', models.ImageField(blank=True, upload_to='partner_image')),
                ('partnername', models.CharField(max_length=500)),
                ('partnerdes', models.CharField(max_length=500)),
            ],
        ),
    ]
