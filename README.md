# 🚀 Jira Lite (Flask Backend)

A lightweight issue tracking system built using Flask, inspired by Jira.
This project demonstrates backend development skills including REST APIs, authentication, and clean architecture.

---

## 📌 Features

* 🔐 User Authentication (JWT)
* 📝 Create, Update, Delete Issues
* 📂 Project-based Issue Management
* 🔍 Filtering & Pagination (if added)
* ⚠️ Proper Error Handling
* 🧱 Clean Code Structure (Blueprints, Services)

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Database:** SQLite / PostgreSQL
* **ORM:** SQLAlchemy
* **Authentication:** Flask-JWT-Extended
* **Others:** Marshmallow (optional validation)

---

## 📁 Project Structure

```
jira_lite/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── utils/
│
├── run.py
├── requirements.txt
├── .gitignore
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```
git clone https://github.com/<your-username>/jira-lite.git
cd jira-lite
```

### 2. Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the app

```
python run.py
```

---

## 🔑 API Endpoints (Sample)

### Auth

* `POST /register`
* `POST /login`

### Issues

* `POST /issue`
* `GET /issues`
* `PUT /issue/<id>`
* `DELETE /issue/<id>`

---

## 🧠 Key Concepts Used

* REST API Design
* JWT Authentication
* Decorators for route protection
* Service Layer Architecture
* Database Relationships

---

## 🚀 Future Improvements

* 👥 User roles (Admin/User)
* 💬 Comments on issues
* 📊 Activity logs
* 🌍 Deployment (Render / AWS)

---

## 🙌 Author

**Rohit Najan**
Software Engineer | Backend Developer

---

## ⭐ Note

This project is built for learning and demonstrating backend development skills.
Open to feedback and improvements!
