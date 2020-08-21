import django_filters
from django_filters import CharFilter
from .models import *

class SearchFilter(django_filters.FilterSet):
	#name = CharFilter(field_name='name', lookup_expr='icontains')
	#roll = CharFilter(field_name='roll', lookup_expr='icontains')
	class Meta:
		model = Student
		fields = '__all__'
		exclude = ['name', 'roll']
