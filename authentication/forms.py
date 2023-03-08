from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models  import profile
from django.forms import ModelForm



class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"First Name","class":"form-control"}))    
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Last Name","class":"form-control"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"username","class":"form-control"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder":"Email","class":"form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password","class":"form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirm your password","class":"form-control"}))
    

    class Meta:
        model = User 
        fields = ['first_name','last_name','username','email','password1','password2']

class UserProfileForm(ModelForm):
    phone = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Phone Number"}))


    class Meta:
        model = profile
        fields = ('CIN','phone','appartment','parking_spot','image')
        widgets = {
            'CIN':forms.NumberInput(attrs={'class':'form-control'}),
            'appartment':forms.Select(attrs={'class':'form-control form-group','width':'500px',"placeholder":"apprtmentS",'style': 'width:230px'}),
            'parking_spot':forms.Select(attrs={'class':'form-control form-group','style': 'width:230px'}),
            'image':forms.FileInput(attrs={'class':'form-group','style': 'width:230px'}),



        }
class UserUpdateForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))    
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = User 
        fields = ['first_name','last_name','username','email']
class UpdateProfileForm(ModelForm):
    phone = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control"}))


    class Meta:
        model = profile
        fields = ('CIN','phone','appartment','parking_spot')
        widgets = {
            'CIN':forms.NumberInput(attrs={'class':'form-control'}),
            'appartment':forms.Select(attrs={'class':'form-control form-group','width':'500px',"placeholder":"apprtmentS",'style': 'width:230px'}),
            'parking_spot':forms.Select(attrs={'class':'form-control form-group','style': 'width:230px'}),


        }

