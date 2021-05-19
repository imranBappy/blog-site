from django import forms
from django.contrib.auth.models import User
from .models import ProfilUpdate,Category,Blog

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "last_name":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
        }
        
class ProForm(forms.ModelForm):
    class Meta:
        model=ProfilUpdate
        fields=["image"]
        widgets={
            "image":forms.FileInput(attrs={"class":"form-control col-lg-3"}),
        }