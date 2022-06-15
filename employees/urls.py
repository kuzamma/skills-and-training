from .views import  TrainingView, WorkshopView
from django.urls import path
from . import views

from django.urls import path

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.home, name='employees'),
    path('training/', views.TrainingView, name='training'),
    path('vtraining/', views.viewTraining, name='vtraining'),
    path('vworkshop/', views.viewWorkshop, name='vworkshop'),
    path('workshop/', views.WorkshopView, name='workshop'),

    path('create-employee', views.createEmployeee, name="create_employee"),
    path('employee-list', views.employee_list, name="employee_list"),
    path('employee-edit/<int:pid>', views.edit_employee, name="edit_employee"),
    path('delete_employee/<int:pid>', views.delete_employee, name="delete_employee"),
]