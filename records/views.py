from django.shortcuts import render
from django.views.generic import View, FormView
from . import models, forms
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
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
            'queryform' : queryForm,
            'checkbox_form' : forms.CheckBoxForm(),
            'students' : students,
            'fields' : [field.name for field in models.Student._meta.get_fields()]
        }
        return render(request, self.template_name, context)


    def post(self, request):
        context={}
        if request.method=='POST':
            queryForm=forms.QueryForm(request.POST)
            checkBoxForm=forms.CheckBoxForm(request.POST)
            if queryForm.is_valid():
                context.append(query(queryForm))
            if checkBoxForm.is_valid():
                context.append(checkbox(checkBoxForm))
                return render(request, self.template_name, context)

def query(form):
    fields=[field.name for field in models.Student._meta.get_fields()]
    name=form.cleaned_data['name']
    print(form.cleaned_data['check_name'])
    for field in form:
        print(field)
    return {
        'students' : models.Student.objects.filter(name=name),
        'fields' : fields,
        'query_form' : form
    }

def checkbox(form):
    for field in form:
        print(form.cleaned_data[field])
    return {
        'checkbox_form': form
    }