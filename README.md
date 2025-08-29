# Travel Booking System

A **Django-based Travel Booking Application** that allows users to search, filter, and book travel options (flights, trains, buses, cabs) with seat selection, price calculation, and booking management.

---

## Features
-  **Search & Filter** travel options by type, source, destination, and date  
-  **Booking Management** with seat selection & total price calculation  
-  **Admin Dashboard** to manage users, travel options & bookings  
-  **User Authentication** for secure login/signup  
-  **Dynamic Pricing** updates based on seat availability  

---

## Tech Stack
- **Backend**: Django, Python  
- **Frontend**: HTML, CSS, Bootstrap  
- **Database**: MySQL

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/travel-booking.git
   cd travel-booking
   ```

## Installation & Setup

1. **Create virtual environment & install dependencies**
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

2. **Run migrations**
```bash
python manage.py migrate
```

3. **Start the server**
```bash
python manage.py runserver
```

4. **Open in browser**  
[http://127.0.0.1:8000](http://127.0.0.1:8000)
