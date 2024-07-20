from django.shortcuts import get_object_or_404, render,redirect
from labware_app.models import Contact,Product
from django.contrib import messages
from math import ceil
from django.conf import settings
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.

def product_list(request):
    # products = Product.objects.all()
    allProds=[]
    catprods=Product.objects.values('category','product_id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n//4 + ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nSlides),nSlides])
    
    params={'allProds':allProds}    
    
    return render(request,"newindex.html",params)
    # return render(request, 'newindex.html', {'products': products})

def product_details(request, product_id):
    products = Product.objects.all()
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'productdetail.html', {'product': product})

def products(request):
    # objects=Product.objects.all()
    allProds=[]
    catprods=Product.objects.values('category','product_id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n//4 + ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nSlides),nSlides])
    
    params={'allProds':allProds}    
    
    return render(request,"index1.html",params)

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        ph_num=request.POST.get('pnumber')
        query=request.POST.get('query')
        myquery=Contact(name=name,email=email,ph_num=ph_num,query=query)
        myquery.save()
        
        email_subject=f"New Query from the user -{name} "
        message=f"Query from {name} \n - {query} \n \n Contact details:\n Name-{name} \n  email- {email} \n Phno - {ph_num}"
                     
        email_message=EmailMessage(subject=email_subject,body=message,from_email=settings.EMAIL_HOST_USER,to=["*******@gmail.com"],bcc=[""],reply_to=[email])
        email_message.send() 
        # messages.info(request,"We will get back to you soon ")
        
        return render(request,"contact.html")

    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def home(request):
    return render(request,'home.html')    

def infrastructure(request):
    return render(request,"infrastructure.html")

