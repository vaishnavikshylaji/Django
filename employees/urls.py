from django.urls import path
from employees import views

app_name = 'employees'

urlpatterns = [
    path('', views.EmployeeManagementClass.index, name='index'),
    path('employees/create/', views.EmployeeManagementClass.create, name='create'),
    path('store/', views.EmployeeManagementClass.store, name='store'),
    path('<int:id>/edit/', views.EmployeeManagementClass.edit, name="edit"),
    path('<int:id>/update/', views.EmployeeManagementClass.update, name="update"),
    path('<int:id>/delete/', views.EmployeeManagementClass.delete, name='delete'),

    path('designations/', views.DesignationManagementClass.index, name='designations'),
    path('designations/create/', views.DesignationManagementClass.create, name='designation_create'),
    path('designations/store/', views.DesignationManagementClass.store, name='designation_store'),
    path('designations/<int:id>/edit/', views.DesignationManagementClass.edit, name='designation_edit'),
    path('designations/<int:id>/update/', views.DesignationManagementClass.update, name='designation_update'),
    path('designations/<int:id>/delete/', views.DesignationManagementClass.delete, name='designation_delete'),
]