from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Student(models.Model):
	#user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
	CHOICES=(
		('CSE', 'cse'),
		('Civil', 'civil'),
		('Mechanical', 'mech'),
		('Production', 'prod'),
		('Metallurgy', 'meta'),
		('EEE', 'eee'),
		('ECE', 'ece')
	)

	name = models.CharField(max_length=30, null=True)
	roll = models.CharField(max_length=9, primary_key=True)
	dept = models.CharField(max_length=10, null=True, choices=CHOICES)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('update', kwargs={'id': self.id})

	def get_ab_url(self):
		return reverse('delete', kwargs={'id': self.id})
