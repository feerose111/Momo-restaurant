# Momo Restaurant Management System

This is a simple web-based application built using Django to manage a Momo restaurant. It provides basic features for managing menu items, orders, and customer information.

---

## Features

- **Menu Management**:
  - Add, edit, and delete menu items.
  - Categorize items based on types (e.g., steamed, fried, etc.).

- **Order Management**:
  - Place and manage customer orders.
  - Track order status (e.g., pending, completed).

- **Customer Management**:
  - Store and retrieve customer information for personalized service.

---

## Requirements

The following dependencies are required for this project:

```
asgiref==3.8.1
Django==5.1.1
python-decouple==3.8
sqlparse==0.5.1
tzdata==2024.2
```

---

## Installation

### Prerequisites

- Python 3.8 or higher installed on your machine.

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/feerose11/Momo-restaurant.git
   ```

2. **Navigate to the Project Directory**
   ```bash
   cd momo-restaurant
   ```

3. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up Environment Variables**
   - Create a `.env` file in the project root with the following:
     ```env
     SECRET_KEY=your-secret-key
     DEBUG=True
     ALLOWED_HOSTS=localhost,127.0.0.1
     ```

6. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

7. **Run the Server**
   ```bash
   python manage.py runserver
   ```

---

## Usage

1. Open your browser and go to `http://127.0.0.1:8000/`.
2. Use the admin panel (`/admin`) to manage menu items, orders, and customer data.

---

## Future Enhancements

- Online ordering system with payment gateway integration.
- Detailed analytics for sales and customer preferences.
- User authentication for staff and customers.

---

## Contribution

Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

---
