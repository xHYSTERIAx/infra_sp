# Generated by Django 2.2.16 on 2022-06-17 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0017_auto_20220617_1053'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='title',
            options={},
        ),
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default='oyujjhcnnl', max_length=10, verbose_name='Код подтверждения'),
        ),
    ]
