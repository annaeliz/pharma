from django.contrib.auth import authenticate,logout,login
from django.core.checks.messages import Error
from django.db.models.expressions import F
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from datetime import date
from django.contrib import messages
import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.db.models import Sum
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

def home(request):
    product=products.objects.all().order_by('-id')[:4] 
    d={'product':product}
    return render(request,'home.html',d)
def about(request):
    return render(request,'about.html',)
def contact(request):
    return render(request,'contact.html',)
def userlogin(request):
    error=" "
    d={}
    if request.method == "POST" : 
        u=request.POST['emailid']
        p=request.POST['pwd']
        user=authenticate(username=u, password= p)
        if user:
            try:
                user1=signup.objects.get(user=user)
                login(request,user)
                error="no"
            except:
                error="yes" 
        else:
            error="yes"     
    d={'error':error}     
    return render(request,'userlogin.html',d)
    
def login_admin(request):
    error=""
    if request.method=="POST":
        u=request.POST['uname']
        p=request.POST['pwd']
        user=authenticate(username=u, password= p)
        try:
            if user.is_staff:
                login(request, user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d={'error':error}
    return render(request,'login_admin.html',d)

def usersignup(request):
    error=" "
    d={}
    if request.method == "POST" :       
        f=request.POST['firstname']
        l=request.POST['lastname']
        c=request.POST['contact']
        e=request.POST['emailid']
        p=request.POST['pwd']
        al1=request.POST['aline2']
        al2=request.POST['aline3']
        user=User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
        signup.objects.create(user=user,contact=c,aline1=al1,aline2=al2)
        try:
                error="no"
        except:
                error="yes"
    d={'error':error}
    return render(request,'usersignup.html',d)

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    tc=signup.objects.all().count()
    tb=orders.objects.all().count()
    tp=products.objects.all().count()
    d={'tc':tc,'tb':tb,'tp':tp}
    return render(request,'admin_home.html',d)


def user_home(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    product=products.objects.all().order_by('-id')[:3]  
    categorys=category.objects.all()
    d={'product':product,'categorys':categorys}
    return render(request,'user_home.html',d)   


def product(request):
    if not request.user.is_authenticated:
        return redirect('userlogin') 
    product=products.objects.all()
    product2=products.objects.filter(category="Medicines").order_by('category')  
    d={'product':product,'product2':product2}
    return render(request,'product.html',d)   


def cat1(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    product2=products.objects.filter(category="Medicines").order_by('category') 
    d={'product2':product2}
    return render(request,'cat1.html',d) 

def cat2(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    product1=products.objects.filter(category="Covid Essentials").order_by('category')  
    d={'product1':product1}
    return render(request,'cat2.html',d) 

def cat3(request):
    if not request.user.is_authenticated:
        return redirect('userlogin') 
    product3=products.objects.filter(category="Nutrition And Supplements").order_by('category')   
    d={'product3':product3}
    return render(request,'cat3.html',d) 


def cat4(request):
    if not request.user.is_authenticated:
        return redirect('userlogin') 
    product4=products.objects.filter(category="Devices").order_by('category')   
    d={'product4':product4}
    return render(request,'cat4.html',d) 

def cat5(request):
    if not request.user.is_authenticated:
        return redirect('userlogin') 
    product5=products.objects.filter(category="Mom & Baby").order_by('category')   
    d={'product5':product5}
    return render(request,'cat5.html',d) 


def cat6(request):
    if not request.user.is_authenticated:
        return redirect('userlogin') 
    product6=products.objects.filter(category="Personal Care").order_by('category')   
    d={'product6':product6}
    return render(request,'cat6.html',d) 

def send_feedback(request):
    if not request.user.is_authenticated:
        return redirect('userlogin') 
    error=""
    d={}
    if request.method == "POST" :       
        n=request.POST['name']
        f=request.POST['feed']
        u=User.objects.get(id=request.user.id)
        feedback.objects.create(user=u,name=n,feedback=f) 
        try:
                error="no"
        except:
                error="yes"
    d={'error':error} 
    return render(request,'send_feedback.html',d)

def view_feedback(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    feedbacks=feedback.objects.all().order_by('-id')
    d={'feedbacks':feedbacks}
    return render(request,'view_feedback.html',d)

def change_passworduser(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    error=""
    d={}
    if request.method== "POST":
        n=request.POST['newpassword']
        con=request.POST['confirmpassword']
        try:
            u=User.objects.get(id=request.user.id)       
            if  n==con:
                u.set_password(n)
                u.save()
                error="no"
            else: 
                error="yes"
        except:
            error="yes"
    d={'error':error}        
    return render(request,'change_passworduser.html',d)


def update_orders(request,pid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    order=orders.objects.get(id=pid)
    error=False
    if request.method=="POST":
            s=request.POST['status']
            order.status=s
            order.save()
            error=True
    d={'order':order,'error':error}
    return render(request,'update_orders.html',d)

def delete_order(request,pid):
    order=orders.objects.get(id=pid)
    order.delete()
    return redirect('view_booking')


def Logout(request):
    logout(request)
    return render(request,'Logout.html')

def view_users(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    data=signup.objects.all()
    d={'data':data}
    return render(request,'view_users.html',d)


def delete_user(request,pid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    client=signup.objects.get(id=pid)
    client.delete()
    return redirect('view_users')

def categories(request):
    if not request.user.is_authenicated:
        return redirect('login_admin')
    return render(request,'admin_home.html',)


def addproduct(request):
    error=" "
    d={}
    if request.method == "POST" :       
        n=request.POST['name']
        i=request.FILES['image']
        c=request.POST['cat']
        p=request.POST['price']
        b=request.POST['brand']
        d=request.POST['des']
        u=User.objects.get(id=request.user.id) 
        products.objects.create(user=u,uploadingdate=date.today(),productname=n,productimage=i,category=c,productprice=p,brand=b,description=d)
        try:
                error="no"
        except:
                error="yes"
    d={'error':error}
    return render(request,'addproduct.html',d)

def add_category(request):
    error=" "
    d={}
    if request.method == "POST" :       
        n=request.POST['name']
        i=request.FILES['image']
        u=User.objects.get(id=request.user.id) 
        category.objects.create(user=u,uploadingdate=date.today(),categoryname=n,categoryimage=i)
        try:
                error="no"
        except:
                error="yes"
    d={'error':error}
    return render(request,'add_category.html',d)


def view_product(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    data=products.objects.all()
    d={'data':data}
    return render(request,'view_product.html',d)

def delete_product(request,pid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    client=products.objects.get(id=pid)
    client.delete()
    return redirect('view_product')


def view_category(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    data=category.objects.all()
    d={'data':data}
    return render(request,'view_category.html',d)

def delete_category(request,pid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    client=category.objects.get(id=pid)
    client.delete()
    return redirect('view_category')


def edit_product(request,pid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
   
    data=products.objects.get(id=pid)
    error=False
    if request.method=="POST":
        n=request.POST['name']
        i=request.FILES['image']
        c=request.POST['cat']
        p=request.POST['price']
        b=request.POST['brand']
        d=request.POST['des']
        data.productname=n
        data.productimage=i
        data.category=c
        data.productprice=p
        data.brand==b
        data.description=d
        data.save()
        error=True
    d={'data':data,'error':error}
    return render(request,'edit_product.html',d)

def view_booking(request):
    order=orders.objects.all()
    ordered_products=[]
    ordered_bys=[]
    for o in order:
        ordered_product=products.objects.all().filter(id=o.product.id)
        ordered_by=signup.objects.all().filter(id = o.customer.id)
        ordered_products.append(ordered_product)
        ordered_bys.append(ordered_by)
    return render(request,'view_booking.html',{'data':zip(ordered_products,ordered_bys,order)})

def my_orders(request):
    if not request.user.is_authenticated:
        return redirect('userlogin') 
    customer=signup.objects.get(user_id=request.user.id)
    order=orders.objects.all().filter(customer_id = customer)
    ordered_products=[]
    for o in order:
        ordered_product=products.objects.all().filter(id=o.product.id)
        ordered_products.append(ordered_product)

    return render(request,'my_orders.html',{'data':zip(ordered_products,order)})

def add_to_cart(request,pk):
    if not request.user.is_authenticated:
        return redirect('userlogin') 
    product=products.objects.all()
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=1
    response = render(request, 'product.html',{'product':product,'product_count_in_cart':product_count_in_cart})
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids=="":
            product_ids=str(pk)
        else:
            product_ids=product_ids+"|"+str(pk)
        response.set_cookie('product_ids', product_ids)
    else:
        response.set_cookie('product_ids', pk)

    prod=products.objects.get(id=pk)
    messages.info(request, prod.productname + ' added to cart successfully!')
    return response

def my_cart(request):
    if not request.user.is_authenticated:
        return redirect('userlogin') 
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0
    product=None
    total=0
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids != "":
            product_id_in_cart=product_ids.split('|')
            product=products.objects.all().filter(id__in = product_id_in_cart)
            for p in product:
                total=total+p.productprice
    return render(request,'my_cart.html',{'product':product,'total':total,'product_count_in_cart':product_count_in_cart})


def search_view(request):
    query = request.GET['query']
    print(query)
    product=products.objects.all().filter(productname__icontains=query)
    word="Searched Result :"
    print(word)
    return render(request,'product.html',{'product':product,'word':word})

def remove_from_cart(request,pk):
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0
    total=0
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        product_id_in_cart=product_ids.split('|')
        product_id_in_cart=list(set(product_id_in_cart))
        product_id_in_cart.remove(str(pk))
        product=products.objects.all().filter(id__in = product_id_in_cart)
        for p in product:
            total=total+p.productprice
        value=""
        for i in range(len(product_id_in_cart)):
            if i==0:
                value=value+product_id_in_cart[0]
            else:
                value=value+"|"+product_id_in_cart[i]
        response = render(request, 'my_cart.html',{'product':product,'total':total,'product_count_in_cart':product_count_in_cart})
        if value=="":
            response.delete_cookie('product_ids')
        response.set_cookie('product_ids',value)
        return response

def customer_address(request):
    product_in_cart=False
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids != "":
            product_in_cart=True
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    if request.method == 'POST':
            e=request.POST['email']
            m=request.POST['mobile']
            a=request.POST['add']
            total=0
            if 'product_ids' in request.COOKIES:
                product_ids = request.COOKIES['product_ids']
                if product_ids != "":
                    product_id_in_cart=product_ids.split('|')
                    product=products.objects.all().filter(id__in = product_id_in_cart)
                    for p in product:
                        total=total+p.productprice
            response = render(request, 'payment.html',{'total':total})
            response.set_cookie('email',e)
            response.set_cookie('mobile',m)
            response.set_cookie('address',a)
            return response
    return render(request,'customer_address.html',{'product_in_cart':product_in_cart,'product_count_in_cart':product_count_in_cart})

def payment_success(request):
    u=User.objects.get(id=request.user.id)
    customer=signup.objects.get(user_id=request.user.id)
    product=None
    email=None
    mobile=None
    address=None
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids != "":
            product_id_in_cart=product_ids.split('|')
            product=products.objects.all().filter(id__in = product_id_in_cart)
    if 'email' in request.COOKIES:
        email=request.COOKIES['email']
    if 'mobile' in request.COOKIES:
        mobile=request.COOKIES['mobile']
    if 'address' in request.COOKIES:
        address=request.COOKIES['address']
    for p in product:
        orders.objects.get_or_create(user=u,customer=customer,product=p,status='Pending',email=email,mobile=mobile,address=address)
    response = render(request,'payment_success.html')
    response.delete_cookie('product_ids')
    response.delete_cookie('email')
    response.delete_cookie('mobile')
    response.delete_cookie('address')
    return response

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return

def download(request,orderID,productID):
    if not request.user.is_authenticated:
        return redirect('user_home')
    order=orders.objects.get(id=orderID)
    product=products.objects.get(id=productID)
    mydict={
        'orderDate':order.order_date,
        'customerName':request.user,
        'customerEmail':order.email,
        'customerMobile':order.mobile,
        'shipmentAddress':order.address,
        'orderStatus':order.status,

        'productName':product.productname,
        'productImage':product.productimage,
        'productPrice':product.productprice,
        'productDescription':product.description,


    }
    return render_to_pdf('download.html',mydict)
def profile(request):
    if not request.user.is_authenticated:
        return redirect('userlogin') 
    customer=signup.objects.get(user_id=request.user.id)
    return render(request,'profile.html',{'customer':customer})

def edit_profile(request):
    customer=signup.objects.get(user_id=request.user.id)
    user=User.objects.get(id=customer.user_id)
    error=False
    if request.method=="POST":
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        al1=request.POST['aline1']
        al2=request.POST['aline2']
        m=request.POST['mobile']
        user.first_name=f
        user.last_name=l
        user.username=e
        customer.aline1=al1
        customer.aline2=al2
        customer.contact=m
        user.save()
        customer.save()
        error=True
    d={'user':user,'customer':customer,'error':error}
    return render(request,'edit_profile.html',d)


