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

class Article(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    paragraph = models.TextField()
    img = models.ImageField(blank=True, null=True)

class Question(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    question_name = models.CharField(max_length=200)
    explanation = models.TextField()
    img = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.question_name

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)
    answer_name = models.CharField(max_length=100, blank=True)
    img = models.ImageField(blank=True, null=True)
    isCorrect = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_name