import sqlite3
import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Insecure MD5 Hash
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    
    # Vulnerable SQL String Concatenation
    query = f"SELECT * FROM users WHERE username = '{username}'"
    return "Login Route"