# Generated by Django 3.2 on 2021-07-27 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='current_price',
            field=models.FloatField(blank=True, default=0),
        ),
    ]