from django.shortcuts import render
from django.views.generic import View, FormView
from . import models, forms
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db.models import Q
# Create your views here.

def index(request):
    return render(request, 'index.html', {})


class InsertView(FormView):
    template_name = 'form.html'
    form_class = forms.StudentForm
    success_url = 'index/'

    def form_valid(self, form):
        print(form.cleaned_data)
        #form.save()
        return super().form_valid(form)


class TableView(View):
    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(TableView, self).dispatch(request, *args, **kwargs)

    template_name = 'table.html'
    
    

    


    def get(self, request):
        queryForm = forms.QueryForm()
        students = models.Student.objects.all()
        context = {
            'query_form' : queryForm,
            'students' : students,
            'fields' : [field.name for field in models.Student._meta.get_fields()]
        }
        
        return render(request, self.template_name, context)


    def post(self, request):
       
        fields=[field.name for field in models.Student._meta.get_fields()]
        
        if request.method=='POST':
            queryForm=forms.QueryForm(request.POST)
            if queryForm.is_valid():
                context={
                    'query_form':queryForm,
                    'students':query(queryForm),
                    'fields':fields
                }
                return render(request, self.template_name, context)

def query(form):
    filter={}
    flag=1
    multipleFilter={}
    for key, value in form.cleaned_data.items():
        if value:
            if not isinstance(value, list):
                filter[key]=value
                print(filter)
            else:
                multipleFilter[key]=value
    students=list(models.Student.objects.filter(**filter))
    mstudents=students.copy()
    if multipleFilter:


        for student in students:
            for key, value in multipleFilter.items():
                flag=0
                print(key)
                for val in value:
                    if val=='':
                        flag=1
                        break
                    print(val)
                    print(getattr(student, key))
                    if str(getattr(student,key)) == val:
                        flag=1
                        break    
                if flag==0:
                    print("deleted")
                    print(student)
                    mstudents.remove(student)
                    break
                
                
                    
                

    print(mstudents)
    #students=models.Student.objects.filter(**filter)
    # print(filter)
    return mstudents

