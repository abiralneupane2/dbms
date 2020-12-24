from django import forms
from django.forms import ModelForm
from . import models
#from address.forms import AddressField

def universityTuple():
    context=[
    ]
    context.append(('','All'))
    universitys = models.University.objects.all()
    for university in universitys:
        context.append((university.name, university.name))
    return context

FACULTY=models.FACULTY
FACULTY.insert(0,('','All'))

COUNTRY=models.COUNTRY
COUNTRY.insert(0,('','All'))

class StudentForm(ModelForm):

    class Meta:
        model = models.Student
        fields = '__all__'

class QueryForm(forms.Form):
    id = forms.IntegerField(label='id', required=False)
    name = forms.CharField(label='Full Name', required=False, max_length=100, widget=forms.TextInput)
    year_enrolled = forms.IntegerField(label='Year Enrolled', required=False)
    bachelor_degree = forms.MultipleChoiceField(label='Bachelor Degree', required=False, choices=FACULTY)
    university = forms.MultipleChoiceField(label='University', required=False, choices=universityTuple())
    current_address = forms.MultipleChoiceField(label='Lives in', required=False, choices=COUNTRY)


