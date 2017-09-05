from django.conf.urls import url
from django.contrib import admin
from views import signup_view,indexview,login_user,logout_view,profile

urlpatterns = [
    url(r'^$', indexview),
    url(r'^login/',login_user),
    url(r'^logout',logout_view),
    url(r'^signup/',signup_view),
    url(r'^index/',indexview),
    url(r'^profile/',profile),
]