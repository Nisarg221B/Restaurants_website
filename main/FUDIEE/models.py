from django.db import models
import mimetypes

# Create your models here.
class food_item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    img = models.ImageField(upload_to ='FUDIEE/',blank=True,null=True)
    price = models.IntegerField(blank=True,null=True)
    type = models.CharField(max_length=20)

class item_types(models.Model):
    type = models.CharField(max_length=20)

class featured_dishes(models.Model):
    name1 = models.CharField(max_length=100)
    description1 = models.TextField(blank=True,null=True)
    img1 = models.ImageField(upload_to ='FUDIEE/',blank=True,null=True)
    price1 = models.IntegerField(blank=True,null=True)
    name2 = models.CharField(max_length=100)
    description2 = models.TextField(blank=True,null=True)
    img2 = models.ImageField(upload_to ='FUDIEE/',blank=True,null=True)
    price2 = models.IntegerField(blank=True,null=True)

