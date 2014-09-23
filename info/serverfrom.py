from django import forms
from django.shortcuts import render_to_response
from django.http  import HttpResponse,HttpResponseRedirect
from info.models import server_list
from info.index import login

class host_ip(forms.Form):
	host = forms.CharField(max_length=30)
	ip   = forms.CharField(max_length=40)

def serverlist(req):
	username = req.session.get('username')
	if username:
		if req.method == 'POST':
			input_hostinfo = host_ip(req.POST)
			if  input_hostinfo.is_valid():
				host = input_hostinfo.cleaned_data['host']
				ip   = input_hostinfo.cleaned_data['ip']
				serverlist = server_list()
				serverlist.host = host
				serverlist.ip   = ip
				serverlist.save()
				print input_hostinfo.cleaned_data
				return HttpResponseRedirect('/info/serverlist/$')
			else:
				hosts = server_list.objects.all()
				count = server_list.objects.count()
		else:
	  	 input_hostinfo = host_ip()	
	   	hosts = server_list.objects.all()
	   	#iplist  = [i.ip for i in hosts]
	   	#hostlist = [i.host for i in hosts] + [i.ip for i in hosts]
	   	#hostslist = hostlist + iplist
	   	count = server_list.objects.count() 
		return render_to_response('serverlist.html',{'username':username,'input_hostinfo':input_hostinfo,'hosts':hosts,'count':count})
	else:
		return HttpResponse('Login,Plase')

