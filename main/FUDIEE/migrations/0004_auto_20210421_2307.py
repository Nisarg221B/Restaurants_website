# Generated by Django 2.2.5 on 2021-04-21 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FUDIEE', '0003_auto_20210421_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_item',
            name='img',
            field=models.ImageField(upload_to='FUDIEE/'),
        ),
    ]
