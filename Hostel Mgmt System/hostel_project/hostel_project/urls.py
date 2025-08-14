"""
URL configuration for hostel_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hostel import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.landing, name='landing'),
    path('', views.home, name='home'),
    # path('export-students/', views.export_stud_csv, name='export_students'),
    path('rent/', views.rent, name='rent'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.student_login, name='login'),
    path('logout/', views.student_logout, name='logout'),
    path('student_dashboard', views.student_dashboard, name='student_dashboard'),
    path('student_profile', views.student_profile, name='student_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('rent_status/', views.rent_status, name="rent_status"),
    path('room_info/', views.room_info, name='room_info'),
    path('complaint/', views.complaint, name="complaint"),
    path('complaint_history/', views.complaint_history, name="complaint_history"),
]

