# Generated by Django 2.0.7 on 2018-07-16 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charge', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='echarge',
            name='address',
            field=models.CharField(max_length=128),
        ),
    ]