from django.urls import path
from .views import CourseListView, LessonListView

app_name = "myApp"

urlpatterns = [
    path('', CourseListView.as_view(), name="course-list"),
    path('<slug:course_name>/', LessonListView.as_view(), name="lesson-list")
]