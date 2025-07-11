from django.shortcuts import render,redirect
from .models import *
from django.shortcuts import get_object_or_404, redirect
from django.http import Http404
from .forms import *
import pandas as pd
from django.http import HttpResponse
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
    if request.method == 'POST':
        r = request.POST
        full_name = r['full_name']
        age = r['age']
        subject = r['subject']
        experiance = r['experiance']
        Teacher.objects.create(full_name=full_name, age=age, experiance=experiance, subject_id=subject)

        # student.subject.add(r['subject'])
        return redirect('/teachers/')

    context = {
        'teacher':Teacher.objects.all(),
        'subject':Subject.objects.all(),
    }

    return render(request, 'teachers.html', context)


def Groups(request):
    if request.method == 'POST':
        r = request.POST
        name = r['name']
        subject = r['subject']
        teacher = r['teacher']
        Group.objects.create(name=name, teacher_id=teacher, subject_id=subject)

        return redirect('/groups/')

    context = {
        'group':Group.objects.all(),
        'subject':Subject.objects.all(),
        'teacher':Teacher.objects.all(),
    }

    return render(request, 'groups.html', context)


def Subjects(request):
    # if request.method == 'POST':
    #     r = request.POST
    #     name = r['name']
    #     Subject.objects.create(name=name,)

    #     # student.subject.add(r['subject'])
    #     return redirect('/subjects/')
    if request.method == 'POST':
        form = Subjectsform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/subjects/')
    else:
        form = Subjectsform()

    context = {
        'form':form,
        'subject':Subject.objects.all()
    }

    return render(request, 'subjects.html', context)


def delete_object(request, model_name, id):
    # Словарь, связывающий названия моделей с их классами
    model_mapping = {
        'student': Student,
        'teacher': Teacher,
        'subject': Subject,
        'group': Group,
    }
    
    # Получаем модель по имени
    model = model_mapping.get(model_name.lower())
    if not model:
        raise Http404("Модель не найдена")
    
    # Находим объект или возвращаем 404
    obj = get_object_or_404(model, id=id)
    obj.delete()
    
    return redirect(request.META.get('HTTP_REFERER', '/index/'))


def export_students_exel(request):

    students = Student.objects.all().values('f_name', 'l_name', 'age', 'group', 'subject', 'payment')

    df = pd.DataFrame(students)

    response = HttpResponse(content_type='application/vdn.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=students.xlsx'

    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Students')

    return response