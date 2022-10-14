from os import name
from telnetlib import STATUS
from xmlrpc.client import Boolean
from django.core.checks import messages
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
# Create your models here.

class Tasklist(models.Model):

    clientname= models.CharField(max_length=100,null=True,blank=True)
    task = models.CharField(max_length=100)
    startdate = models.DateField(default=timezone.now, blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    assignee = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    priority = models.CharField(max_length=100,null=True)
    fstatus = models.BooleanField(default=False)

    def __str__(self):
        return self.task + " - Task - " + str(self.fstatus)

class edit_page(models.Model):

    old_id = models.ForeignKey(Tasklist,null=True,on_delete=models.CASCADE)
    updatedate = models.DateField(blank=True, null=True)
    time_from = models.TimeField(blank=True, null=True)
    time_to = models.TimeField(blank=True, null=True)
    messagelogs = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='',default=True)

    def __str__(self):
        return self.messagelogs

class gst_master(models.Model):

    id = models.AutoField(primary_key=True)
    legal_name = models.CharField(max_length = 100,null=True)
    trade_name = models.CharField(max_length = 100,null=True)
    gst_no = models.CharField(max_length = 100,null=True)
    gst_username = models.CharField(max_length = 100,null=True)
    gst_pwd = models.CharField(max_length = 100,null=True)
    pan_no = models.CharField(max_length = 100,null=True)
    company_name = models.CharField(max_length = 100,null=True)
    org = models.CharField(max_length = 100,null=True)
    con_person = models.CharField(max_length = 100,null=True)
    state = models.CharField(max_length = 100,null=True)
    city = models.CharField(max_length = 100,null=True)
    address1 = models.CharField(max_length = 1000,null=True)
    address2 = models.CharField(max_length = 1000,null=True)
    email1 = models.EmailField(null=True)
    email2 = models.EmailField(null=True)
    pincode = models.IntegerField(null=False)
    phone = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.legal_name

class emp(models.Model):
    
    emp_name = models.CharField(max_length=100,null=True)
    date = models.DateField(blank=True,null=True)
    intime = models.TimeField(blank=True,null=True)
    outtime = models.TimeField(blank=True,null=True)

class work(models.Model):

    emp_name = models.CharField(max_length=100,null=True)
    client = models.CharField(max_length=100,null=True)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True,null=True)
    work_from = models.TimeField(blank=True,null=True)
    work_to = models.TimeField(blank=True,null=True)
    file = models.FileField(upload_to='',default=True)

class client(models.Model):
    
    name = models.CharField(max_length=100,null=True)
    pan = models.CharField(max_length=100,null=True)
    #res_per_name = models.CharField(max_length=100,null=True)
    #name = models.CharField(max_length=100,null=True)
    #designation = models.CharField(max_length=100,null=True)
    #c_no = models.IntegerField(max_length=10,null=True)
    #email = models.EmailField(null=True)
    #cc = models.EmailField(null=True)
    #address1 = models.CharField(max_length=100,null=True)
    #address2 = models.CharField(max_length=100,null=True)
    #city = models.CharField(max_length=100,null=True)
    #state = models.CharField(max_length=100,null=True)
    #pincode = models.IntegerField(max_length=6,null=True)

    def __str__(self):
        return self.name

class list(models.Model):

    company_name = models.CharField(max_length=100,null=True)
    file_name = models.CharField(max_length=100,primary_key=True)
    ay = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.company_name
