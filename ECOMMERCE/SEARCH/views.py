from django.shortcuts import render
from SHOP.models import Product
from django.db.models import Q
from django.shortcuts import HttpResponse

# Create your views here.
def searchresult(request):
    products=None
    query=None
    if request.method=="POST":
        query=request.POST.get('q')
        if query:
            products=Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request,'Search.html',{'query':query,'products':products})