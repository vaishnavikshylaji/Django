from django import forms

from employees.models import Designation


class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = ['name']
