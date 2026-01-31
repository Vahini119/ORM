
from django.db import models
from django.contrib import admin
class fooddelivery(models.Model):
             name=models.CharField(max_length=12);
             email=models.EmailField();
             order_id=models.IntegerField(primary_key=True);
             address=models.CharField(max_length=25);
             order=models.CharField(max_length=15);
             money =models.FloatField();
             mobile_no=models.IntegerField();
class fooddeliveryAdmin(admin.ModelAdmin):
    list_display =['name','email','order_id','address','order','money','mobile_no'];

   

