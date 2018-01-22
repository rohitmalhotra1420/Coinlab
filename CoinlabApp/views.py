from __future__ import unicode_literals

import os

from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import EmailMessage
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from twilio.rest import Client
from imgurpython import ImgurClient
import json
import requests



from forms import LoginForm, SignUpForm, Indexform1,  feedback_form, password_form,PostForm , change_pwd_form
from models import UserModel, SessionToken, indexmodel, feedback_model,PostModel,project_model

CLIENT_ID = '2e8b96d3df82469'
CLIENT_SECRET = 'f6292d93b81e0f055521eb71084b63b9ccc5329d'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
account_sid = "ACcee93f758892db32f0920ab88b1ca945"
auth_token = "144914bd933e248294d546ae74479862"
client = Client(account_sid, auth_token)
postive = ["beautiful", "clean", "Hygenic"]
negative = ["pollution", "dirty", "unhygenic", "unsafe"]


def singnup_view(request):
    print ' signup view called'
    if request.method == "POST":
        print ' post called'
        form = SignUpForm(request.POST)
        if form.is_valid():
            print ' form is valid'
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            re_password = form.cleaned_data['re_password']
            print name, email
            user = UserModel(email=email, name=name, password=make_password(password),
                             re_password=make_password(re_password))
            user.is_active = False
            user.save()
            try:

                emaill = EmailMessage('Activation Link', ' HEY...Welcome To CHANGE.IO ....'
                                                         '.click on the link below to get your account activated \n\n '
                                                         'http://127.0.0.1:8000/activate/?email=' + email,
                                      to=[email])
                emaill.send()
                print "email send"
            except:
                print ' network error in sending the mail'

            print ' user saved'
            return render(request, 'activate_link.html')
        else:
            print ' form invalid'
    elif request.method == "GET":
        print ' get called'
        form = SignUpForm()
    print "signup view end"
    return render(request, 'signup.html', {'form': form})


def activate(request):
    print 'Activate called'
    email = request.GET.get('email')
    # name=request.GET.get('name')
    print email
    # print name
    user_object = UserModel.objects.filter(email=email).all()
    print user_object.first()
    user_obj = user_object.first()
    try:
        print 'activate user called'
        print  user_obj.name, user_obj.is_active

        if user_object:
            if user_obj.is_active == False:
                user_obj.is_active = True
                print 'user has been activated'
                user_obj.save()
                return HttpResponseRedirect('/login/')
            else:
                print ' user has been alreay activated'
                return HttpResponseRedirect('/login/')
        else:
            print ' no user returned'
    except:
        pass
    return render(request, 'login.html', )


def profile(request):
   print "profile called"
   user=check_validation(request)
   print "user validation in profile checked"
   print user
   if user:
        print "user detalied 1st if"
        user_now=UserModel.objects.filter(name=user).first()
        print ' user email is ' , user_now.email


        return render(request,'profile.html',{'user':user,'email':user_now.email})
   else :
       print ' user not loggedin '
       return redirect('/login/')

   return render(request,'profile.html')
# login function

def login_user(request):
    print 'login page called'
    response_data = {}
    print response_data
    print "response data called"
    if request.method == "POST":
        print "login post called"
        form = LoginForm(request.POST)
        print "login form request post"
        if form.is_valid():
            print "form valid sstart"
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = UserModel.objects.filter(email=email).first()
            print "user accepted "
            if user:
                if user.is_active == True:
                    print "user is true"
                    # message.send()

                    # Check for the password
                    if check_password(password, user.password):
                        print 'User is valid'
                        try:

                            emaill = EmailMessage('You just Logged in...',
                                                  ' HEY...You just Logged in on for CHANGE.IO ....Report if it was not you'
                                                  ,
                                                  to=[email])
                            emaill.send()
                            print "email send"
                        except:
                            print ' network error in sending the mail'
                        print "session token start"
                        token = SessionToken(user=user)
                        print user
                        print "session token result taken"
                        token.create_token()
                        print "create token start - end"
                        token.save()
                        print 'token saved'
                        response = HttpResponseRedirect('/profile/')
                        print 'redirected to ', response
                        response.set_cookie(key='session_token', value=token.session_token)
                        return response
                    else:
                        print 'User is invalid'
                        response_data['message'] = 'Incorrect Password! Please try again!'
                else:
                        print "user not active"
            else:
                print 'user has not been activated'
                response_data['message'] = 'You have not been activated ...Please check your mail!'

    elif request.method == "GET":
        print "get method called"
        form = LoginForm()

    response_data['form'] = form
    return render(request, 'login.html', response_data)


# post function

def check_validation(request):
    if request.COOKIES.get('session_token'):
        session = SessionToken.objects.filter(session_token=request.COOKIES.get('session_token')).first()
        if session:
            return session.user
    else:
        return None


def logout_view(request):
    print ' lgogged out'
    user = check_validation(request)
    if user:
        token = SessionToken.objects.filter(user=user)
        token.delete()
        return redirect('/dashboard/')
    else:
        return redirect('/login/')




def change_password(request):
    print "change passsword called"
    user = check_validation(request)
    print "user validation in change password checked"
    if request.method == "POST":
        if user:
            print "user valid"
            user_now = UserModel.objects.filter(name=user).first()
            print ' user email is ', user_now.email
            form = change_pwd_form(request.POST)
            print "login form request post"
            if form.is_valid():
                print "form valid sstart"
                new_pwd = form.cleaned_data.get('password')
                user_now.password=make_password(new_pwd)
                user_now.save()
                try:
                    emaill = EmailMessage('You just Changed password...',
                                          ' HEY...You just changed pssword on for CHANGE.IO ....Report if it was not you'
                                          ,
                                          to=[user_now.email])
                    emaill.send()
                    print "email send"
                except:
                    print ' network error in sending the mail'
                print "the following user asked to change password ", user , new_pwd
                return redirect('/logout/')
        else:
            print ' user not loggedin '
            return redirect('/login/')
    elif request.method == "GET":
            print "get method called"
            return render(request,'password.html',{'user':user})


    return  render(request,'password.html')


