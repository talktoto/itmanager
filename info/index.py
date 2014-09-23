from django  import forms
from models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response


class reguser(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)


def  userfrom(req):
	if req.method == "POST":
		userinfo = reguser(req.POST)
		if  userinfo.is_valid():
			username   = userinfo.cleaned_data['username']
			password   = userinfo.cleaned_data['password']
			User.objects.create(username=username,password=password)
			print userinfo.cleaned_data
			return HttpResponseRedirect('/login')
		else:
			return HttpResponseRedirect('/reguser')
	else:
	   userinfo = reguser()	
	return render_to_response('reguser.html',{'input_userinfo':userinfo})		


def login(req):
	if req.method == "POST":
		userinfo = reguser(req.POST)
		if userinfo.is_valid():
			username = userinfo.cleaned_data['username']
			password = userinfo.cleaned_data['password']
			user = User.objects.filter(username__exact=username,password__exact=password)
			print username,password
			if user:
				response =  HttpResponseRedirect('/in')
				response.set_cookie('username',username,3600)
				req.session['username'] = username
				return response
			else:
				return HttpResponseRedirect('/login')
	else:
		userinfo = reguser()
	return render_to_response('login.html',{'input_userinfo':userinfo})

def in1(req):
	user = req.session.get('username')
	print user
	if user:
		return render_to_response('in.html',{'user':user})
	else:
		return HttpResponseRedirect('/login')

def logout(req):
	response = HttpResponse()
	response.delete_cookie('username')
	del req.session['username']
	return HttpResponseRedirect('/login')
