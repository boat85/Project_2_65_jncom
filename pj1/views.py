# from slugify import slugify

from os import umask
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages as m
from .models import users
from .models import Products
from .forms import AddProducts,FRegiter



# Create your views here.

def admin_u(request):
  id1 = request.session['id']
  u=users.objects.raw('SELECT * FROM `pj1_users` WHERE id={}'.format(id1))
  return render(request,'admin_u.html',{'u':u })



def index(request):
  products = Products.objects.all()
  
  id1 = request.session['id']
  u=users.objects.raw('SELECT * FROM `pj1_users` WHERE id={}'.format(id1))

  return render(request,'index.html',{
    'pd':products,
    'u':u,
    'id':id1
  })
  


def login(request):
  username = request.POST['username']
  password = request.POST['pass']
  
  user=users.objects.all()
  
  for i in user:
    if i.username==username and i.password==password:
      id = i.id
    
      # [id,username,fname,status]
      # request.session['user']={'id':id,'user':username1,'fn':fname,'s':status}
      
      request.session['id'] = id
      # request.session['user'] = username1
      # request.session['fn'] = fname
      # request.session['s'] = status
      # # request.session['images'] = img
      
      id1 = request.session['id']
      u=users.objects.raw('SELECT * FROM `pj1_users` WHERE id={}'.format(id1))
      # u=users.objects.get(id=id)
      products = Products.objects.all()
      
      return render(request,'index.html',{
      'u':u,
      'pd':products
      })
    
    
  m.info(request,'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง')
  return redirect('/loginto')




def loginto(request):
  id1 = request.session['id']
  u=users.objects.raw('SELECT * FROM `pj1_users` WHERE id={}'.format(id1))
  
  return render(request,'login.html',{'u':u,'id':id1})




def logout(request):
  request.session['id'] = -1
  # return render(request,'index.html',{'id':request.session['id']})
  return redirect('/loginto')

def register(request):
  id1 = request.session['id']
  u=users.objects.raw('SELECT * FROM `pj1_users` WHERE id={}'.format(id1))
  
  return render(request,'register.html',{
    'u':u,
    'id':id1
    })
  
  

def showuser(request):
  # user=users.objects.all()
  id1 = request.session['id']
  u=users.objects.raw('SELECT * FROM `pj1_users` WHERE id={}'.format(id1))
  # u=users.objects.get(id=id1)
  
  return render(request,'showuser.html',{
    'u':u,
    })
    
    



  
def showallusers(request):
    us = users.objects.all()
    
    id1 = request.session['id']
    u=users.objects.raw('SELECT * FROM `pj1_users` WHERE id={}'.format(id1))
    
    return render(request,'showallusers.html',{
    'u1':us,
    'u':u,
    'id':id1
  })


def adduser(request):
  form = FRegiter
  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    if users.objects.filter(username=username).exists():
      m.info(request,'ชื่อผู้ใช้มีคนใช้แล้ว')
      return redirect('/register')
    elif users.objects.filter(email=email).exists():
      m.info(request,'อีเมล์นี้มีคนใช้แล้ว')
      return redirect('/register')
    
    form = FRegiter(request.POST,request.FILES)
    if form.is_valid():
      form.save()
      return redirect('/loginto')
    return redirect('/register')
  return redirect('/register')
  
  # username = request.POST['username']
  # fname = request.POST['fname']
  # lname = request.POST['lname']
  # tell = request.POST['tell']
  # nname = request.POST['nname']
  # email = request.POST['email']
  # address = request.POST['address']
  # password = request.POST['password']
  # repassword = request.POST['repassword']
  
  # if password==repassword:
  #   if users.objects.filter(username=username).exists():
  #     m.info(request,'ชื่อผู้ใช้มีคนใช้แล้ว')
  #     return redirect('/register')
  #   elif users.objects.filter(email=email).exists():
  #     m.info(request,'อีเมล์นี้มีคนใช้แล้ว')
  #     return redirect('/register')
  #   elif users.objects.filter(tell=tell).exists():
  #     m.info(request,'เบอร์นี้มีผู้ใช้แล้ว')
  #     return redirect('/register')
  #   else:
  #     users.objects.create(
  #     username=username,
  #     fname=fname,
  #     lname=lname,
  #     tell=tell,
  #     nname=nname,
  #     email=email,
  #     address=address,
  #     password=password,
  #     # images='',
  #     # status_u = '2'
  #     )
      
  #     return redirect('/')
    
  # else:
  #   m.info(request,'รหัสผ่านไม่ต้องกัน')
  #   return redirect('/register')
  
  



  
def showproduct(request):
  id = request.POST['id']
  pd = Products.objects.raw('SELECT * FROM `pj1_products` WHERE id = {}'.format(id))
  
  id1 = request.session['id']
  u=users.objects.raw('SELECT * FROM `pj1_users` WHERE id={}'.format(id1))
  
  return render(request,'showproduct.html',{'pd':pd,'u':u})



  
def showallproducts(request):
    products = Products.objects.all()
    id1 = request.session['id']
    u=users.objects.raw('SELECT * FROM `pj1_users` WHERE id={}'.format(id1))
    return render(request,'showallproducts.html',{
    'pd':products,
    'u':u

  })
    
    
    
def swhileproducts(request):
    
    s=str(request.GET['s'])
    print(s)
    products = Products.objects.raw("SELECT * FROM `pj1_products` WHERE type="+s)

    id1 = request.session['id']
    u=users.objects.raw('SELECT * FROM `pj1_users` WHERE id={}'.format(id1))
    return render(request,'index.html',{
    'pd':products,
    'u':u,
    'id':id1,

  })
    
def showwhileproducts(request):
    
    # if request.GET['s'] == 1:
    products = Products.objects.raw("SELECT * FROM `pj1_products` WHERE type='เมาส์' ")

    id1 = request.session['id']
    u=users.objects.raw('SELECT * FROM `pj1_users` WHERE id={}'.format(id1))
    return render(request,'index.html',{
    'pd':products,
    'u':u,
    'id':id1,

  })
  
  
  
  
  
  
  
def add_product(request):
  form = AddProducts
  id1 = request.session['id']
  u=users.objects.raw('SELECT * FROM `pj1_users` WHERE id={}'.format(id1))
  return render(request,'add_product.html',{'form':form,'u':u,'id':id1})


def add_prod(request):
  form = AddProducts
  
  if request.method == 'POST':
    form = AddProducts(request.POST,request.FILES)
    if form.is_valid():
      form.save()
      return redirect('/showallproducts')
    
    
    
def delete_product(request):
  id = request.POST['id']
  prod = Products.objects.get(id=id)
  prod.delete()
  # redirect('/showallproducts')
  products = Products.objects.all()
  id1 = request.session['id']
  u=users.objects.raw('SELECT * FROM `pj1_users` WHERE id={}'.format(id1))
  return render(request,'showallproducts.html',{
    'u':u,
    'pd':products,
  })
  