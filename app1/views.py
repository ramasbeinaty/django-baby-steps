from django.shortcuts import redirect, render

#importing loading from django template  
from django.template import loader  

from django.http import HttpResponse  
from django.views.decorators.http import require_http_methods
from app1.forms import StudentModelForm, StudentForm, EmployeeForm
from app1.functions.functions import handle_uploaded_file  

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
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfully") 

    else:  
        student = StudentForm()  
        return render(request,"my_form.html",{'form':student})  

def emp_form(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                return redirect('/index')  
            except:  
                pass  

    else:  
        form = EmployeeForm()  
    return render(request,'my_form.html',{'form':form})  

def index(request):  
   template = loader.get_template('index.html') # getting our template  

   name = {  
        'student':'Rama'  
    }  

   return HttpResponse(template.render(name))       # rendering the template in HttpResponse  