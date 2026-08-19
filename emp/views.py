from django.http import HttpResponse, request
from django.shortcuts import redirect, render

from emp.froms import FeedbackForm,EmployeeForm
from .models import Employee, Testimonals


def emp_home(request):
    emps = Employee.objects.all()

    return render(request, "home.html", {"emps": emps})


def add_emp(request):
    if request.method == "POST":

        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_email = request.POST.get("emp_email")
        emp_department = request.POST.get("emp_department")
        emp_address = request.POST.get("emp_address")
        emp_phone = request.POST.get("emp_phone")
        emp_Working = request.POST.get("emp_Working")

        e = Employee()

        e.Name = emp_name
        e.Emp_Id = emp_id
        e.Email = emp_email
        e.Department = emp_department
        e.Address = emp_address
        e.Phone = emp_phone

        if emp_Working is None:
            e.Working = False
        else:
            e.Working = True

        e.save()

        return redirect("/home/")
    form = EmployeeForm()
    return render(request, "add_emp.html", {"form": form})

def delete_emp(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect("/home/")

def update_emp(request, id):
    emp = Employee.objects.get(id=id)

    if request.method == "POST":
        emp.Name = request.POST.get("emp_name")
        emp.Emp_Id = request.POST.get("emp_id")
        emp.Email = request.POST.get("emp_email")
        emp.Department = request.POST.get("emp_department")
        emp.Address = request.POST.get("emp_address")
        emp.Phone = request.POST.get("emp_phone")

        emp_Working = request.POST.get("emp_Working")

        if emp_Working is None:
            emp.Working = False
        else:
            emp.Working = True

        emp.save()

        return redirect("/home/")

    return render(request, "update_emp.html", {"emp": emp})




def Testimonials(request):
    testimonials = Testimonals.objects.all()
    return render(request, "testimonials.html", {"testimonials": testimonials})
    
def Feedback(request):
    if request.method == "POST":
            form = FeedbackForm(request.POST)
            if form.is_valid():
               print(form.cleaned_data['email'])
               print(form.cleaned_data['name'])
               print(form.cleaned_data['feedback'])
               print("feedback_success") 
               return redirect("/home/")

            
            else:
                 return render(request, "feedback.html", {"form": form}) # Redirect to a success page
    else:
        form=FeedbackForm()

        # Process the feedback data (e.g., save to database, send email, etc.)
        # You can implement your logic here
 # Redirect to a success page or the same page
    return render(request, "feedback.html",{"form": form})






