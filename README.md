# Car Rental Management System

A web-based application for managing rental vehicles, customer information, reservations, and vehicle return operations.

## Overview

The Car Rental Management System provides a centralized way to manage vehicles, rental bookings, customer records, rental periods, and vehicle availability.

It demonstrates database-driven application development, booking workflows, data validation, and rental management.

## Key Features

- Add, update, and manage vehicle records
- Maintain customer information
- Search vehicles by category and availability
- Create and manage rental bookings
- Validate booking dates
- Track vehicle pickup and return
- Calculate rental charges based on configured rates
- Track booking status
- Generate vehicle and booking reports

## Technology Stack

- Python
- Flask
- MySQL 8.0
- HTML5 and CSS3
- Bootstrap
- Jinja2

## Database Design

Proposed tables:

- `customers`
- `vehicles`
- `bookings`
- `payments`
- `users`

Use foreign keys and suitable constraints to maintain relationships and prevent invalid booking records.

## Project Structure

```text
Car-Rental-Management-System/
├── app.py
├── config.py
├── database.sql
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── templates/
├── static/
└── tests/
```

## Installation

```bash
git clone https://github.com/amoltathesoftwareengineer/Car-Rental-Management-System.git
cd Car-Rental-Management-System
python -m venv .venv
```

Activate on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure MySQL, create the database using `database.sql`, and set the required environment variables.

## Run the Application

```bash
python app.py
```

Open the local development URL shown in the terminal.

## Business Applications

- Vehicle rental operations
- Reservation management
- Fleet availability tracking
- Rental revenue reporting
- Customer booking history

## Security

Use password hashing, parameterized SQL queries, server-side validation, and role-based access controls. Payment processing requires additional security and should not store raw card details.

## Future Enhancements

- Online payment gateway integration
- Booking confirmation notifications
- Vehicle maintenance tracking
- Rental invoice generation
- Interactive availability calendar
- Analytics dashboard

## Author

Amol Tathe

GitHub: https://github.com/amoltathesoftwareengineer

## License

Add an appropriate open-source license before permitting reuse.
