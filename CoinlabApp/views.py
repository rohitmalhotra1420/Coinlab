# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from models import signupmodel,loginmodel,password_rest,SessionToken,indexmodel
from forms import Signupform,Resetform,Loginform,Indexform
from django.core.mail import EmailMessage
from twilio.rest import Client
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
account_sid = "ACcee93f758892db32f0920ab88b1ca945"
auth_token = "144914bd933e248294d546ae74479862"
client = Client(account_sid, auth_token)


def signup_view(request):
    print "signup called"
    if request.method=='POST':
        print "post start"
        form=Signupform(request.POST)
        print "post sucessfully called"
        if form.is_valid():
            print "form inside"
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            re_password=form.cleaned_data['re_password']
            if password==re_password:
                print "password match"
                user=signupmodel(name=name,password=password,email=email,re_password=re_password)
                user.save()
                return render(request,'login.html')
            else:
                print "password didn't match"
        else:
            print " "
    elif request.method=='GET':
        form=Signupform()
    return render(request,'signup.html',{'form':form})


def indexview(request):
    if request.method == 'POST':
        form = Indexform(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name= form.cleaned_data['last_name']
            subject = form.cleaned_data['subject']
            user = indexmodel(first_name=first_name,last_name=last_name,subject=subject )
            user.save()
            message=subject
            email = EmailMessage('CONTACT_US', message, to=['vaidishan9@gmail.com'])
            email.send()
            return render(request, 'index.html')
        else:
            print " "
    elif request.method == 'GET':
        form = Indexform()
    return render(request, 'index.html', {'form': form})


def profile(request):
    if request.method=='POST':
         return render(request,'profile.html')
    elif request.method=='GET':
        return render(request,'profile.html')


def login_user(request):
    print 'loin page called'
    response_data = {}
    print 'responsedata'
    if request.method == "POST":
        print "post start"
        form = Loginform(request.POST)
        print "post end"
        if form.is_valid():
            print "login form start"
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = loginmodel.objects.filter(username=username).first()
            email = EmailMessage('Login Alert', 'welcome to instaclone!!!!', to=['vaidishan9@gmail.com'])
            email.send()
            message = client.api.account.messages.create(to="+918930841996",
                                                         from_="+15202638729",
                                                         body="Hey coinlabworks!!!")
            print message.sid
            #message.send()
            print "login form end"
            if user:
                # Check for the password
                if check_password(password, user.password):
                    print 'User is valid'
                    token = SessionToken(user=user)
                    token.create_token()
                    token.save()
                    response = redirect('/login/')
                    response.set_cookie(key='session_token', value=token.session_token)
                    return response
                else:
                    print 'User is invalid'
                    response_data['message'] = 'Incorrect Password! Please try again!'
    elif request.method == "GET":
        print "failed"
        form = Loginform()

    response_data['form'] = form
    return render(request, 'login.html', response_data)



def check_validation(request):
    if request.COOKIES.get('session_token'):
        session = SessionToken.objects.filter(session_token=request.COOKIES.get('session_token')).first()
        if session:
            time_to_live = session.created_on + timedelta(days=1)
            if time_to_live > timezone.now():
                return session.user
    else:
        return None

def logout_view(request):
    user=check_validation(request)
    if user:
        token=SessionToken.objects.filter(user=user)
        token.delete()
        return redirect('/login/')
    else:
        return redirect('/login/')

