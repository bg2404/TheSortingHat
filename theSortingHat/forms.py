from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('roll_no', 'student_name', 'gender',)


class GetInfoForm(forms.Form):
    roll_no = forms.IntegerField(label='roll_no')