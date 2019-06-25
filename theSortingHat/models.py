from django.db import models
from .choices import GENDER_CHOICES, HAT_CHOICES

class Student(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=10, null=False, choices=GENDER_CHOICES)
    hat = models.CharField(max_length=10, blank=True, null=True, choices=HAT_CHOICES)

    def __str__(self):
        return str(self.student_name) + " - Roll No " + str(self.roll_no)
