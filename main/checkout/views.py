from django.shortcuts import render,redirect
from .models import *
from django.conf import settings
from FUDIEE.models import *
# Create your views here.

def checkout(request):
    orders = {}
    o_total = 0
    if request.method == 'POST':
       items = food_item.objects.all()
       for i in items:
           x = request.POST[i.name]
           x = int(x)
           if x<=0 or x==None:
               continue
           price = x * i.price
           o_total += price
           orders[i.name] = price
       print(orders)
       print(o_total)
       return render(request,"checkout.html",{'o_total':o_total,'orders':orders})
       #return redirect("checkout")
    else:
       print(orders)
       return render(request,"checkout.html",orders)
    
