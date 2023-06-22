from django.shortcuts import render
from  SHOP.models import Category,Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def allProdCat(request):
    c=Category.objects.all()
    return render(request,'Category.html',{'c':c})

def allproducts(request,cslug):
    c=Category.objects.get(slug=cslug)
    p=Product.objects.filter(category__slug=cslug)
    return render(request,'Product.html',{'p':p,'c':c})


def prodetail(request,pslug):
    p=Product.objects.get(slug=pslug)
    return render(request,'Detail.html',{'p':p})

def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        f=request.POST['f']
        l=request.POST['l']
        e=request.POST['e']
        p=request.POST['p']
        cp=request.POST['cp']
        if p==cp:
            user=User.objects.create_user(username=u,first_name=f,last_name=l,email=e,password=p)
            user.save()
            return allProdCat(request)

    return render(request,'Register.html')

def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return allProdCat(request)
        else:
            messages.error(request,"INVALID CREDENTIALS")

    return render(request,'Login.html')

def user_logout(request):
    logout(request)
    return allProdCat(request)

