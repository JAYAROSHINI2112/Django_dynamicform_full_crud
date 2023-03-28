from django import forms  
from django.forms import modelformset_factory
from employee.models import Employee  


myFormSet = modelformset_factory(
    Employee, fields=("__all__" ), extra=1
)

class my_form(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
        