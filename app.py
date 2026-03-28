from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'suhani'
app.config['MYSQL_DB'] = 'password_manager'

mysql = MySQL(app)

@app.route("/")
def home():
    return "<h1>Password Manager Backend is running!</h1>"

@app.route("/save-password", methods=["POST"])
def save_password():
    data = request.get_json()
    site_name = data['website']
    username = data['username']
    password = data['password']

    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO passwords (vault_id, sitename, username, encrypted_password)
        VALUES (%s, %s, %s, %s)
    """, (201, site_name, username, password))
    mysql.connection.commit()
    cur.close()

    return jsonify({"status": "success", "message": "Password saved!"})

@app.route("/get-passwords", methods=["GET"])
def get_passwords():
    cur = mysql.connection.cursor()
    cur.execute("SELECT sitename, username, encrypted_password FROM passwords")
    rows = cur.fetchall()
    cur.close()

    passwords = []
    for row in rows:
        passwords.append({
            "website": row[0],
            "username": row[1],
            "password": row[2]
        })

    return jsonify(passwords)

if __name__ == "__main__":
    app.run(debug=True)
        