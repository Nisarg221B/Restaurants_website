# Generated by Django 3.2 on 2021-04-23 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FUDIEE', '0008_auto_20210423_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featured_dishes',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='FUDIEE/'),
        ),
        migrations.AlterField(
            model_name='featured_dishes',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='FUDIEE/'),
        ),
        migrations.AlterField(
            model_name='food_item',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='FUDIEE/'),
        ),
    ]
