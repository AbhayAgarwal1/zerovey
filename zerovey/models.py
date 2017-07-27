from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
# This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User)
# The additional attributes we wish to include.
	gender	 = models.CharField(blank=False,max_length=40000)
	skin_type = models.CharField(blank=False,max_length=40000)
	hair_type = models.CharField(blank=False,max_length=40000)
	
# Override the __unicode__() method to return out something meaningful!
# Remember if you use Python 2.7.x, define __unicode__ too!
	def __str__(self):
		return self.user.username



class Blog(models.Model):


	author = models.ForeignKey(User,default="", blank=True, null=True)

	title = models.CharField(blank=False,max_length=40000)
	body = models.CharField(blank=False,max_length=40000)


	def __str__(self):
		return self.title












# Create your models here.
