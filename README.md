# HostelConnect---Hostel-management-system-using-python-Django
HostelConnect is a modern, web-based hostel management system developed using Django and Bootstrap. It simplifies hostel operations by digitizing student data, rent management, and visitor communication, while offering a clean, responsive UI suitable for mobile and desktop use.

The system is designed to manage student accommodation effectively, providing a reliable interface for both administrators and hostel residents. Visitors can explore facilities and submit contact inquiries, while students can log in to manage complaints and view personal details.

💡 The UI design and Bootstrap styling were implemented with the help of ChatGPT, which also provided assistance throughout the development process for code optimization, debugging, and mobile responsiveness.

**Note: ** This repository contains only the HTML template files used for the frontend design of the Hostel Management System. Backend files such as Python views, models, and Django configurations are not included in this public repository for code privacy and security reasons.

**🎯 Objective**

The goal of this project is to simplify hostel operations such as room inquiry, student registration, rent management, and complaints, by digitizing them into a centralized platform that is mobile-friendly and easy to use.


**🔧 Key Features**

**🌐 For Visitors**

  - Explore hostel images and facilities

  - Contact form for booking-related inquiries

  - View location using embedded Google Maps

  - List of all amenities (Wi-Fi, meals, inverter, washing machine, etc.)


- Home Page - 

<img width="1365" height="688" alt="Screenshot 2025-08-06 174748" src="https://github.com/user-attachments/assets/e6d85a76-9297-4fc2-a4ca-6ed751517ddf" />

<img width="1364" height="686" alt="Screenshot 2025-08-06 174828" src="https://github.com/user-attachments/assets/051bd61c-b3c5-4b51-9c3b-7bdd35a73491" />


- Services Page - 

<img width="1365" height="686" alt="Screenshot 2025-08-06 174914" src="https://github.com/user-attachments/assets/fd4ed27c-8054-45a8-9945-33385613faec" />


**👨‍🎓 For Students**

  - Secure login system

  - View personal profile and facilities

  - Submit complaints or feedback

  - See complaints responses given by admin

  - Stay informed about hostel services


- Student login -
  <img width="1364" height="685" alt="Screenshot 2025-08-06 174939" src="https://github.com/user-attachments/assets/6b7531a8-4285-47d3-b479-fee0d6bac32f" />

- Student dashboard -
  <img width="1365" height="682" alt="Screenshot 2025-08-06 175001" src="https://github.com/user-attachments/assets/3cedaf68-be83-4f44-9464-1664f4ce59d1" />
  <img width="1365" height="684" alt="Screenshot 2025-08-06 175022" src="https://github.com/user-attachments/assets/b9f0ccd2-0e67-4879-8cfb-275714ac66d8" />
  <img width="1365" height="682" alt="Screenshot 2025-08-06 175052" src="https://github.com/user-attachments/assets/2a2f3289-8f37-4dd9-bef1-81f1b12ace30" />


**🧑‍💼 For Admin**

  - View and manage student data

  - Track and manage rent payments

  - Receive and respond to complaints

  - Access contact inquiries from visitors

  - <img width="1365" height="677" alt="Screenshot 2025-08-06 175931" src="https://github.com/user-attachments/assets/d94c8562-33fb-4537-ae8a-ae3167927fe5" />




**📱 Frontend**

  - Built with Bootstrap 5 for responsive design

  - Clean, attractive, and optimized UI

  - Image carousel, icons, and feature cards for a modern look


**🛠️ Backend**

  - Built using Django (Python)

  - Uses SQLite database (can be upgraded to PostgreSQL)

  - Models for Students, Complaints, Rent, and Contacts

  - Admin panel for complete control


**🛡️ Security**

  - CSRF protection on all forms

  - Only authenticated users (students/admin) can access protected data


**⚠️ Drawbacks / Limitations**

  - No Online Payment Integration
        Rent payments are not handled online; it only stores data manually.

  - No Automated Email Alerts
        No system for auto-sending email notifications for rent due, complaint status, etc.

  - Lacks Role-based Authorization
        All admin users have the same privileges; no granular roles like warden, accountant, etc.

  - No Room Allotment System
        Students aren’t assigned specific rooms through the system.

  - Single Admin Model
        No support for multi-admin handling or hostel branches.

  - Basic Complaint Management
        Complaints can be submitted but not marked as “Resolved” with status tracking.


**👤 User Roles**

Visitor: Contact form for booking inquiry

Student: Login to access profile & complaint box

Admin: Manages all operations via dashboard

🔮 Future Updates (Planned)
✅ Online Payment Gateway
Allow students to pay rent using Razorpay/Paytm and auto-update rent status.

✅ Student Registration Flow
Add a student self-registration form with admin approval.

✅ Room Allotment & Availability
Enable real-time room allocation and view of available beds.

✅ Notification System
Email/SMS alerts for payment reminders, complaint replies, etc.

✅ Admin Roles
Create separate dashboards/privileges for different hostel staff (warden, accountant, etc.)

✅ Search & Filter in Admin Panel
Add ability to search/filter students by name, room, status, etc.

✅ Data Backup/Export
Feature for admins to download all data in Excel or CSV format.



**Developer Info:**

Created by Ayush
GitHub: github.com/AyushGaikwad84
Email: ayushsgaikwad8480@gmail.com

**Note:**

This project was made for learning purposes only. It includes basic functionality and can be further enhanced for production use.
