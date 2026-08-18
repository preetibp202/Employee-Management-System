from operator import add

from django.contrib import admin

from Employee import models
from emp.models import Employee, Testimonals

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Emp_Id', 'Email','Phone', 'Address', 'Working', 'Department')
    list_editable=('Email', 'Phone', 'Address', 'Working', 'Department')

class TestimonalsAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Testimonial', 'picture', 'rating')
    list_editable=('Testimonial', 'picture', 'rating')

# Register your models here.
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Testimonals,TestimonalsAdmin)