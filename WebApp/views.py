from django.shortcuts import render,redirect
from AdminApp.models import *
from WebApp.models import *

# Create your views here.
def home(request):
    products=ProductDB.objects.order_by('-id')[:8]
    categories=CategoryDB.objects.all()
    return render(request,'home.html',
                  {
                      'categories':categories,
                      'products':products
                  })

def about(request):
    return  render(request,'about.html')

def services(request):
    services=ServicesDB.objects.all()
    return  render(request,'services.html',
                   {
                       'services':services
                   })


def all_products(request):
    categories=CategoryDB.objects.all()
    products=ProductDB.objects.all()
    latest_products=ProductDB.objects.order_by('-id')[:3]
    return  render(request,'all_products.html',
                   {
                       'categories':categories,
                       'products':products,
                       'latest_products':latest_products
                    })

def filtered_products(request,cat_name):
    filtered_product=ProductDB.objects.filter(Category_Name=cat_name)
    return render(request,'filtered_products.html',
                  {'filtered_product':filtered_product})

def single_product(request,p_id):
    products=ProductDB.objects.get(id=p_id)
    return render(request,'single_product.html',
                  {
                      'products':products
                  })

def contact(request):
    return  render(request,'contact.html')

def save_contact(request):
    if request.method=='POST':
        cname=request.POST.get("name")
        cemail=request.POST.get("email")
        message=request.POST.get("msg")
        obj=ContactDB(Name=cname,Email=cemail,Message=message)
        obj.save()
        return redirect(contact)


def sign_in(request):
    return render(request,'sign_in.html')

def sign_up(request):

    return render(request,'sign_up.html')

def save_signup(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        email=request.POST.get("email")
        passwd=request.POST.get("password")
        cpasswd=request.POST.get("confirm_password")
        obj=SignupDB(Username=uname,Email=email,Password=passwd,Confirm_Password=cpasswd)
        if SignupDB.objects.filter(Username=uname,Password=passwd).exists():
            print("Username already exists.....")
            return redirect(sign_up)
        elif SignupDB.objects.filter(Email=email).exists():
            print("Email already Exists....")
            return redirect(sign_up)
        obj.save()
        return redirect(sign_in)

def user_login(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        pswd=request.POST.get("password")
        if SignupDB.objects.filter(Username=uname,Password=pswd).exists():
            request.session['Username']=uname
            request.session['Password']=pswd
            return redirect(home)
        else:
            return redirect(sign_in)
    else:
        return redirect(sign_in)

def user_logout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(home)


def cart(request):
    return render(request,'cart.html')


