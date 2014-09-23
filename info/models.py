from django.db import models

class server_list(models.Model):
	host = models.CharField(max_length=20)
	ip   = models.IPAddressField()
	def __unicode__(self):
		return "%-14s:    %s" % (self.host,self.ip)

class User(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=200)
	def __unicode___(self):
		return self.username

class logpath(models.Model):
	project = models.CharField(max_length=20)
	ip	= models.IPAddressField()
	path    = models.TextField()
	def __unicode__(self):
		return self.project
