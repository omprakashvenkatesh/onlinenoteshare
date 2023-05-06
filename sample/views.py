from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.core import mail
from sample import models
import random



# Create your views here.

def display(request):
    return render(request,'index.html')

def indexpage(request):
  return render(request,'index.html')

def view_mynotes(request):
   
    user = User.objects.get(id=request.user.id)
    notes = Notes.objects.filter(user = user)

    d = {'notes':notes}
    return render(request,'view_mynotes.html',d)

def signup2(request):
    error=""
    if request.method=='POST':
       uname = request.POST.get('name') 
       cont = request.POST.get('contact')
       email = request.POST.get('emailid')
       passc = request.POST.get('password')
       otpbox = request.POST.get('otpbox')
       br1 = request.POST.get('branch')
       data ={
           uname,cont,email,passc,br1,otpbox
       }
       try:
          if data is not None:
             my_user = User.objects.create_user(uname,email,passc)
             Signup.objects.create(user=my_user,email=email,contact=cont,branch=br1)
             my_user.save()
             error="no"
          else:
             error="yes"
       except:
             error="yes"
   
    return render(request,'signup.html')
def loginpage(request):
    error=""
    if request.method=="POST":
        uname = request.POST.get('name')
        passc = request.POST.get('pass')

        user = authenticate(request,username=uname,password=passc)
        if user is not None:
            login(request,user)
            error="no"
            
        else:
            error="yes"
         
    return render(request,'login.html',locals())
       
def profilepage(request): 
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    signup1 = Signup.objects.filter(user = user)
    d = {'signup':signup1}

    return render(request,'profile.html',d)
  



    
def contactpage(request):
    if request.method == 'POST':
       usname = request.POST['name']
       mailid = request.POST['mailbox']
       phone = request.POST['phonenumber']
       message = request.POST['message']

        
    return render(request,'contact.html',locals())  
       
def sendotp(request):
        uname = request.POST.get('name') 
        cont = request.POST.get('contact')
        email = request.POST.get('emailid')
        passc = request.POST.get('password')
        otpbox = request.POST.get('otpbox')
        br1 = request.POST.get('branch')
        email = request.POST.get('emailid')
        otpverify = random.randint(10000,99999)
        str(otpverify)
        mail = EmailMessage(
           subject='OTP verification',
           body = 'Here your otp is: ' +str(otpverify),
           from_email = "omprakashvenkatesh11@gmail.com",
           to =
           [email],
        )
        mail.send()
        
       

        return render(request,"signup.html",{"uname":uname,"cont":cont,"email":email,"passc":passc,"otpbox":otpbox,"br1":br1,"otpverify":otpverify})
    
def editprofile(request):
   
    return render(request,'editprofile.html')

def aboutpage(request):
    return render(request,'about.html')

def redirectpage(request):
  return render(request,'redirect.html')

def register(request):
    error=""
    if request.method=="POST":
      uname = request.POST.get('name') 
      cont = request.POST.get('contact')
      email = request.POST.get('emailid')
      passc = request.POST.get('password')
      otpbox = request.POST.get('otpbox')
      br1 = request.POST.get('branch')
      data ={
           uname,cont,email,passc,br1,otpbox
       }
      try:
        if data is  not None:
         my_user = User.objects.create_user(username=uname,email=email,password=passc)
         obj = models.Signup()
         obj.user = my_user
         obj.email= email
         obj.contact= cont
         obj.branch= br1
         obj.save()
         
        
      except:
          return redirect('signup')
      


     


      return render(request,'redirect.html')

def Logout(request):
    logout(request)
    return redirect('login')
