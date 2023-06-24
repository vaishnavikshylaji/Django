from django import forms

from employees.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'designation', 'year_of_experience']

