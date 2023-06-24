from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from employees.forms.DesignationForm import DesignationForm
from employees.forms.EmployeeForm import EmployeeForm
from employees.models import Employee, Designation
from employees.serializers.DesignationSerializer import DesignationSerializer
from employees.serializers.EmployeeSerializer import EmployeeSerializer


class EmployeeManagementClass:
    def index(request):
        args = {}
        employeesData = Employee.objects.order_by('-created_at')
        args['employees'] = employeesData
        return TemplateResponse(request, 'index.html', args)

    def create(request):
        args = {}
        designations = Designation.objects.all()
        args['designations'] = designations
        return render(request, 'create.html', args)

    def store(request):
        if request.method == 'POST':
            print(request.POST)
            form = EmployeeForm(request.POST)
            serializer = EmployeeSerializer(data=request.POST)
            if serializer.is_valid():
                employee = form.save(commit=False)
                designation = Designation.objects.get(id=request.POST.get('designation_id'))
                employee.designation = designation
                employee.save()
                return redirect('employees:index')
            else:
                args = {}
                args['errors'] = serializer.errors
                designations = Designation.objects.all()
                args['designations'] = designations
                return render(request, 'create.html', args)

    def update(request, id):

        employee = Employee.objects.get(id=id)
        if request.method == 'POST':
            form = EmployeeForm(request.POST, instance=employee)
            serializer = EmployeeSerializer(data=request.POST)
            if serializer.is_valid():
                employee = form.save(commit=False)
                designation = Designation.objects.get(id=request.POST.get('designation_id'))
                employee.designation = designation
                employee.save()
                return redirect('employees:index')
            else:
                args = {}
                args['errors'] = serializer.errors
                designations = Designation.objects.all()
                args['designations'] = designations
                return render(request, 'create.html', args)

    def edit(request, id):
        args = {}
        employee = Employee.objects.get(id=id)
        args['employee'] = employee
        designations = Designation.objects.all()
        args['designations'] = designations
        return render(request, 'edit.html', args)

    def delete(request, id):
        employee = Employee.objects.get(id=id)
        employee.delete()
        return JsonResponse({'message': 'Item deleted successfully.'})


class DesignationManagementClass:
    def index(request):
        args = {}
        designationsData = Designation.objects.order_by('-created_at')
        args['designations'] = designationsData
        return TemplateResponse(request, 'designations/index.html', args)

    def create(request):
        return render(request, 'designations/create.html')

    def store(request):
        if request.method == 'POST':
            print(request.POST)
            form = DesignationForm(request.POST)
            serializer = DesignationSerializer(data=request.POST)
            if serializer.is_valid():
                form.save()
                return redirect('employees:designations')
            else:
                args = {}
                args['errors'] = serializer.errors
                return render(request, 'designations/create.html', args)

    def edit(request, id):
        args = {}
        designation = Designation.objects.get(id=id)
        args['designation'] = designation
        return render(request, 'designations/edit.html', args)

    def update(request, id):

        designation = Designation.objects.get(id=id)
        if request.method == 'POST':
            form = DesignationForm(request.POST, instance=designation)
            serializer = DesignationSerializer(data=request.POST)
            if serializer.is_valid():
                form.save()
                return redirect('employees:designations')
            else:
                args = {}
                args['errors'] = serializer.errors
                return render(request, 'designations/create.html', args)

    def delete(request, id):
        designation = Designation.objects.get(id=id)
        designation.delete()
        return JsonResponse({'message': 'Item deleted successfully.'})


