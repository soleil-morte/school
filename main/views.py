from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def Index(request):
    if request.method == 'POST':
        r = request.POST
        f_name = r['f_name']
        l_name = r['l_name']
        age = r['age']
        subject = r['subject']
        group = r['group']
        payment = 'payment' in request.POST
        student=Student.objects.create(f_name=f_name, l_name=l_name, age=age, payment=payment)

        student.subject.add(r['subject'])
        student.group.add(r['group'])
        return redirect('/index/')

    context = {
        'student':Student.objects.all(),
        'group':Group.objects.all(),
        'subject':Subject.objects.all(),
    }
    
    return render(request, 'index.html', context)


def Teachers(request):
    context = {
        'teacher':Teacher.objects.all(),
    }

    return render(request, 'teachers.html', context)


def Groups(request):
    context = {
        'group':Group.objects.all(),
    }

    return render(request, 'groups.html', context)


def Subjects(request):
    context = {
        'subject':Subject.objects.all(),
    }

    return render(request, 'subjects.html', context)