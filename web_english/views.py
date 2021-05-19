from django.shortcuts import render,redirect
from .models import Head_titel,ProfilUpdate,Android_stor,App_Category,AppList,Content_2
from .models import Blog,Subscription,Our_team,Brand_logo,Category,Course,Content_1
from math import ceil

from django.contrib.auth.models import User
from django.contrib import auth
from .forms import UserForm,ProForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):
    blog=Blog.objects.all()
    team=Our_team.objects.all()
    sliderhead=Head_titel.objects.all()
    contant_1=Content_1.objects.all()
    contant_2=Content_2.objects.all()
    sendblog={
        'blog':blog,
        "team":team,
        "sliderhead":sliderhead,
        "contant_1":contant_1,
        "contant_2":contant_2,
    }
    if request.method=="POST":
        subscribe=request.POST.get("Subscription_email")
        mile=Subscription(mail=subscribe)
        mile.save()
    return render(request,"index.html",sendblog)
def blog(request):
    blog=Blog.objects.all()
    blogcategory=Category.objects.all()
    sliderhead=Head_titel.objects.all()
    sendblog={
        'blog':blog,
        'category':blogcategory,
        "sliderhead":sliderhead
    }
    return render(request,"blog.html",sendblog)
def details_blog(request,id):
    blog=Blog.objects.filter(id=id)
    sendblog={
        'blog':blog
    }
    return render(request,"details_blog.html",sendblog)
def category(request,category):
    blog=Blog.objects.filter(category=category)
    blogcategory=Category.objects.all()
    sliderhead=Head_titel.objects.all()
    sendblog={
        'blog':blog,
        'category':blogcategory,
        "sliderhead":sliderhead
    }
    return render(request,"category.html",sendblog)
def singup(request):
    f_name=request.POST.get("f_name")
    l_name=request.POST.get("l_name")
    email=request.POST.get("email")
    passw=request.POST.get("password")
    cpassw=request.POST.get("confirmpassword")
    propic=request.FILES["propic"] 
    if request.method=="POST":
        if passw==passw:
            try:
                user=User.objects.get(username=email)
                return render(request,"index.html",{'error':"User already exists"})  
            except User.DoesNotExist:
                user=User.objects.create_user(username=email,password=cpassw,first_name=f_name,last_name=l_name)
                return render(request,"index.html",{'success':"user created successfully"})    
        else:
            return render(request,"index.html")
    else: 
        return redirect(index)
def login(request):
    email=request.POST.get("email")
    passw=request.POST.get("password")
    if request.method=="POST":
       user=auth.authenticate(username=email,password=passw)
       if user is not None:
            auth.login(request,user)
            return redirect(index) 
       else:
            return render(request,"index.html",{'error_login':"Invalide User and Password"})
    else: 
        return redirect(index)
def logout(request):
    auth.logout(request)
    return redirect(index)
def profile(request):
    return render(request,"profile.html")
def updateprofile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            ufrom=UserForm(request.POST,instance=request.user)
            pfrom=ProForm(request.POST,request.FILES,instance=request.user.profilupdate)
            if ufrom.is_valid() and pfrom.is_valid():
                ufrom.save()
                pfrom.save()
                return render(request,"profile.html",{"pro_update":"Profile Update successfully"})
        else:
            ufrom=UserForm(instance=request.user)
            pfrom=ProForm(instance=request.user.profilupdate)
        return render(request,"updateprofile.html",{"userfrom":ufrom,"pfrom":pfrom})
    else:
        return redirect(login)
def android_stor(request):
    appstor=Android_stor.objects.all()
    appcategory=App_Category.objects.all()
    applist=AppList.objects.all()
    sendvar={
        'apppost':appstor,
        'category':appcategory,
        'applist':applist
    }
    return render(request,"android_stor.html",sendvar)
def allblog(request):
    blog=Blog.objects.filter(category=category)
    blogcategory=Category.objects.all()
    blogpost=Blog.objects.all()
    sendblog={
        'blog':blog,
        'category':blogcategory,
        'blogpost':blogpost
    }
    return render(request,"allblog.html",sendblog)
def allblogcategory(request,category):
    blog=Blog.objects.filter(category=category)
    blogcategory=Category.objects.all()
    sendblog={
        'blog':blog,
        'category':blogcategory,
    }
    return render(request, "allblogcategory.html",sendblog)
def searchapp(request):
    search=request.POST.get("searchapp")
    appstortitel=Android_stor.objects.filter(titel__icontains=search)
    appstorbody=Android_stor.objects.filter(body__icontains=search)
    appstor=appstortitel.union(appstorbody)
    sendvar={
        'apppost':appstor,
    }
    return render(request,"searchapp.html",sendvar)
def android_course(request):
    allcourse=Course.objects.all()
    sliderhead=Head_titel.objects.all()
    contant_1=Content_1.objects.all()
    contant_2=Content_2.objects.all()
    n= len(allcourse)
    nsliders=n//4 + ceil((n/4)+(n//4))
    sendvar={
        'allcourse':allcourse,
        'sliderhead':sliderhead,
        "contant_1":contant_1,
        "contant_2":contant_2,
        'no_of_slides':nsliders,
        'product': allcourse
    }
    return render(request, "android_course.html",sendvar)
def view_course(request,id):
    view_course=Course.objects.filter(id=id)
    sendvar={
        "view_course":view_course,
    }
    return render(request, "course.html",sendvar)