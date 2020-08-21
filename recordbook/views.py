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
		else:
			context = {
			'form': form,
			}
			return render(request, 'new.html', context)
	context = {
		'form': form,
	}
	return render(request, 'new.html', context)


def homeView(request):
	students = Student.objects.all()
	searchfilter = SearchFilter(request.GET, queryset=students)
	students = searchfilter.qs
	arr1 = []
	#arr2 = []
	for x in students:
		arr1.append(x.name)
		#arr2.append(x.roll)
	print(arr1)
	context = {
			'arr1': arr1,
			#'arr2': arr2,
			'students': students,
			'filter': searchfilter,
	}
	return render(request, 'home.html', context)

def updateStudent(request, roll):
	student = Student.objects.get(roll=id)
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

def deleteStudent(request, roll):
	student = Student.objects.get(roll=id)
	student.delete()
	return redirect('home')
	context = {
	}
	return render(request, 'home.html', context)
