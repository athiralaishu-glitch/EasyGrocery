

from django.shortcuts import render,redirect
from AdminApp.models import *
from WebApp.models import *
from django.contrib import messages

# Create your views here.
def home(request):
    products=ProductDB.objects.order_by('-id')[:8]
    categories=CategoryDB.objects.all()
    cart_count=0
    uname=request.session.get('Username')
    if uname:
        cart_count = CartDB.objects.filter(Username=uname).count()

    # items=data.count()
    return render(request,'home.html',
                  {
                      'categories':categories,
                      'products':products,
                      'cart_count':cart_count
                      # 'items':items
                  })

def about(request):
    products = ProductDB.objects.order_by('-id')[:8]
    categories = CategoryDB.objects.all()
    cart_count = 0
    uname = request.session.get('Username')
    if uname:
        cart_count = CartDB.objects.filter(Username=uname).count()
    return  render(request,'about.html',
                   {
                       'categories': categories,
                       'products': products,
                       'cart_count': cart_count
                       # 'items':items
                   })


def services(request):
    products = ProductDB.objects.order_by('-id')[:8]
    categories = CategoryDB.objects.all()
    services=ServicesDB.objects.all()
    cart_count = 0
    uname = request.session.get('Username')
    if uname:
        cart_count = CartDB.objects.filter(Username=uname).count()
    return  render(request,'services.html',
                   {
                       'services':services,
                       'categories': categories,
                       'products': products,
                       'cart_count': cart_count
                   })


def all_products(request):
    categories=CategoryDB.objects.all()
    products=ProductDB.objects.all()

    cart_count = 0
    uname = request.session.get('Username')
    if uname:
        cart_count = CartDB.objects.filter(Username=uname).count()
    latest_products=ProductDB.objects.order_by('-id')[:3]
    return  render(request,'all_products.html',
                   {
                       'categories':categories,
                       'products':products,
                       'latest_products':latest_products,
                       'cart_count':cart_count
                    })

def filtered_products(request,cat_name):
    categories = CategoryDB.objects.all()
    cart_count = 0
    uname = request.session.get('Username')
    if uname:
        cart_count = CartDB.objects.filter(Username=uname).count()
    filtered_product=ProductDB.objects.filter(Category_Name=cat_name)
    return render(request,'filtered_products.html',
                  {'filtered_product':filtered_product,
                   'categories': categories,
                   'cart_count': cart_count
                   })

def single_product(request,p_id):
    products=ProductDB.objects.get(id=p_id)
    return render(request,'single_product.html',
                  {
                      'products':products
                  })

def contact(request):
    products = ProductDB.objects.order_by('-id')[:8]
    categories = CategoryDB.objects.all()
    cart_count = 0
    uname = request.session.get('Username')
    if uname:
        cart_count = CartDB.objects.filter(Username=uname).count()
    return  render(request,'contact.html',
                   {
                       'categories': categories,
                       'products': products,
                       'cart_count': cart_count
                   })

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
        messages.success(request,"Registered Successfully...")
        return redirect(sign_in)

def user_login(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        pswd=request.POST.get("password")
        if SignupDB.objects.filter(Username=uname,Password=pswd).exists():
            request.session['Username']=uname
            request.session['Password']=pswd
            messages.success(request, "Logged in Successfully...")
            return redirect(home)
        else:
            messages.error(request, "Invalid username or password...")

            return redirect(sign_in)
    else:
        return redirect(sign_in)

def user_logout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(home)
#------------------------------------------------------------------------------------------------------------------------------------------

def cart(request):
    categories = CategoryDB.objects.all()
    cart_count = 0
    uname = request.session.get('Username')
    if uname:
        cart_count = CartDB.objects.filter(Username=uname).count()
    data=CartDB.objects.filter(Username=request.session['Username'])
    sub_total=0
    delivery=0
    grand_total=0
    for i in data:
        sub_total += i.TotalPrice
        if sub_total > 1000:
            delivery=0
        elif sub_total > 500:
            delivery=50
        else:
            delivery=100
        grand_total=sub_total+delivery
    return render(request,'cart.html',
                  {'data':data,
                            'sub_total':sub_total,
                            'delivery':delivery,
                            'grand_total':grand_total,
                            'categories': categories,
                            'cart_count': cart_count
                   })

def save_cart(request):
    if request.method=='POST':
        uname=request.POST.get("uname")
        pname=request.POST.get("pname")
        quantity=request.POST.get("quantity")
        price=request.POST.get("price")
        total=request.POST.get("total")
        pro=ProductDB.objects.filter(ProductName=pname).first()
        pimg=pro.ProductImage if pro else None
        obj=CartDB(Username=uname,ProductName=pname,Quantity=quantity,Price=price,TotalPrice=total, ProductImage=pimg)
        obj.save()
    return redirect(cart)

def delete_cart_items(request,c_id):
    items=CartDB.objects.filter(id=c_id)
    items.delete()
    return redirect(cart)


#---------------------------------------------------------------------------------------------------------------------------------------

def checkout(request):
    return render(request,'checkout.html')

def payment(request):
    return render(request,'payment.html')


