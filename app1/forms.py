from django import forms  
from app1.models import Student  

# use the Model form
class StudentModelForm(forms.ModelForm):  
    class Meta:  
        model = Student  
        fields = "__all__"  

# use django form
class StudentForm(forms.Form):  
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length = 100)  