from django.views.generic.list import ListView
from .models import Course, Lesson

class CourseListView(ListView):
    model = Course
    template_name = "myApp/index.html"
    context_object_name = "courses"

class LessonListView(ListView):
    model = Lesson
    template_name = "myApp/lesson_view.html"
    context_object_name = "lessons"

    def get_queryset(self):
        course_name = self.kwargs['course_name'] # Get the selected course from the URL parameter
        lessons = Lesson.objects.filter(course__course_name=course_name) # Filter the lessons queryset by the selected course
        return lessons