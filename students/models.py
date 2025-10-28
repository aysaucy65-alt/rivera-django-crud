from django.db import models
from django.urls import reverse

class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    year_level = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])
