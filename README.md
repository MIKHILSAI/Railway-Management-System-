# 🚆 Railway Management System

A simple **Railway Management System** implemented in Python that models trains, schedules, passengers, and bookings with persistent storage using JSON files.

The system allows adding trains, schedules, and passengers, booking tickets with seat management, and displaying all details via a command-line interface.

## ✨ Features

* **Persistent Storage**
  Data is stored in JSON files (`trains.json`, `schedules.json`, `passengers.json`, `bookings.json`) and auto-loaded on restart.

* **Booking Logic**
  ✔️ Checks seat availability
  ✔️ Decrements available seats on booking
  ✔️ Automatically assigns seat numbers

* **Interactive Menu (CLI)**
  Add trains, schedules, and passengers, book tickets, and view details through a simple text menu.

* **Data Validation**
  Prevents duplicate entries and invalid references (e.g., booking on non-existent trains).

## 🏗️ Components

### Classes

* **Train** – Represents a train with ID, name, total seats, available seats, and routes.
* **Schedule** – Holds schedule details like IDs, departure/arrival times, and stations.
* **Passenger** – Stores passenger information.
* **Booking** – Contains booking details (passenger ID, train ID, seat number, date).
* **RailwayManagementSystem** – Manages trains, schedules, passengers, and bookings, with data loading/saving and menu operations.

---

## ⚙️ Installation & Setup

### 🔹 Prerequisites

* Python **3.x** installed on your system.

### 🔹 Steps

1. **Fork the Repository**
   Go to the repository: https://github.com/MIKHILSAI/Railway-Management-System-
   Click **Fork** (top-right) to create your own copy in your GitHub account.

2. **Clone the Repository**
   git clone https://github.com/your-username/Railway-Management-System-.git
   
3. **Navigate into the Project Folder**
   cd Railway-Management-System-

4. **Run the Program**
   python "Railway management system.py"

## 🚀 Usage

* Add **Trains**, **Schedules**, and **Passengers** via the menu.
* Use the **Booking option** to reserve tickets.
* Display details for all entities.
* Exit safely from the menu.

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch (`feature/your-feature`)
3. Commit changes (`git commit -m "Add new feature"`)
4. Push to your fork (`git push origin feature/your-feature`)
5. Create a Pull Request

## 📜 License

This project is licensed under the **MIT License** – free to use and modify.
