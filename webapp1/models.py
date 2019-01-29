from django.db import models

# Create your models here.

class faculty(models.Model):
    faculty_school = models.CharField(max_length=255)
    NoofStudents = models.IntegerField()
    NoofCourses = models.IntegerField()
    NoOfStaffs= models.IntegerField()

    def __str__(self):
        return self.faculty_school
