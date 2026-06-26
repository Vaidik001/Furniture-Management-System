# 🪑 Furniture Management System (Django)

A backend-focused Furniture Management System built using **Python, Django, and SQLite**. This project demonstrates structured database design, role-based access control, and clean backend architecture for managing furniture inventory and transactions.

---

## 🚀 Tech Stack

* Python
* Django
* SQLite (Database)
* Django Admin Panel


---

## 📌 Project Overview

This system is designed to manage furniture-related operations with proper role separation and structured relational data models. It supports different user roles and categorizes furniture into multiple types for better tracking and workflow management.

---

## 👥 User Roles

* 🧑‍💼 **Seller**
* 🛒 **Buyer**
* 🏠 **Rental User**

Each role has:

* Profile management
* Contact details
* Role-based access control

---

## 🪑 Furniture Categories

* 🆕 New Furniture
* 🪵 Old Furniture
* 🔄 Rental Furniture

Each category follows a different workflow for handling and tracking items.

---

## ⚙️ Key Features

* 🔐 Role-based authentication system
* 🧾 User profile and contact management
* 📦 Furniture listing and categorization
* 🔗 Strong relational database models
* 🛠️ Admin dashboard for full control
* 📊 Transaction tracking system
* 🧩 Clean and scalable backend architecture

---

## 🗄️ Database Design

* Structured relational models using Django ORM
* Foreign key relationships between users, roles, and furniture
* Ensures data integrity and consistency
* Optimized for scalability

---

## 🛠️ Admin Panel Features

* Manage users (Seller, Buyer, Rental)
* Add / update / delete furniture items
* Monitor transaction history
* Full backend control system

---

## 📂 Project Setup

### 1. Clone the repository

```bash
git clone https://github.com/Vaidik001/Furniture-Management-System.git
cd Furniture-Management-System
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate environment

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Start server

```bash
python manage.py runserver
```

---

## 📸 Screenshots (Optional)

Add project screenshots here:

* Home Page
* Admin Panel
* Furniture Listing Page
* User Dashboard

---

## 🎯 Future Improvements

* REST API integration
* Payment system for rentals
* Advanced search and filtering
* UI frontend improvement
* Deployment on cloud (Render / AWS)

---

## 👨‍💻 Author

**Vaidik Patel**
Django Developer | Backend Enthusiast

---

## ⭐ Show Your Support

If you like this project:

* Give ⭐ on GitHub
* Fork the repository
* Share with others
