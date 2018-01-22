from django.conf.urls import url
from django.contrib import admin


from views import singnup_view,profile,indexview1,login_user,logout_view,activate,dashboard ,feedback,password,post_view , change_password
from django.conf.urls import url
urlpatterns = [
    url(r'^$', indexview1),
    url(r'^signup/',singnup_view),
   # url(r'^index/',indexview1),
    url(r'^login/',login_user),
    url(r'^logout/',logout_view),
    url(r'^activate/',activate),
    url(r'^profile/',profile),
    url(r'^activate/',activate),
    url(r'^dashboard/',dashboard),
    url(r'^feedback/',feedback),
    url(r'^post/', post_view),
  #  url(r'^comment/', comment_view),
    url(r'^password/',password),
    url(r'^dashboard/',dashboard),
    url(r'^feedback/',feedback),
    url(r'^password/',password),
    url(r'^password_change/',change_password),


]