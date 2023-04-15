from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Course

class CourseListView(ListView):
    model = Course
    template_name = "myApp/index.html"
    context_object_name = "courses"