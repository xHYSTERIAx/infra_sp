# Generated by Django 2.2.16 on 2022-06-22 04:49

from django.db import migrations, models
import reviews.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0029_auto_20220622_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.PositiveSmallIntegerField(validators=[reviews.validators.correct_year], verbose_name='Год выпуска'),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length=3500, verbose_name='Информация о себе'),
        ),
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default='hpnramnhhu', max_length=10, verbose_name='Код подтверждения'),
        ),
    ]
