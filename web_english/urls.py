"""marion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web_english import views

urlpatterns = [
    path('', views.index, name="home"),
    path('blog', views.blog, name="blog"),
    path('singup', views.singup, name="singup"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('profile',views.profile,name="profile"),
    path('all_blog',views.allblog,name="allblog"),
    path('all_blog/<str:category>/',views.allblogcategory,name="allblogcategory"),
    path('search_app',views.searchapp,name="searchapp"),
    path('android_stor',views.android_stor,name="android_stor"),
    path('android_course',views.android_course,name="android_course"),
    path('updateprofile',views.updateprofile,name="updateprofile" ),
    path('details_blog/<int:id>/', views.details_blog, name="details_blog"),
    path('category/<str:category>/', views.category, name="category"),
    path('view_course/<int:id>/', views.view_course, name="view_course"),
]
