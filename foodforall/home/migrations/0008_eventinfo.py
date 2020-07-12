# Generated by Django 3.0.8 on 2020-07-12 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_contactinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventname', models.CharField(max_length=500)),
                ('eventimg', models.ImageField(blank=True, upload_to='Event_image')),
                ('eventdes', models.CharField(max_length=500)),
                ('eventlocation', models.CharField(max_length=500)),
                ('eventcontact', models.IntegerField(default=0)),
                ('date', models.DateField()),
            ],
        ),
    ]
