from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
import csv
from .models import Complaint, Contact, Student, RentPaymentHistory

@login_required(login_url='login')
def student_dashboard(request):
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        messages.error(request, "Session expired or profile missing. Please login again.")
        logout(request)
        return redirect('login')

    return render(request, 'student_dashboard.html', {'student': student})

# Create your views here.

#  for csv files
# def export_stud_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'

    writer = csv.writer(response)
    
    # Write header row
    writer.writerow(['Name', 'Room No', 'Mobile', 'Email', 'Gender', 'Address', 'Join Date'])

    # Write data rows
    students = Student.objects.all()
    for student in students:
        writer.writerow([student.name, student.room_no, student.phone, student.email, student.gender, student.address, student.join_date])

    return response


def landing(request):
    return render(request, "landing_page.html")

def home(request):
    return render(request, "index.html")

def rent(request):
    return render(request, "room&facilities.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        num = request.POST.get("number")
        mail = request.POST.get("email")
        msg = request.POST.get("msg")

        Contact.objects.create(
            name=name,
            mobile_number=num,
            visitor_email=mail,
            msg=msg
        )
        messages.success(request, "Thanks for Contacting us. We'll be in touch soon.")
        return redirect("contact")
    return render(request, "contact.html")

def student_login(request):
    if request.user.is_authenticated:
        return redirect('student_dashboard')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user) # Logs the user in (creates session)
            messages.success(request, "Login Successful!")
            return redirect("student_dashboard")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "student_login.html")  # if request is GET it shows login form again.

def student_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')

def student_profile(request):
    # student = get_object_or_404(Student, user=request.user)
    # student_rent = get_object_or_404(RentPaymentHistory, student=student)

    # return render(request, "student_profile.html", {'student': student})
    try:
        student = Student.objects.get(user=request.user)
        return render(request, "student_profile.html", {'student': student})
    except Student.DoesNotExist:
        messages.error(request, "Session expired or profile missing. Please login again.")
        logout(request)
        return redirect('login')

    return render(request, 'student_dashboard.html', {'student': student})

# def rent_history(request):
#     student_rent = get_object_or_404(RentPaymentHistory, use=request.user)
#     return render(request, "")

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)  # Prevent logout after password change
            messages.success(request, "Your password was successfully updated.")
            return redirect('student_dashboard')
        else:
            messages.error(request, "Sorry, there is an error.")
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'change_password.html', {'form': form})

@login_required(login_url='login')
def rent_status(request):
    try:
        rent = Student.objects.get(user=request.user)
        rent_history = RentPaymentHistory.objects.filter(student=rent).order_by('-date_paid')

        amount_payable = None
        latest_rent = rent_history.first()  # get most recent rent record

        if latest_rent:
            if latest_rent.remaining_amount > 0:
                amount_payable = latest_rent.remaining_amount
            else:
                amount_payable = 0

    except Student.DoesNotExist:
        messages.error(request, "Student profile not found. Login again. If problem persists Please contact admin.")
        return redirect('student_dashboard')

    rent_s = "Paid" if rent.rent_status else "Not paid"
    return render(request, "rent_status.html", {
        'rent': rent,
        'rent_s': rent_s,
        'rent_history': rent_history,
        'amount_payable': amount_payable,
        'latest_rent': latest_rent
    })

@login_required(login_url='login')
def room_info(request):
    return render(request, "room_info.html")

def complaint(request):
    if request.method == "POST":
        sub = request.POST.get("sub")
        msg = request.POST.get("msg")

        student = get_object_or_404(Student, user=request.user)

        Complaint.objects.create(
            student=student,
            subject = sub,
            msg = msg,
        )

        messages.success(request, "Your Complaint has been raised.")
        return redirect("student_dashboard")
    return render(request, "complaint.html")

@login_required(login_url='login')
def complaint_history(request):
    student = get_object_or_404(Student, user=request.user)
    complaints = Complaint.objects.filter(student=student).order_by('-date')
    return render(request, 'complaint_history.html', {'complaints': complaints})