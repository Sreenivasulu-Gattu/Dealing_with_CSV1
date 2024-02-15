from django.contrib import admin

# Register your models here.
from app.models import *

class cust(admin.ModelAdmin):
    list_display = ['bank_name']
class cust2(admin.ModelAdmin):
    list_display = ['bank_name','ifsc','branch','address','contact','city','district','state']

admin.site.register(Bank,cust)

admin.site.register(Branch,cust2)
