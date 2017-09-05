# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import password_rest,loginmodel,signupmodel,indexmodel


admin.site.register(password_rest)
admin.site.register(loginmodel)
admin.site.register(signupmodel)
admin.site.register(indexmodel)

# Register your models here.
