from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


class workshops(models.Model):
	title1 = models.CharField(max_length=200, null=True)
	bdate = models.DateTimeField(max_length=200, null=True)
	address = models.CharField(max_length=200, null=True)

	type = models.CharField(max_length=200, null=True)
	conducted = models.CharField(max_length=200, null=True)
	level = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.title1

class seminars(models.Model):
	title1 = models.CharField(max_length=200, null=True)
	bdate = models.DateTimeField(max_length=200, null=True)
	address = models.CharField(max_length=200, null=True)

	type = models.CharField(max_length=200, null=True)
	conducted = models.CharField(max_length=200, null=True)
	level = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.title1


class Employee(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    doj = models.DateField(null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    post = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    active = models.BooleanField(default=True)
    leave_count = models.IntegerField(null=True, blank=True, default=0)
    on_leave = models.BooleanField(default=False)