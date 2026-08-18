from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Employee(models.Model):
    Name = models.CharField(max_length=100)
    Emp_Id = models.IntegerField()
    Email = models.EmailField()
    Phone = models.CharField(max_length=10)
    Address = models.CharField(max_length=100)
    Working = models.BooleanField(default=True)
    Department = models.CharField(max_length=100)

class Testimonals(models.Model):
    Name = models.CharField(max_length=100)
    Testimonial = models.TextField()
    picture = models.ImageField(upload_to='media/testimonials/')
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )