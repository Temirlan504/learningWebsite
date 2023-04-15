from django.urls import path
from .views import CourseListView

app_name = "myApp"

urlpatterns = [
    path('', CourseListView.as_view(), name="course-list")
]