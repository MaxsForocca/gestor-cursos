from django.contrib import admin
from .models import Course, Instructor, Enrollment

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("code", "title", "instructor", "start_date", "end_date")
    search_fields = ("code", "title")
    list_filter = ("instructor",)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("student_name", "student_email", "course", "enrolled_at")
    search_fields = ("student_name", "student_email", "course__code")
