from django.shortcuts import render,redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.core.files.storage import FileSystemStorage
from AdminApp.models import *
from WebApp.models import *
from  django.contrib import messages


# Create your views here.
def dashboard(request):
    categories=CategoryDB.objects.count()
    products=ProductDB.objects.count()
    return render(request,'dashboard.html',
                  {
                      'categories':categories,
                      'products':products
                  })

def add_category(request):
    return render(request,'add_category.html')

def save_category(request):
    if request.method=="POST":
        name=request.POST.get("cname")
        description=request.POST.get("desc")
        image=request.FILES["cimg"]
        obj=CategoryDB(CategoryName=name,Description=description,CategoryImage=image)
        obj.save()
        messages.success(request,"Category Successfully added...")
        return  redirect(add_category)

def edit_category(request,c_id):
    category=CategoryDB.objects.get(id=c_id)
    return  render(request,'edit_category.html',
                   {'cat':category})

def update_category(request,c_id):
    if request.method=='POST':
        name = request.POST.get("cname")
        description = request.POST.get("desc")
        try:
            img = request.FILES["cimg"]
            fs=FileSystemStorage()
            x=fs.save(img.name,img)
        except MultiValueDictKeyError:
            x=CategoryDB.objects.get(id=c_id).CategoryImage
        CategoryDB.objects.filter(id=c_id).update(CategoryName=name,Description=description,CategoryImage=x)
        messages.success(request,'Category updates successfully...')
        return redirect(view_category)

def delete_category(request,c_id):
    category=CategoryDB.objects.filter(id=c_id)
    category.delete()
    messages.error(request,"Product deleted Successfully")
    return redirect(view_category )


def view_category(request):
    cat=CategoryDB.objects.all()
    return render(request,'view_category.html',
                  {'category':cat})

#---------------------------------------------------------------------------------------------------------------------------------------


def add_products(request):
    cat=CategoryDB.objects.all()
    return render(request,'add_products.html',
                  {'cat':cat})

def save_products(request):
    if request.method=='POST':
        name=request.POST.get("pname")
        desc=request.POST.get("desc")
        price=request.POST.get("price")
        cate=request.POST.get("category")
        img=request.FILES["pimg"]
        products=ProductDB(ProductName=name,Description=desc,Price=price,Category_Name=cate,ProductImage=img)
        products.save()
        messages.success(request,"Product saved Successfully..")
        return redirect(add_products)

def view_products(request):
    prod=ProductDB.objects.all()
    return render(request,'view_products.html',
                  {"prod":prod})

def edit_products(request,p_id):
    prod=ProductDB.objects.get(id=p_id)
    return render(request,'edit_products.html',
                  {"prod":prod})

def update_products(request,p_id):
    if request.method=='POST':
        name=request.POST.get("pname")
        desc=request.POST.get("desc")
        price=request.POST.get("price")
        cate=request.POST.get("category")
        try:
            img = request.FILES["pimg"]
            fs=FileSystemStorage()
            x=fs.save(img.name,img)
        except MultiValueDictKeyError:
            x=ProductDB.objects.get(id=p_id).ProductImage
        ProductDB.objects.filter(id=p_id).update(ProductName=name,Description=desc,Price=price,Category_Name=cate,ProductImage=x)
        messages.success(request,'Product updates successfully...')
        return redirect(view_products)

def delete_products(request,p_id):
    prod=ProductDB.objects.filter(id=p_id)
    prod.delete()
    messages.error(request,"Product deleted Successfully")
    return redirect(view_products)
#----------------------------------------------------------------------------------------------------------------------------------------


def add_services(request):
    return render(request,'add_services.html')

def save_services(request):
    if request.method=="POST":
        sname=request.POST.get("name")
        des=request.POST.get("desc")
        simg=request.FILES['img']
        obj=ServicesDB(Name=sname,Description=des,Image=simg)
        obj.save()
        return redirect(add_services)

def delete_services(request,s_id):
    ser=ServicesDB.objects.filter(id=s_id)
    ser.delete()
    return redirect(view_services)


def view_services(request):
    services=ServicesDB.objects.all()
    return render(request,'view_services.html',
                  {
                      'services':services
                  })




def admin_login_page(request):
    return render(request,'admin_login.html')

def admin_login(request):
    if request.method=='POST':
        uname=request.POST.get("username")
        pswd=request.POST.get("password")

        if User.objects.filter(username__contains=uname).exists():
            user=authenticate(username=uname,password=pswd)
            if user is not None:
                login(request,user)
                request.session['username']=uname
                request.session['password']=pswd
                return redirect(dashboard)
            else:
                return redirect(admin_login_page)
        else:
            return redirect(admin_login_page)


def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login_page)

def contact_data(request):
    data=ContactDB.objects.all()
    return render(request,'contact_data.html',
                  {
                      'data':data
                  })




