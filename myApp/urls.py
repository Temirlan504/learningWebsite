from django.urls import path
from .views import CourseListView, LessonListView, LessonDetailView

app_name = "myApp"

urlpatterns = [
    path('', CourseListView.as_view(), name="course-list"),
    path('<str:course_name>/', LessonListView.as_view(), name="lesson-list"),
    path('<str:course_name>/<str:lesson_name>/', LessonDetailView.as_view(), name="lesson-detail")
]