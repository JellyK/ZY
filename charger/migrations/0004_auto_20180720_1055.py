# Generated by Django 2.0.7 on 2018-07-20 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charger', '0003_auto_20180720_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teslacharger',
            name='charge_info',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='teslacharger',
            name='charger_info',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='teslacharger',
            name='opening_time_info',
            field=models.CharField(max_length=128),
        ),
    ]