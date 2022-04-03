from django.shortcuts import render

#importing loading from django template  
from django.template import loader  

from django.http import HttpResponse  
from django.views.decorators.http import require_http_methods
from app1.forms import StudentModelForm, StudentForm

import datetime  
  
# Create your views here.  

@require_http_methods(["GET"]) 
def hello(request):  
    return HttpResponse("<h2>Hello, Welcome to Django through Hello route!</h2>")  

def now_time(request):  
    now = datetime.datetime.now()  
    html = "<html><body><h3>Now time is %s.</h3></body></html>" % now  
    return HttpResponse(html)    # rendering the template in HttpResponse

def student_model_form(request):
    student = StudentModelForm()  
    return render(request,"my_form.html",{'form':student})    

def student_form(request):
    student = StudentForm()  
    return render(request,"my_form.html",{'form':student})  

def index(request):  
   template = loader.get_template('index.html') # getting our template  
   name = {  
        'student':'Rama'  
    }  
   return HttpResponse(template.render(name))       # rendering the template in HttpResponse  