# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid

class signupmodel(models.Model):
    name=models.CharField(max_length=120)
    email=models.EmailField()
    password=models.CharField(max_length=400)
    re_password=models.CharField(max_length=400)

    def __str__(self):
        self.name
class indexmodel(models.Model):

    first_name=models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    subject= models.CharField(max_length=400)

    def __str__(self):
        self.first_name

class loginmodel(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=400)

    def __str__(self):
        self.email

class password_rest(models.Model):
    new_password=models.CharField(max_length=400)
    renew_password=models.CharField(max_length=400)


class SessionToken(models.Model):
    user = models.ForeignKey(signupmodel)
    session_token = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)

    def create_token(self):
        self.session_token = uuid.uuid4()
# Create your models here.
