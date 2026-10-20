import os
from datetime import date
from decimal import Decimal

import mysql.connector
from dotenv import load_dotenv
from flask import Flask, request, redirect, render_template_string

load_dotenv()
app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "car_rental_db")
    )

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>DriveEase | Car Rental</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
rel="stylesheet">
<style>
body{background:#f4f7fb;color:#172033}
.hero{background:#10233f;color:white;padding:40px;border-radius:18px}
.card{border:0;border-radius:15px}
.btn-primary{background:#155eef;border:0}
</style>
</head>
<body>
<div class="container py-4">
<nav class="d-flex justify-content-between mb-4">
<h3>🚘 DriveEase</h3><span>Car Rental Management</span>
</nav>
<div class="hero mb-4">
<h1>Find your next ride.</h1>
<p class="mb-0">Simple, transparent and convenient car rentals.</p>
</div>
{% if message %}
<div class="alert alert-info">{{ message }}</div>
{% endif %}
<h3 class="mb-3">Available Vehicles</h3>
<div class="row g-3">
{% for v in vehicles %}
<div class="col-md-4">
<div class="card p-4 h-100 shadow-sm">
<h4>{{ v.name }}</h4>
<p class="text-secondary">{{ v.category }}</p>
<h5>₹{{ "%.2f"|format(v.daily_rate) }} / day</h5>
<form method="post" action="/book">
<input type="hidden" name="vehicle_id" value="{{ v.id }}">
<input class="form-control mb-2" name="name"
placeholder="Your full name" required maxlength="100">
<input class="form-control mb-2" type="email" name="email"
placeholder="Email address" required maxlength="150">
<input class="form-control mb-2" name="phone"
placeholder="Phone number" required maxlength="20">
<label class="form-label">Pickup date</label>
<input class="form-control mb-2" type="date" name="start_date"
min="{{ today }}" required>
<label class="form-label">Return date</label>
<input class="form-control mb-3" type="date" name="end_date"
min="{{ today }}" required>
<button class="btn btn-primary w-100">Book Vehicle</button>
</form>
</div>
</div>
{% else %}
<p>No vehicles available yet. Add vehicles to the database.</p>
{% endfor %}
</div>
<footer class="text-center text-secondary mt-5">
Car Rental Management System · Built with Flask and MySQL
</footer>
</div>
</body>
</html>
"""

@app.get("/")
def home():
    message = request.args.get("message", "")
    conn = get_db()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("""
            SELECT v.id, v.name, v.category, v.daily_rate
            FROM vehicles v
            WHERE v.available = TRUE
              AND NOT EXISTS (
                SELECT 1 FROM bookings b
                WHERE b.vehicle_id = v.id
                  AND b.status = 'CONFIRMED'
                  AND b.start_date <= %s
                  AND b.end_date >= %s
              )
            ORDER BY v.daily_rate
        """, (date.today(), date.today()))
        vehicles = cur.fetchall()
        return render_template_string(
            PAGE, vehicles=vehicles, today=date.today().isoformat(),
            message=message
        )
    finally:
        conn.close()

@app.post("/book")
def book():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip().lower()
    phone = request.form.get("phone", "").strip()

    try:
        vehicle_id = int(request.form["vehicle_id"])
        start = date.fromisoformat(request.form["start_date"])
        end = date.fromisoformat(request.form["end_date"])
    except (ValueError, KeyError):
        return redirect("/?message=Invalid+booking+details")

    if not name or not email or not phone:
        return redirect("/?message=Please+complete+all+fields")

    if start < date.today() or end < start:
        return redirect("/?message=Please+check+your+booking+dates")

    conn = get_db()
    try:
        conn.start_transaction()
        cur = conn.cursor(dictionary=True)

        cur.execute("""
            SELECT id, daily_rate FROM vehicles
            WHERE id = %s AND available = TRUE
            FOR UPDATE
        """, (vehicle_id,))
        vehicle = cur.fetchone()

        if not vehicle:
            conn.rollback()
            return redirect("/?message=Vehicle+not+available")

        cur.execute("""
            SELECT id FROM bookings
            WHERE vehicle_id = %s AND status = 'CONFIRMED'
              AND start_date <= %s AND end_date >= %s
        """, (vehicle_id, end, start))

        if cur.fetchone():
            conn.rollback()
            return redirect("/?message=Dates+already+booked")

        cur.execute("""
            INSERT INTO customers (name, email, phone)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE
              name = VALUES(name), phone = VALUES(phone)
        """, (name, email, phone))

        cur.execute("SELECT id FROM customers WHERE email = %s", (email,))
        customer_id = cur.fetchone()["id"]

        days = (end - start).days + 1
        total = Decimal(str(vehicle["daily_rate"])) * days

        cur.execute("""
            INSERT INTO bookings
            (customer_id, vehicle_id, start_date, end_date, total_amount)
            VALUES (%s, %s, %s, %s, %s)
        """, (customer_id, vehicle_id, start, end, total))

        conn.commit()
        return redirect("/?message=Booking+confirmed")

    except mysql.connector.Error:
        conn.rollback()
        app.logger.exception("Booking database error")
        return redirect("/?message=Booking+failed.+Please+try+again")
    finally:
        conn.close()

if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG", "false").lower() == "true")
