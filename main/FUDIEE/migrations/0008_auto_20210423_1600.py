# Generated by Django 3.2 on 2021-04-23 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FUDIEE', '0007_auto_20210423_1452'),
    ]

    operations = [
        migrations.RenameField(
            model_name='featured_dishes',
            old_name='name',
            new_name='name1',
        ),
        migrations.RemoveField(
            model_name='featured_dishes',
            name='description',
        ),
        migrations.RemoveField(
            model_name='featured_dishes',
            name='img',
        ),
        migrations.RemoveField(
            model_name='featured_dishes',
            name='price',
        ),
        migrations.AddField(
            model_name='featured_dishes',
            name='description1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='featured_dishes',
            name='description2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='featured_dishes',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='FUDIEE/images'),
        ),
        migrations.AddField(
            model_name='featured_dishes',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='FUDIEE/images'),
        ),
        migrations.AddField(
            model_name='featured_dishes',
            name='name2',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='featured_dishes',
            name='price1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='featured_dishes',
            name='price2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='food_item',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='food_item',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='FUDIEE/images'),
        ),
        migrations.AlterField(
            model_name='food_item',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
