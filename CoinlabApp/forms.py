

from models import UserModel, indexmodel , feedback_model,PostModel


from django import forms

class SignUpForm(forms.ModelForm):
  class Meta:
    model = UserModel
    fields=['email','name','password','re_password']


class Indexform1(forms.ModelForm):
    class Meta:
        model=indexmodel
        fields=['first_name','last_name']

class LoginForm(forms.ModelForm):
    class Meta:
      model = UserModel
      fields = ['email', 'password']


class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['image', 'caption']


class feedback_form(forms.ModelForm):
    class Meta:
        model=feedback_model
        fields=['first_name','last_name','subject']

class password_form(forms.ModelForm):
    class Meta:
        model=UserModel
        fields=['password','re_password']