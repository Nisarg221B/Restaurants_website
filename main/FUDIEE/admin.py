from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(food_item)
admin.site.register(item_types)
admin.site.register(featured_dishes)