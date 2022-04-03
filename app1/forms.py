from django import forms  
from app1.models import Student, Employee  

# use the Model form
class StudentModelForm(forms.ModelForm):  
    class Meta:  
        model = Student  
        fields = "__all__"  

# use django form
class StudentForm(forms.Form):  
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length = 100)
    file      = forms.FileField(label="Attach a profile image") # for creating file input  
  
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"  