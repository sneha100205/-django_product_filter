# 🛍️ Django Product Filter App

This is a Django web application that allows users to **dynamically filter products** based on:
- Search keywords (name, category, description)
- Price range (min and max)

It uses Django’s `Q` objects for flexible filtering logic and is backed by a SQLite database.

---

## 📌 Features

- 🔍 **Dynamic Filtering**: Filter products by keyword and price range.
- 🧠 **Smart Search**: Uses Django’s `Q` object to search multiple fields.
- 💾 **Admin Panel**: Easily add or manage products using Django Admin.
- 🖥️ **Clean UI**: User-friendly product listing interface.

---

## 🚀 How to Run the Project

### 1. Clone or download the project folder

Unzip the folder or run:
```bash
git clone <your-repo-url>
cd django_product_filter
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations to set up the database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (admin)

```bash
python manage.py createsuperuser
```

Follow the prompts to set username and password.

### 6. Start the development server

```bash
python manage.py runserver
```

Visit:
- 🏠 `http://127.0.0.1:8000/` → Main product filter page  
- 🔐 `http://127.0.0.1:8000/admin/` → Admin panel (login with superuser)

---

## 📦 Adding Products

### ✅ Via Django Admin:
1. Visit `/admin/`
2. Login using the superuser account
3. Click on **Products**
4. Add products with name, description, category, and price

### ✅ Via Django Shell:
```bash
python manage.py shell
```

```python
from products.models import Product
Product.objects.create(name="iPhone", category="Electronics", description="Smartphone", price=999)
Product.objects.create(name="Shoes", category="Fashion", description="Running shoes", price=120)
Product.objects.create(name="Book", category="Books", description="Learn Django", price=45)
exit()
```

---

## 🧠 Tech Stack

- **Django 5.x**
- **Python 3.13**
- **SQLite**
- **HTML + Bootstrap (optional for styling)**
- **Q objects** for complex queries

---

## 📸 Suggested Screenshots for Submission

1. Homepage showing full product list
2. Filtered results by category or price
3. Admin panel showing added products
4. Add product form in admin panel

---

## 📁 Project Structure

```
django_product_filter/
├── manage.py
├── myshop/
│   ├── settings.py
│   └── ...
├── products/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── products/
│           └── product_list.html
└── db.sqlite3
```

---

## ✅ Author

Developed by Sneha Chatwani
For academic/demo purposes.
