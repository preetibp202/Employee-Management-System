from django import forms
from sqlalchemy import label
from .models import Employee
class FeedbackForm(forms.Form):
    name = forms.CharField(label="Enter Your Name", max_length=100, required=True)
    email = forms.EmailField(label="Enter Your Email", required=True)
    feedback = forms.CharField(label=" Enter Your Feedback", widget=forms.Textarea, required=True)




class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'Name',
            'Emp_Id',
            'Email',
            'Department',
            'Address',
            'Phone',
            'Working'
        ]