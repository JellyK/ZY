# Generated by Django 2.0.7 on 2018-07-21 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charger', '0006_auto_20180720_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teslacharger',
            name='location_type',
            field=models.CharField(max_length=128),
        ),
    ]
