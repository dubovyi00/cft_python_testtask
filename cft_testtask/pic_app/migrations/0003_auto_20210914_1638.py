# Generated by Django 3.2.7 on 2021-09-14 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pic_app', '0002_remove_pictures_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='color',
            field=models.CharField(max_length=6, verbose_name='Код цвета #'),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='mode',
            field=models.CharField(choices=[('WB', 'Черные vs Белые'), ('HEX', 'Цвет по HEX-коду')], default='WB', max_length=30, verbose_name='Режим'),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='src',
            field=models.ImageField(upload_to='images/', verbose_name='Выберите картинку'),
        ),
    ]
