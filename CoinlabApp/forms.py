from django import forms
from models import loginmodel,password_rest,signupmodel,indexmodel

class Signupform(forms.ModelForm):
    class Meta:
        model=signupmodel
        fields=['name','email','password','re_password']

class Indexform(forms.ModelForm):
    class Meta:
        model=indexmodel
        fields=['first_name','last_name','subject']

class Loginform(forms.ModelForm):
    class Meta:
        model=loginmodel
        fields=['email','password']

class Resetform(forms.ModelForm):
    class Meta:
        model=password_rest
        fields=['new_password','renew_password']

