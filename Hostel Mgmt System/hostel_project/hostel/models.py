from multiprocessing import Value
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    # A OneToOneField allows only one student per user.  it is like foreign key (object).
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    address = models.TextField()
    room_no = models.CharField(max_length=10)
    rent_price = models.CharField(max_length=10, default="3000")
    rent_status = models.BooleanField(default=False)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} |-| {self.room_no}"
    
class Complaint(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    msg = models.TextField()
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')
    response = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.student.name} |-| {self.subject} |-| {self.date} |-| {self.status}" 

class RentPaymentHistory(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2)
    remaining_amount = models.DecimalField(max_digits=8, decimal_places=2)
    date_paid = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=[('paid', 'paid'), ('unpaid', 'unpaid')])

    def __str__(self):
        return f"{self.student.name} |-| {self.date_paid} |-| {self.status}"
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    mobile_number = models.CharField()
    visitor_email = models.EmailField()
    msg = models.TextField(blank=True, null=True)
    contact_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}  |-|  {self.contact_date}  |-|  {self.visitor_email}  |-|  {self.mobile_number}"

class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    amount_paid = models.DecimalField(max_digits=7, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.month}"
