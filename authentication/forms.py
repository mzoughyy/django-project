from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models  import profile
from django.forms import ModelForm

from .models import ChatMessage

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
        fields = ('CIN','phone','appartment','parking_spot','second_parking','image')
        widgets = {
            'CIN':forms.NumberInput(attrs={'class':'form-control'}),
            'appartment':forms.Select(attrs={'class':'form-control form-group','width':'500px',"placeholder":"apprtmentS",'style': 'width:230px'}),
            'parking_spot':forms.Select(attrs={'class':'form-control form-group','style': 'width:230px'}),
            'second_parking':forms.Select(attrs={'class':'form-control hidden form-group','id':'input-field','style': 'width:230px'}),

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
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={"class":"form-control"}), required=False)



    class Meta:
        model = profile
        fields = ('CIN','phone','appartment','parking_spot','image')
        widgets = {
            'CIN':forms.NumberInput(attrs={'class':'form-control'}),
            'appartment':forms.Select(attrs={'class':'form-control form-group','width':'500px',"placeholder":"apprtmentS",'style': 'width:230px'}),
            'parking_spot':forms.Select(attrs={'class':'form-control form-group','style': 'width:230px'}),



        }

class EmailForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Subject","class":"form-control"}))   
    message = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Message","class":"form-control"}))    
 

class ChatMessageForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={"class":"forms", "rows":3, "placeholder": "Type message here"}))
    class Meta:
        model = ChatMessage
        fields = ["body",]

class EmailUs(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Name","class":"form-control"}))   
    email = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Email","class":"form-control "}))    
    phone = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Phone"}))

