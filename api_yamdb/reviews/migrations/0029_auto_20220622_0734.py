# Generated by Django 2.2.16 on 2022-06-22 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0028_auto_20220621_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default='qhiotdkfih', max_length=10, verbose_name='Код подтверждения'),
        ),
    ]
