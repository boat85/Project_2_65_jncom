from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages as m
from .models import users
from .models import Products
# from .test import Cuser


def login(request):
  username = request.POST['username']
  password = request.POST['pass']
  
  user=users.objects.all()
  
  for i in user:
    if i.username==username and i.password==password:
      username1 = i.username
      fname = i.fname
      status = i.status_u
      id = i.id
      img = i.images
      
      
      request.session['id'] = id
      request.session['user'] = username1
      request.session['fn'] = fname
      request.session['s'] = status
      # request.session['img'] = img

      return redirect('/index')
    
    
  m.info(request,'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง')
  return redirect('/loginto')




# Create your views here.
def index(request):
  
  products = Products.objects.all()
  
  try:
    id = request.session['id'] 
    user = request.session['user'] 
    fn = request.session['fn'] 
    s = request.session['s'] 
    # img = request.session['img']
  except:
    request.session['id'] = -1
    request.session['user'] = ''
    request.session['fn'] = ''
    request.session['s'] = -1
    # request.session['img'] = ''
  
  
  
  return render(request,'index.html',{
    'id':request.session['id'] ,
    'fn':request.session['fn'] ,
    'user': request.session['user'] ,
    's': request.session['s'] ,
    # 'num':num,
    'pd':products,
    # 'img': request.session['img'],
  })
    




def register(request):
  return render(request,'register.html')





def showuser(request):
  # user=users.objects.all()
  id = request.session['id']
  u=users.objects.raw('SELECT * FROM `pj1_users` WHERE id={}'.format(id))
  
  
  
  return render(request,'showuser.html',{
    'u':u,
    'id':request.session['id'] ,
    'fn':request.session['fn'] ,
    'user': request.session['user'] ,
    's': request.session['s'] ,

    })





def loginto(request):
  
  return render(request,'login.html',{'id':request.session['id'] ,
    'fn':request.session['fn'] ,
    'user': request.session['user'] ,
    's': request.session['s'] ,})




def logout(request):
  request.session['id'] = -1
  request.session['user'] = ''
  request.session['fn'] = ''
  request.session['s'] = -1
  return redirect('/index')




def adduser(request):
  username = request.POST['username']
  fname = request.POST['fname']
  lname = request.POST['lname']
  tell = request.POST['tell']
  nname = request.POST['nname']
  email = request.POST['email']
  address = request.POST['address']
  password = request.POST['password']
  repassword = request.POST['repassword']
  
  if password==repassword:
    if users.objects.filter(username=username).exists():
      m.info(request,'ชื่อผู้ใช้มีคนใช้แล้ว')
      return redirect('/register')
    elif users.objects.filter(email=email).exists():
      m.info(request,'อีเมล์นี้มีคนใช้แล้ว')
      return redirect('/register')
    elif users.objects.filter(tell=tell).exists():
      m.info(request,'เบอร์นี้มีผู้ใช้แล้ว')
      return redirect('/register')
    else:
      users.objects.create(
      username=username,
      fname=fname,
      lname=lname,
      tell=tell,
      nname=nname,
      email=email,
      address=address,
      password=password,
      # images='',
      # status_u = '2'
      )
      
      return redirect('/')
    
  else:
    m.info(request,'รหัสผ่านไม่ต้องกัน')
    return redirect('/register')
  
  

  
def showproduct(request):
  id = request.POST['id']
  pd = Products.objects.raw('SELECT * FROM `pj1_products` WHERE id = {}'.format(id))
  
  
  
  return render(request,'showproduct.html',{'pd':pd,'id':request.session['id'] ,
    'fn':request.session['fn'] ,
    'user': request.session['user'] ,
    's': request.session['s'] ,})



def admin_u(request):
  return render(request,'admin_u.html',{'id':request.session['id'] ,
    'fn':request.session['fn'] ,
    'user': request.session['user'] ,
    's': request.session['s'] ,})