from django import forms
from django.forms import ModelForm
from . import models
#from address.forms import AddressField

def universityTuple():
    context=[
    ]
    universitys = models.University.objects.all()
    for university in universitys:
        context.append((university.name, university.name))
    print(context)
    return context

FACULTY=models.FACULTY
FACULTY.insert(0,('All','All'))

class StudentForm(ModelForm):

    class Meta:
        model = models.Student
        fields = '__all__'

class QueryForm(forms.Form):
    name = forms.CharField(label='Full Name', required=False, max_length=100, widget=forms.TextInput)
    bachelor_degree = forms.MultipleChoiceField(label='Bachelor Degree', required=False, choices=FACULTY)
    university = forms.MultipleChoiceField(label='University', required=False, choices=universityTuple())