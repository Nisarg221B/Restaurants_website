# Generated by Django 3.2 on 2021-04-23 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FUDIEE', '0005_alter_food_item_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='item_types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
            ],
        ),
    ]
