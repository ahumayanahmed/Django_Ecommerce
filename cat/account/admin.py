from django.contrib import admin
from account.models import UserRegistration
from account.models import account
# Register your models here.
admin.site.register(UserRegistration)
admin.site.register(account)