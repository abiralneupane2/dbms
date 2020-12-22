
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.InsertView.as_view(), name='form'),
    path('table/', views.TableView.as_view(), name='main_table'),
]
