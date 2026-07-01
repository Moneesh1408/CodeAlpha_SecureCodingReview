import sqlite3
import bcrypt
from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if not username or not password:
        return "Missing fields", 400
    
    # SECURE FIX 1: Use bcrypt instead of MD5 for modern hashing
    # (Note: In a live app, you would fetch the stored hash from DB to compare)
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # SECURE FIX 2: Use parameterized queries to prevent SQL injection
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    
    return "Login Route"