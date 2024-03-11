from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import HomeItems, HomeItemDetails , HomeCart
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# Create your views here.













def hometools(request):
    templates=loader.get_template('hometools.html')
    furniture= HomeItemDetails.objects.select_related('itemsid')
    print(furniture.query)
    return HttpResponse(templates.render({'furniture':furniture, 'request':request}))

















def Homedetails(request , id):
     template=loader.get_template('Homedetails.html')
     currentuser=request.user
     print(currentuser.id)
     furniture=HomeItemDetails.objects.select_related('itemsid').filter(id=id)
     context={
         'furniture':furniture,
         'request':request
     }
     return HttpResponse(template.render(context))
















@login_required(login_url='/auth_login/')
def HomeCheckout(request, id):
     template=loader.get_template('HomeCheckout.html')
     
     currentuser=request.user
     print(currentuser.id)
     furniture=HomeItemDetails.objects.select_related('itemsid').filter(id=id)
    
     context={
         'furniture':furniture,
         'request':request
     }
     return HttpResponse(template.render(context=context))
















@login_required(login_url='/auth_login/')
def add_to_homecart(requset,id):
     currentuser=requset.user
     discount=2
     state=False
     furniture=HomeItemDetails.objects.select_related('itemsid').filter(id=id)
    
     for item in furniture:
           net=item.total-discount
     cart = HomeCart(
      Id_product=item.id,
      Id_user=currentuser.id,
      price=item.price,
      qty=item.qty,
      tax=item.tax,
      total=item.total,
      discount=discount,
      net=net,
      status=state
)
     

     currentuser=requset.user.id
     count=HomeCart.objects.filter(Id_user=currentuser).count()
     print(count)
     cart.save()
     requset.session['countcart']=count
     return redirect("/hometools")

