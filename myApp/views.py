from django.views.generic import ListView, DetailView
from .models import Course, Lesson, Article, Question, Answer

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
    
    # Passing in additional arguments to the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["course_name"] = self.kwargs['course_name']
        return context
    
class LessonDetailView(DetailView):
    model = Lesson
    template_name = "myApp/lesson_detail_view.html"

    # Done to use str in the url instead of a pk
    def get_object(self):
        course_name = self.kwargs['course_name']
        lesson_name = self.kwargs['lesson_name']
        lesson = Lesson.objects.get(course__course_name=course_name, lesson_name=lesson_name)
        return lesson
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lesson = self.object
        context["lesson_name"] = self.kwargs['lesson_name']
        # lesson.article_set.all() retrieves all the articles related to the current lesson.
        context["articles"] = lesson.article_set.all() # Lesson specific articles
        context["questions"] = lesson.question_set.all()
        return context