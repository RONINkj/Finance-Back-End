# Finance Data Processing Backend (FastAPI)

## 📌 Overview

This project is a backend system for a finance dashboard that manages financial transactions, user roles, and analytics.

It demonstrates:

* Clean API design
* Role-Based Access Control (RBAC)
* Data validation
* Aggregation queries for analytics
* Structured backend architecture

---

## 🚀 Tech Stack

* **Backend Framework:** FastAPI
* **Database:** SQLite
* **ORM:** SQLAlchemy
* **Authentication:** JWT (JSON Web Tokens)
* **Validation:** Pydantic

---

## 📁 Project Structure

```
app/
 ├── main.py
 ├── db/
 │    ├── database.py
 │    └── models.py
 ├── schemas/
 ├── routes/
 │    ├── auth.py
 │    ├── transaction.py
 │    └── analytics.py
 ├── dependencies/
 │    ├── auth.py
 │    └── roles.py
 └── core/
      └── security.py
```

---

## 🔐 Authentication & Authorization

### Authentication

* JWT-based authentication
* Users login and receive an access token
* Token must be included in protected requests

### Authorization (RBAC)

| Role    | Permissions                                      |
| ------- | ------------------------------------------------ |
| Admin   | Full access (CRUD + analytics + user management) |
| Analyst | Create + Read + Analytics                        |
| Viewer  | Read-only access                                 |

---

## 👤 User Management

### Features:

* Register users with roles
* Login to receive JWT token
* Role-based restrictions enforced at API level

---

## 💰 Transaction Management

### Supported Operations:

* Create transaction
* Get all transactions
* Update transaction
* Delete transaction
* Filter transactions

### Example Transaction:

```json
{
  "amount": 5000,
  "type": "expense",
  "category": "food",
  "date": "2026-04-02",
  "notes": "Groceries"
}
```

---

## 📊 Analytics APIs

### 1. Summary

* Total income
* Total expense
* Net balance

### 2. Category Breakdown

* Total per category

### 3. Recent Transactions

* Latest 5 entries

### 4. Monthly Trends

* Aggregated monthly totals

---

## 🔑 API Endpoints

### Auth

* `POST /auth/register`
* `POST /auth/login`

### Transactions

* `POST /transactions`
* `GET /transactions`
* `PUT /transactions/{id}`
* `DELETE /transactions/{id}`
* `GET /transactions/filter`

### Analytics

* `GET /analytics/summary`
* `GET /analytics/category`
* `GET /analytics/recent`
* `GET /analytics/monthly`

---

## 🧪 How to Run Locally

### 1. Clone repository

```
git clone <your-repo-link>
cd finance-backend
```

### 2. Create virtual environment

```
python -m venv venv
```

### 3. Activate environment

```
venv\Scripts\activate   (Windows)
source venv/bin/activate (Mac/Linux)
```

### 4. Install dependencies

```
pip install -r requirements.txt
```

### 5. Run server

```
uvicorn app.main:app --reload
```

---

## 📘 API Documentation

After running the server:

* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

---

## 🧠 Design Decisions

* Used layered architecture (routes → dependencies → db)
* Implemented RBAC using dependency injection
* Separated schemas for validation and response safety
* Used aggregation queries for analytics instead of manual logic

---

## ⚠️ Assumptions

* Role values are predefined: `admin`, `analyst`, `viewer`
* SQLite used for simplicity (can be swapped)
* Authentication is stateless using JWT

---

## 👨‍💻 Author

Kanishk Jaiswal

---
