# 🔐 Vault — Password Manager

A full stack password manager built with HTML, CSS, JavaScript, Python Flask and MySQL.

## Features
- Save passwords for any website
- View all saved passwords
- Show/hide password toggle
- Search passwords by website or username
- Delete passwords
- Clean minimal UI

## Tech Stack
- **Frontend** — HTML, CSS, JavaScript
- **Backend** — Python Flask
- **Database** — MySQL

## Project Structure
```
password-manager/
├── index.html       # Frontend UI
├── app.py           # Flask backend
└── database.sql     # MySQL table definitions
```

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/suhanigupta2006-jpg/password-manager
```

### 2. Install Python dependencies
```bash
pip3 install flask flask-mysqldb flask-cors
```

### 3. Set up MySQL
- Create a database called `password_manager`
- Run `database.sql` to create the tables

### 4. Run the Flask server
```bash
python3 app.py
```

### 5. Open the frontend
- Open `index.html` with Live Server in VS Code

## Screenshot
![Password Manager UI](password_manager.jpeg)

## Author
Made by Suhani Gupta
