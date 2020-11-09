from django.shortcuts import render, redirect
from registration_page.forms import EmpModelForm
from registration_page.models import EmpModel
from django.contrib import messages


# Create your views here.
def showallemployees(request):
    allemployees = EmpModel.objects.all()
    return render(request, "index.html", {"allempdata": allemployees})


def Insertemp(request):
    if request.method == "POST":
        if request.POST.get('eid') and request.POST.get('ename') and request.POST.get('email') and request.POST.get(
                'econtact'):
            saveemp = EmpModel()
            saveemp.empid = request.POST.get('eid')
            saveemp.empname = request.POST.get('ename')
            saveemp.email = request.POST.get('email')
            saveemp.phoneno = request.POST.get('econtact')
            saveemp.save()
            # messages.success(request,"Employee "+saveemp.ename+' added successfully..!')
            return redirect('/')
        else:
            return render(request, "Insert.html")
    else:
        return render(request, "Insert.html")


def edit(request, id):
    employee = EmpModel.objects.get(id=id)
    return render(request, "edit.html", {"employee": employee})


def update(request, id):
    employee = EmpModel.objects.get(id=id)
    if request.POST.get('eid') and request.POST.get('ename') and request.POST.get('email') and request.POST.get(
            'econtact'):
        saveemp = EmpModel()
        saveemp.empid = request.POST.get('eid')
        saveemp.empname = request.POST.get('ename')
        saveemp.email = request.POST.get('email')
        saveemp.phoneno = request.POST.get('econtact')
        saveemp.save()
        return redirect('/')
    else:
        return render(request, "edit.html")


def delete(request, id):
    employee = EmpModel.objects.get(id=id)
    employee.delete()
    return redirect('/')
