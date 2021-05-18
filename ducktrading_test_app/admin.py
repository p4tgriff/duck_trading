from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Security)
admin.site.register(Order)
admin.site.register(BankAccount)


# Register your models here.
