# Generated by Django 3.2.7 on 2021-09-14 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pic_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pictures',
            name='name',
        ),
    ]
