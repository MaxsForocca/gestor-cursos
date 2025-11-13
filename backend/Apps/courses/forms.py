from django import forms
from .models import Course, Instructor, Enrollment

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["title", "code", "description", "instructor", "start_date", "end_date"]

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ["student_name", "student_email"]
