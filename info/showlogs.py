from info.models import logpath
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts	import render_to_response
import tail

class projectform(forms.Form):
	project = forms.CharField(max_length=30)

def print_line(txt):
	print txt

def showlog(req):
	sess = req.session.get('username')
	if sess:
		if req.method == 'POST':
			input_project = projectform(req.POST)
                        if input_project.is_valid():
                        	pro = input_project.cleaned_data['project']
                        	logs = 	tail.Tail('/export/itmanager/info/logs/a.txt').register_callback(print_line)
				
				return HttpResponse(logs)
	else:
		return HttpResponseRedirect('/login')
	projects = logpath.objects.all()
	input_project = projectform()
	count = logpath.objects.count()
	return render_to_response('showlogs.html',{'username':sess,'input_project':input_project,'projects':projects,'count':count})
