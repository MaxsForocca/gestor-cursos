from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Course, Instructor, Enrollment
from .forms import CourseForm, EnrollmentForm

class CourseListView(ListView):
    model = Course
    template_name = "courses/course_list.html"
    context_object_name = "courses"

class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/course_detail.html"
    context_object_name = "course"

class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = "courses/course_form.html"

class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = "courses/course_form.html"

class CourseDeleteView(DeleteView):
    model = Course
    template_name = "courses/confirm_delete.html"
    success_url = reverse_lazy("courses:course-list")

# Enrollment example (create enrollment for a course)
from django.shortcuts import get_object_or_404, redirect, render

def enroll(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.course = course
            enrollment.save()
            return redirect(course.get_absolute_url())
    else:
        form = EnrollmentForm()
    return render(request, "courses/enroll_form.html", {"form": form, "course": course})
