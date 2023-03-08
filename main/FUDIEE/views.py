from  django.shortcuts import render
from .models import *
from django.conf import settings

# Create your views here.

def about(request):
    return render(request,"about.html",{'title':'about Fudiee'})

def index(request):
    items = food_item.objects.all()
    types = item_types.objects.all()
    dish = featured_dishes.objects.all()
    return render(request,"index.html",
                  {
                      'items': items,
                      'types':types,
                      'dishs':dish
                  }
                  )
