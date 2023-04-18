from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name
    
class Lesson(models.Model):
    lesson_name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE) # Lesson can have only one course, but Course can have many lessons

    def __str__(self):
        return self.lesson_name