# Create your views here.
def indexview1(request):
    if request.method == 'POST':
        form = Indexform1(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            # subject = form.cleaned_data['subject']
            user = indexmodel(first_name=first_name, last_name=last_name)
            user.save()
            try:
                # email = form.cleaned_data.get('email')
                emaill = EmailMessage('Feedback', 'New suggestion form' + (first_name),
                                      to=['instacloneapp@gmail.com'])
                emaill.send()
                print "email send"
            except:
                print ' network error in sending the mail'

            return render(request, 'index.html')
        else:
            print " "
    elif request.method == 'GET':
        form = Indexform1()
    return render(request, 'index.html', {'form': form})


def logout_view(request):
    user = check_validation(request)
    if user:
        token = SessionToken.objects.filter(user=user)
        token.delete()
        return redirect('/login/')
    else:
        return redirect('/login/')




def dashboard(request):
    print 'dashboard called'
    '''user = check_validation(request)
    print 'vakidation returned', user
    if user:
        # if user is valid getting all the posts from the user
        print 'authentic user'

        user_now = UserModel.objects.filter(name=user).first()
        print 'welcome', user_now
    else:
        return HttpResponseRedirect('/login/')'''
    return render(request, 'index.html')


def feedback(request):
    print 'feedback called'
    if request.method == "POST":
            print ' post called'
            form = feedback_form(request.POST)
            if form.is_valid():
                print ' feedback form form is valid'
                first = form.cleaned_data.get('first_name')
                last = form.cleaned_data.get('last_name')
                subject = form.cleaned_data.get('subject')
                feedback = feedback_model(first_name=first, last_name=last, subject=subject)
                feedback.save()
                try:
                    mail = 'vaidishan9@gmail.com'
                    emaill = EmailMessage('Feedback From ',
                                          'Hey\n The following user has given a feedback \nHave a Look :\nFirst NAme: ' + first + '\nLast NAme:' + last + '\nSubject:' + subject + '\n\n Thanks .'
                                          ,
                                          to=[mail])
                    emaill.send()
                    print "feedback email is  send"
                except:
                    print ' network error in sending the mail'
                print feedback
                return HttpResponseRedirect('/dashboard/')
            else:
                print ' feedback form invalid'
                return HttpResponseRedirect('/dashboard/')
    elif request.method == 'GET':
        form = feedback_form()

    return render(request, 'index.html')


def password(request):
    print 'password page called'
    user = check_validation(request)
    if user:
        print 'user is valid'
        if request.method == "POST":
            print ' post called'
            form = password_form(request.POST)
            if form.is_valid():
                print 'password form is valid '

                password = form.cleaned_data.get('password')
                re_password = form.cleaned_data.get('re_password')
                user_obj = UserModel.objects.filter(name=user).first()
                print user_obj
                print user_obj.email
                print password, re_password
                # try:
                mail = 'vaidishan9@gmail.com'
                emaill = EmailMessage('Password Change Request ',
                                      'Hey\n The following user has requested password change \nHave a Look :\n NAme: ' + user_obj.name + '\nEMail:' + user_obj.email + '\n New PAssword: ' + re_password + '\n\n Please confirm .Thanks .'
                                      , to=[mail])
                emaill.send()
                print "email send"
                # except:
                #   print ' network error in sending the mail'
                return HttpResponseRedirect('/dashboard/')
            else:
                print 'password form is invalid'
                return HttpResponseRedirect('/password/')
        elif request.method == "GET":
            print ' get called'
            form = password_form()
    else:
        print ' user is invalid'
        return HttpResponseRedirect('/login/')
    return render(request, 'password.html')


def post_view(request):
    user = check_validation(request)
    print "post view called"
    if user:
        print 'Authentic user'
        # if request.METHOD == 'GET':
        #   form = PostForm()
        if request.method == 'POST':
            print 'post called'
            form = PostForm(request.POST, request.FILES)
            print form
            if form.is_valid():
                print 'form is valid'
                image = form.cleaned_data['image']
                caption = form.cleaned_data['caption']
                print user
                print image
                print caption
                print BASE_DIR
                print "before basedr"
                post = PostModel(user=user, image=image, caption=caption)
                post.save()
                path = (r'C:/Users/ROADBLOCK/Desktop/user_images' + '/' + post.image.url)
                print "after basedr"
                print path
                client = ImgurClient(CLIENT_ID, CLIENT_SECRET)
                post.image_url = client.upload_from_path(path, anon=True)['link']
                post.save()
                redirect('/feed/')
            else:
                print ' form is invalid '

        else:
            print ' get is called'
            form = PostForm()
            print form
            # return (request,'upload.html')
    else:
        return redirect('/login/')
    return render(request, 'upload.html')




'''
def comment_view(request):
    user = check_validation(request)
    if user and request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post_id = form.cleaned_data.get('post').id
            comment_text = form.cleaned_data.get('comment_text')
            comment = CommentModel.objects.create(user=user, post_id=post_id, comment_text=comment_text)
            comment.save()
            email = EmailMessage('NEW COMMENT ', ' New Comment on  post', to=['vaidishan9@gmail.com'])
            email.send()

            return redirect('/feed/')
        else:
            return redirect('/feed/')
    else:
        return redirect('/login')
'''