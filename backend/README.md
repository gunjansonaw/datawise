# 📊 Dataset Catalog API – Flask + MongoDB

This is a lightweight backend API built with Flask and MongoDB for managing datasets and their quality logs. It supports full CRUD for datasets and logs, along with Swagger docs, filtering, soft deletion, and test coverage.

---

## 🚀 Features

- Create, view, update, and soft-delete datasets
- Add and fetch quality logs (`PASS` / `FAIL`) for datasets
- Filter datasets by owner and tag
- Swagger documentation via Flasgger
- Clean folder structure (routes, services, models, utils)
- Basic unit tests using pytest

---

## 🛠️ Tech Stack

- Python 3.10+
- Flask 2.x
- MongoDB (via Flask-PyMongo)
- Pytest
- Swagger UI (Flasgger)

---

## 📁 Project Structure

backend/
├── app.py # Main Flask app
├── models/ # Dataset & quality log models
├── routes/ # Route handlers
├── services/ # Business logic
├── utils/ # DB, helper utils
├── tests/ # Pytest unit tests
├── requirements.txt # Python dependencies
└── README.md # You're here!


---

## ▶️ Getting Started

### 🔧 Setup

```bash
# Clone the repo
git clone https://github.com/gunjansonaw/datawise


# Create virtual environment
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate on Linux/mac

# Install dependencies
pip install -r requirements.txt
#how to run
Run the API
bash
Copy
Edit
python app.py

📬 API Endpoints
Method	 Route	                    Description
POST	 /datasets	              Create a new dataset
GET	     /datasets	              List all datasets (filterable)
GET	     /datasets/<id> 	      Get dataset by ID
PUT	     /datasets/<id>	           Update dataset
DELETE	 /datasets/<id>	           Soft delete dataset
POST	 /datasets/<id>/quality-1	Add a quality log
GET	     /datasets/<id>/quality-1	Get quality logs