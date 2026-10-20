# 🚘 DriveEase — Car Rental Management System

A web-based car rental management application built with **Python, Flask, MySQL, and Bootstrap 5**. DriveEase provides a simple interface for browsing vehicles, selecting rental dates, and making reservations with database-backed booking validation.

## ✨ Features

- 🚗 **Vehicle Listings** — Browse available vehicles, categories, and daily rental rates.
- 📅 **Date-Based Booking** — Select pickup and return dates.
- 🔒 **Booking Conflict Validation** — Check for overlapping confirmed bookings before creating a reservation.
- 👤 **Customer Records** — Store customer names, email addresses, and phone numbers.
- 💰 **Automatic Cost Calculation** — Calculate rental costs based on the selected rental period.
- 🗄️ **Relational Database** — Store vehicles, customers, and bookings in MySQL.
- 🔐 **Environment Configuration** — Load database credentials from environment variables.
- 📱 **Responsive Interface** — Use Bootstrap 5 for a clean, mobile-friendly layout.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Flask | Web framework |
| MySQL 8.0+ | Relational database |
| MySQL Connector/Python | Database connectivity |
| Bootstrap 5 | Responsive UI |
| HTML5 & CSS3 | Page structure and styling |
| python-dotenv | Environment configuration |

## 📂 Project Structure

```text
Car-Rental-Management-System/
├── app.py
├── database.sql
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## ⚙️ Prerequisites

- Python 3.10 or later
- MySQL Server 8.0.16 or later
- pip
- A modern web browser

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/amoltathesoftwareengineer/Car-Rental-Management-System.git
cd Car-Rental-Management-System
```

### 2. Create and activate a virtual environment

For Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Create the database

Open MySQL and run the SQL script in `database.sql`.

Alternatively, from the MySQL command-line client:

```sql
SOURCE path/to/database.sql;
```

Replace `path/to/database.sql` with the actual path to the file.

The script creates the `car_rental_db` database, its three tables, and sample vehicle records.

### 5. Configure environment variables

Create a `.env` file in the project root using `.env.example` as a template:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=car_rental_db
FLASK_DEBUG=false
```

Replace `your_mysql_password` with your local MySQL password. If the account has no password, leave the value empty.

**Security:** Never commit `.env` or publish database credentials. The `.gitignore` file should exclude `.env`.

### 6. Start the application

```bash
python app.py
```

Open the following URL in your browser:

**http://127.0.0.1:5000**

## 🚗 Sample Vehicles

The database script inserts the following vehicles:

| Vehicle | Category | Daily Rate |
|---|---|---:|
| Hyundai i20 | Hatchback | ₹1,800.00 |
| Honda City | Sedan | ₹2,500.00 |
| Mahindra XUV700 | SUV | ₹4,000.00 |

## 🗄️ Database Design

The application uses three relational tables:

- **`vehicles`** — Vehicle name, category, daily rate, and availability.
- **`customers`** — Customer name, unique email address, and phone number.
- **`bookings`** — Customer and vehicle references, rental dates, total amount, booking status, and creation timestamp.

Foreign keys maintain relationships between customers, vehicles, and bookings. Database constraints validate rental dates and positive monetary values.

## 🧪 How to Test

1. Start the Flask application.
2. Open the home page.
3. Select a vehicle.
4. Enter customer details.
5. Choose pickup and return dates.
6. Submit the booking.
7. Verify that the booking is stored in MySQL.

A successful submission displays a booking confirmation message.

## 🔮 Future Enhancements

- Admin dashboard for managing vehicles and reservations
- Booking history and cancellation
- User authentication and role-based authorization
- Payment gateway integration
- Vehicle search and category filtering
- Automated unit and integration tests
- Deployment to a cloud hosting platform

## 👨‍💻 Author

**Amol Tathe**

- GitHub: [@amoltathesoftwareengineer](https://github.com/amoltathesoftwareengineer)
- LinkedIn: [Amol Tathe](https://www.linkedin.com/in/amoltathesoftwareengineer/)

## 📄 License

This project is currently provided for portfolio and educational purposes. No open-source license has been added yet.

If you intend to permit others to use, modify, and redistribute this software, choose an appropriate open-source license and add a `LICENSE` file to the repository.

## 🙌 Acknowledgements

Built as a portfolio project to demonstrate Python web development, relational database design, SQL fundamentals, and booking workflow implementation.

---

**DriveEase — Making car rental booking simple.**
