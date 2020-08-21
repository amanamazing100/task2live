from django.forms import ModelForm
from .models import Student

class CreateStudentForm(ModelForm):
	class Meta:
		model = Student
		fields = [
		'name', 'roll', 'dept'
		]