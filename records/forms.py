from django import forms
from django.forms import ModelForm
from . import models
#from address.forms import AddressField

class StudentForm(ModelForm):

    class Meta:
        model = models.Student
        fields = '__all__'

class QueryForm(forms.Form):
    name = forms.CharField(label='Full Name', required=False, max_length=100, widget=forms.TextInput(attrs={'id':'name_input'}))

class CheckBoxForm(forms.Form):
    check_name = forms.CharField(label='Permanent Address', widget=forms.CheckboxInput(attrs={'id':'name_checkbox'}), initial=True)
