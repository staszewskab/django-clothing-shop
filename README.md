# Django Clothing Shop

## Project Overview

The **Django Clothing Shop** is a web-based e-commerce application built with Django and Django REST Framework (DRF).  
It allows users to browse products, manage a shopping cart, place orders, and securely register/login.  
The project demonstrates key web development concepts including user authentication, form validation, dynamic client-side interactions, REST API integration, and responsive UI/UX design.

---

## Features

### Core Functionality

- **Product Management:** Display products with details such as name, image, price, and stock. Staff can add or edit products.  
- **Shopping Cart:** Authenticated users can add products, update quantities, and view total prices.  
- **Order Management:** Users can view their order history, including items and totals.  
- **REST API:** JSON endpoints for products and user-specific orders.  
- **AJAX Integration:** Dynamic actions (e.g., adding items to cart) without full page reload.  
- **Responsive Design:** UI adapts to multiple screen sizes. 
- **Form Validation:** Client-side (JavaScript) and server-side (Django forms) validation ensures data integrity.  
- **Error Handling:** Clear error messages on login, registration.  

### User Management

- **Registration:** Users can create accounts with validated email and password.  
- **Login/Logout:** Secure session management using Django's authentication system.  
- **Password Reset:** One-time password reset mechanism (fake email output for testing).  
- **Access Control:** Cart and orders pages are accessible only to logged-in users.

---

## Installation and Setup

1. **Clone the repository:**

```bash
git clone <repository_url>
cd django-clothing-shop/backend
```

2. **Create and activate a virtual environment (recommended):**
```bash
python -m venv venv
# Windows PowerShell
.\venv\Scripts\Activate.ps1
# macOS / Linux
source venv/bin/activate
```
3. **Install dependencies (from your own environment or manually):**
```bash
pip install django djangorestframework pillow
```
4. **Apply database migrations:**
```bash
python manage.py migrate
```
5. **Create a superuser (for admin access):**
```bash
python manage.py createsuperuser
```
6. **Run the development server:**
```bash
python manage.py runserver
```
7. **Access the application:**

Frontend: http://127.0.0.1:8000/

Admin panel: http://127.0.0.1:8000/admin/