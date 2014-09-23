from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
from django.shortcuts import render_to_response

'''
def  index(req):
	t = loader.get_template('index.html')
	c = Context({})
	return HttpResponse(t.render(c))
'''

class po():
	def __init__(self,name,age):
		self.name = name
		self.age =age

	def say(self):
		return 'hahahah' + self.name
	

def index(req):
	ip = ['10.100.10.100','100.100.100.10']
	user = {'name':'mk','age':'23'}
	return render_to_response('index.html',{'title':'itmanager','user':user, 'ip':ip})
