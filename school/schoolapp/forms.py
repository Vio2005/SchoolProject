from django import forms
from .models import *




class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'fee', 'photo', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter course name'}),
            'fee': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter fee'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter description'}),
        }

class TeacherModelForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'course', 'photo', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter teacher name'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter course'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter description'}),
        }



class TeacherModelForm1(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'course', 'photo', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '{{i.name}}'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '{{i.course}}'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': '{{i.description}}'}),
        }

