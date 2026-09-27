# 🏨 Hotel Reservation System

<p align="center">
  <strong>A modern Django-based hotel reservation platform</strong>
</p>

<p align="center">
  Room Reservation • Food Management • Phone Verification • Jalali Calendar • Custom Admin
</p>

<p align="center">
  <a href="https://github.com/MohammadAminJorian/hotel_reserve">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github" alt="GitHub">
  </a>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django-Framework-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
</p>

---

## 🌟 About The Project

**Hotel Reservation System** is a web application built with **Python and Django** for managing hotel room reservations and related services.

The project focuses on implementing real-world reservation logic, including reservation date calculations, food quantity management, reservation conflict validation, phone verification, and a customized Persian administration panel.

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🛏️ Reservation

* Room reservation
* Reservation date management
* Automatic reservation day calculation
* Reservation conflict detection
* Custom reservation validation

</td>

<td width="50%">

### 🍽️ Food Management

* Food management for reservations
* Automatic food quantity calculation
* Connecting food orders to reservations

</td>
</tr>

<tr>
<td width="50%">

### 👤 User Management

* Phone number verification
* User management
* Reservation management

</td>

<td width="50%">

### 🇮🇷 Persian Support

* Persian admin panel
* Jalali calendar
* Persian-friendly date handling
* RTL-oriented interface

</td>
</tr>
</table>

---

## 🛠️ Tech Stack

<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">

<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white">

<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white">

<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white">

<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">

</p>

---

# 📸 Screenshots

## 🏨 Hotel Reservation

<p align="center">
  <img src="img.png" width="90%" alt="Hotel Reservation">
</p>

---

## 🛏️ Reservation Management

<p align="center">
  <img src="img_2.png" width="90%" alt="Reservation Management">
</p>

---

## 🍽️ Food Reservation

<p align="center">
  <img src="img_3.png" width="90%" alt="Food Reservation">
</p>

---

## 🛠️ Admin Panel

<p align="center">
  <img src="img_4.png" width="90%" alt="Admin Panel">
</p>

---

# 🚀 Getting Started

Follow the steps below to run the project locally.

### 1️⃣ Clone the repository

```bash
git clone https://github.com/MohammadAminJorian/hotel_reserve.git
cd hotel_reserve
```

### 2️⃣ Create a virtual environment

```bash
python -m venv env
```

### 3️⃣ Activate the environment

**Windows**

```bash
env\Scripts\activate
```

**Linux / macOS**

```bash
source env/bin/activate
```

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Apply migrations

```bash
python manage.py migrate
```

### 6️⃣ Create an admin user

```bash
python manage.py createsuperuser
```

### 7️⃣ Run the server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

---

# ⚙️ Project Structure

```text
hotel_reserve/
│
├── hotel_reserve/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── ...
│
├── manage.py
├── requirements.txt
├── README.md
│
├── img.png
├── img_2.png
├── img_3.png
└── img_4.png
```

---

# 🧠 What I Implemented

This project includes custom business logic rather than being only a basic Django CRUD application.

### 📅 Reservation Logic

The system handles:

* Reservation duration
* Reservation date calculations
* Available dates
* Invalid reservation dates
* Reservation conflicts

### 🍽️ Food Calculation

Food quantities are calculated based on reservation information and the number of reservation days.

### 📱 Phone Verification

A phone verification flow is included to validate users during the application workflow.

### 🇮🇷 Persian Administration

The administration experience has been customized for Persian-speaking users, including Jalali date support.

---

# 🔮 Future Improvements

Possible future improvements include:

* 💳 Online payment integration
* 📧 Email notifications
* 📱 SMS notifications
* 🏨 Advanced room availability
* 📊 Reservation analytics dashboard
* 👥 Role-based access control
* 🐳 Docker deployment
* ☁️ Production deployment

---

# 👨‍💻 Developer

<p align="center">

<strong>Mohammad Amin Jorian</strong>

<br><br>

<a href="https://github.com/MohammadAminJorian">
  <img src="https://img.shields.io/badge/GitHub-MohammadAminJorian-181717?style=for-the-badge&logo=github" alt="GitHub">
</a>

<a href="https://mohammadaminjorian.github.io/Portfolio/">
  <img src="https://img.shields.io/badge/Portfolio-Visit%20My%20Portfolio-0A66C2?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Portfolio">
</a>

</p>

---

## ⭐ Support

If you found this project interesting, consider giving it a ⭐ on GitHub.

---

<p align="center">
  Made with ❤️ using Python & Django
</p>
