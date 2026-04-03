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

## 📘 Detailed Endpoint Descriptions & Usage

### 🔐 Authentication APIs

#### 1. Register User

* **POST** `/auth/register`
* **Description:** Create a new user with a specific role

**Request Body:**

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "123456",
  "role": "admin"
}
```

---

#### 2. Login User

* **POST** `/auth/login`
* **Description:** Authenticate user and return JWT token

**Response:**

```json
{
  "access_token": "your_token_here",
  "token_type": "bearer"
}
```

---

### 💰 Transaction APIs

#### 3. Create Transaction

* **POST** `/transactions`
* **Access:** Admin, Analyst
* **Description:** Create a financial record

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

#### 4. Get All Transactions

* **GET** `/transactions`
* **Access:** All roles
* **Description:** Retrieve all transactions

---

#### 5. Update Transaction

* **PUT** `/transactions/{id}`
* **Access:** Admin
* **Description:** Update a transaction by ID

---

#### 6. Delete Transaction

* **DELETE** `/transactions/{id}`
* **Access:** Admin
* **Description:** Delete a transaction

---

#### 7. Filter Transactions

* **GET** `/transactions/filter`
* **Access:** All roles

**Query Params:**

* `type` (income/expense)
* `category`

**Example:**

```
/transactions/filter?type=income
```

---

### 📊 Analytics APIs

#### 8. Summary

* **GET** `/analytics/summary`
* **Access:** Admin, Analyst
* **Description:** Returns total income, expense, and balance

---

#### 9. Category Breakdown

* **GET** `/analytics/category`
* **Access:** Admin, Analyst
* **Description:** Returns total amount grouped by category

---

#### 10. Recent Transactions

* **GET** `/analytics/recent`
* **Access:** All roles
* **Description:** Returns last 5 transactions

---

#### 11. Monthly Trends

* **GET** `/analytics/monthly`
* **Access:** Admin, Analyst
* **Description:** Returns monthly aggregated totals

---

## 🔑 Authentication Usage

All protected endpoints require a JWT token.

**Header Format:**

```
Authorization: Bearer <your_token>
```

You can authorize easily via Swagger UI:
👉 `/docs`

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

* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

---

 ## 👨‍💻 Author

Kanishk Jaiswal

---
