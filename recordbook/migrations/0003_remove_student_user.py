# Generated by Django 3.1 on 2020-08-20 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recordbook', '0002_student_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
    ]
