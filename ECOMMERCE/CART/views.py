from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from SHOP.models import Product
from CART.models import Cart,Account,Order
from django.shortcuts import HttpResponse
# Create your views here.

@login_required
def cart_view(request):
    total=0
    try:
        user=request.user
        CART=Cart.objects.filter(user=user)
        for i in CART:
            total+=i.quantity*i.products.price
    except Cart.DoesNotExist:
        pass
    return render(request,'Cart.html',{'CART':CART,'total':total})

@login_required
def add_cart(request,p):
    product=Product.objects.get(id=p)
    user=request.user
    try:
        CART=Cart.objects.get(products=product,user=user)
        if CART.quantity < CART.products.stock:
            CART.quantity+=1
        CART.save()
    except Cart.DoesNotExist:
        CART=Cart.objects.create(products=product,user=user,quantity=1)
        CART.save()
    return redirect('CART:cart_view')

@login_required
def cart_remove(request,p):
    user=request.user
    product=Product.objects.get(id=p)
    try:
        CART=Cart.objects.get(user=user,products=product)
        if CART.quantity > 1:
            CART.quantity -= 1
            CART.save()
        else:
              CART.delete()
    except:
        pass
    return redirect('CART:cart_view')

@login_required

def full_remove(request,p):
    user=request.user
    product=Product.objects.get(id=p)
    try:
        CART=Cart.objects.get(user=user,products=product)
        CART.delete()
    except:
        pass

    return redirect('CART:cart_view')


@login_required

def order(request):
    total=0
    items=0
    msg=0
    if(request.method=="POST"):
        a=request.POST['a']
        p=request.POST['p']
        num=request.POST['num']
        user=request.user
        CART=Cart.objects.filter(user=user)
        for i in CART:
            total+=i.quantity*i.products.price
            items+=i.quantity

        ac=Account.objects.get(acctnumber=num)
        if float(ac.amount) >= total:
            ac.amount=ac.amount-total
            ac.save()
            for i in CART:
                o=Order.objects.create(user=user,products=i.products,address=a,phone=p,order_status="Paid",noofitems=i.quantity)
                o.save()
            CART.delete()
            msg="Ordered Placed Successfully"
            return render(request,'OrderDetails.html',{'msg':msg,'total':total,'items':items})
        else:
            msg="INSUFFICIENT AMOUNT.YOU CANT PLACE ORDER"
            return render(request,'OrderDetails.html',{'msg':msg})

    return render(request,'Form.html')

@login_required

def orderview(request):
    user=request.user
    o=Order.objects.filter(user=user,order_status="Paid")
    return render(request,'Orderview.html',{'o':o,'name':user.username})