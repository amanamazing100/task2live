from django.shortcuts import render, redirect
from .models import *
from .forms import CreateStudentForm
from .filters import SearchFilter 
# Create your views here.

def createStudent(request):
	form = CreateStudentForm()
	if request.method == 'POST':
		form = CreateStudentForm(request.POST)
		print (request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	context = {
		'form': form,
	}
	return render(request, 'new.html', context)


def homeView(request):
	students = Student.objects.all()
	searchfilter = SearchFilter(request.GET, queryset=students)
	students = searchfilter.qs
	context = {
			'students': students,
			'filter': searchfilter,
	}
	return render(request, 'home.html', context)

def updateStudent(request, id):
	student = Student.objects.get(id=id)
	print(id)
	form = CreateStudentForm(request.POST or None, instance=student)
	print(student.name)
	if form.is_valid():
		form.save()
		return redirect('home')
	context = {
		'form': form,
		'student': student
	}
	return render(request, 'update.html', context)

def deleteStudent(request, id):
	student = Student.objects.get(id=id)
	student.delete()
	return redirect('home')
	context = {
	}
	return render(request, 'home.html', context)
