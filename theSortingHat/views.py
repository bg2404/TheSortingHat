from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.messages import get_messages
from .forms import StudentForm, GetInfoForm
from .models import Student
from random import randint


def home(request):
    
    if request.method == 'POST':
        form = GetInfoForm(request.POST)

        if form.is_valid():
            messages.add_message(request, messages.INFO, str(form.cleaned_data['roll_no']))
            return redirect('theSortingHat:detail')
    
    else:
        form = GetInfoForm()
    return render(request, 'theSortingHat/home.html', {'form': form})

def create_student(request):

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid(): 
            form.save()
            return redirect('theSortingHat:home')
    
    else:
        form = StudentForm()
    return render(request, 'theSortingHat/create_student.html', {'form': form})

def detail(request):
    storage = get_messages(request)
    students = None
    if storage:
        for message in storage:
            roll_no = int(message.message)
            students = Student.objects.filter(roll_no=roll_no)
    else:
        students = Student.objects.all()
    return render(request, 'theSortingHat/detail.html', { 'students': students})

def getHat(hat):
    if hat == 0:
        return 'Griffindor'
    elif hat == 1:
        return 'Hufflepuff'
    elif hat == 2:
        return 'Ravenclaw'
    else:
        return 'Slitherin'


def sort(request):
    total_boys = Student.objects.filter(gender='Male').count() + Student.objects.filter(gender='Others').count()
    total_girls = Student.objects.filter(gender='Female').count()
    boys = [total_boys // 4, total_boys // 4, total_boys // 4, total_boys - 3*(total_boys//4)]
    girls = [total_girls // 4, total_girls // 4, total_girls // 4, total_girls - 3*(total_girls//4)]

    all_students = Student.objects.all()
    for student in all_students:
        gender = student.gender
        while True:
            hat = randint(0,3)
            if gender == 'Male' or gender == 'Others':
                if boys[hat] == 0:
                    continue
                else:
                    student.hat = getHat(hat)
                    boys[hat] = boys[hat] - 1
                    break
            else:
                if girls[hat] == 0:
                    continue
                else:
                    student.hat = getHat(hat)
                    girls[hat] = girls[hat] - 1
                    break
        student.save()

    return redirect('theSortingHat:home')
        