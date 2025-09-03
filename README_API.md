

markdown
# Flask To-Do API

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-orange?logo=flask)](https://flask.palletsprojects.com/)
[![Postman](https://img.shields.io/badge/Postman-API%20Testing-red?logo=postman)](https://www.postman.com/)

A simple **RESTful API built with Flask** for managing a to-do list.  
Demonstrates CRUD operations (**Create, Read, Update, Delete**) using JSON.

---

## 🚀 Features

- CRUD operations on tasks  
- JSON-based data handling  
- Ready to test with **Postman**  
- Returns proper HTTP responses and error messages  



## 🛠 Requirements

- Python 3.x  
- Flask (`pip install flask`)  
- Optional: [Postman](https://www.postman.com/) for testing



## ⚡ How to Run

1. Open terminal and navigate to your project folder:

```bash
cd path/to/Flask
````

2. Run the API:

```bash
python app.py
```

* API runs at: `http://127.0.0.1:5000/`



## 📌 API Endpoints

| Method | Endpoint    | Description              |
| ------ | ----------- | ------------------------ |
| GET    | /items      | Retrieve all items       |
| GET    | /items/<id> | Retrieve a specific item |
| POST   | /items      | Add a new item           |
| PUT    | /items/<id> | Update an existing item  |
| DELETE | /items/<id> | Delete an item           |



## 📝 Postman Flow

| Step | Method | Endpoint | Body (if applicable)                                | Description                     |
| ---- | ------ | -------- | --------------------------------------------------- | ------------------------------- |
| 1    | GET    | /items   | -                                                   | Retrieve all items              |
| 2    | POST   | /items   | `{"name":"Item 3","description":"This is item 3"}`  | Add a new item                  |
| 3    | GET    | /items/3 | -                                                   | Retrieve the newly created item |
| 4    | PUT    | /items/3 | `{"name":"Updated Item 3","description":"Updated"}` | Update an existing item         |
| 5    | DELETE | /items/3 | -                                                   | Delete an item                  |


## ⚠ Notes

* Data is **in-memory**, resets on server restart.
* `.gitignore` prevents tracking of `venv/`, `__pycache__/`, logs, and editor files.
* Can be extended to use a **database** for persistence.


