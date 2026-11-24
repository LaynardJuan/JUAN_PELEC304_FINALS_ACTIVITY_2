from django.db import models


class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20)
    address = models.TextField()
    course = models.CharField(max_length=150)
    year_level = models.CharField(max_length=50)
    section = models.CharField(max_length=20)
    guardian_name = models.CharField(max_length=150)
    guardian_phone = models.CharField(max_length=30)
    previous_school = models.CharField(max_length=200)
    enrollment_status = models.CharField(max_length=30, default="Enrolled")

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
