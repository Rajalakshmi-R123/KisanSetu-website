import os
import sqlite3
from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_FOLDER = os.path.join(BASE_DIR, "frontend")
DATABASE = os.path.join(BASE_DIR, "kisansetu.db")

app = Flask(
    __name__,
    static_folder=os.path.join(FRONTEND_FOLDER, "static"),
    static_url_path="/static"
)
app.config["DATABASE"] = DATABASE

# Import API blueprints and services
from routes.chatbot import chatbot_bp
from routes.prices import prices_bp
from routes.quality import quality_bp
from services.price_service import init_prices_table

# Register modular blueprints
app.register_blueprint(chatbot_bp)
app.register_blueprint(prices_bp)
app.register_blueprint(quality_bp)


# ---------------- DATABASE ----------------

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_database():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS crops (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            crop TEXT NOT NULL,
            quantity REAL NOT NULL,
            quality TEXT,
            expected_price REAL,
            location TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            crop TEXT NOT NULL,
            target_price REAL NOT NULL,
            sms INTEGER DEFAULT 0,
            app INTEGER DEFAULT 0,
            email INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()

    # Initialize live prices and quality scans tables
    init_prices_table(DATABASE)


# ---------------- FRONTEND PAGES ----------------

@app.route("/")
@app.route("/index.html")
@app.route("/dashboard.html")
def index():
    return send_from_directory(FRONTEND_FOLDER, "index.html")


@app.route("/<page>")
def pages(page):
    allowed_pages = [
        "sell-crop.html",
        "market.html",
        "buyers.html",
        "alerts.html",
        "earning.html",
        "login.html",
        "register.html",
        "quality-detection.html",
        "chatbot.html"
    ]

    if page in allowed_pages:
        return send_from_directory(FRONTEND_FOLDER, page)

    return "Page not found", 404


# ---------------- STATIC ASSETS (CSS / JS / IMAGES) ----------------

@app.route("/style.css")
def css():
    return send_from_directory(FRONTEND_FOLDER, "style.css")


@app.route("/script.js")
def javascript():
    return send_from_directory(FRONTEND_FOLDER, "script.js")


# ---------------- REGISTER ----------------

@app.route("/api/register", methods=["POST"])
def register():
    data = request.json
    if not data:
        return jsonify({"success": False, "message": "Invalid request body"}), 400

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return jsonify({
            "success": False,
            "message": "All fields are required"
        }), 400

    conn = get_db()
    try:
        conn.execute("""
            INSERT INTO users (name, email, password)
            VALUES (?, ?, ?)
        """, (name, email, password))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({
            "success": False,
            "message": "Email already registered"
        }), 400

    conn.close()
    return jsonify({
        "success": True,
        "message": "Registration successful"
    })


# ---------------- LOGIN ----------------

@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    if not data:
        return jsonify({"success": False, "message": "Invalid request body"}), 400

    email = data.get("email")
    password = data.get("password")

    conn = get_db()
    user = conn.execute("""
        SELECT * FROM users
        WHERE email = ? AND password = ?
    """, (email, password)).fetchone()
    conn.close()

    if user:
        return jsonify({
            "success": True,
            "message": "Login successful",
            "user": user["name"]
        })

    return jsonify({
        "success": False,
        "message": "Invalid email or password"
    }), 401


# ---------------- SELL CROP ----------------

@app.route("/api/sell-crop", methods=["POST"])
def sell_crop():
    data = request.json
    if not data:
        return jsonify({"success": False, "message": "Invalid request body"}), 400

    crop = data.get("crop")
    quantity = data.get("quantity")
    quality = data.get("quality")
    expected_price = data.get("expectedPrice")
    location = data.get("location")

    conn = get_db()
    conn.execute("""
        INSERT INTO crops
        (crop, quantity, quality, expected_price, location)
        VALUES (?, ?, ?, ?, ?)
    """, (crop, quantity, quality, expected_price, location))
    conn.commit()
    conn.close()

    return jsonify({
        "success": True,
        "message": "Crop details saved successfully"
    })


# ---------------- PRICE ALERT ----------------

@app.route("/api/alerts", methods=["POST"])
def create_alert():
    data = request.json
    if not data:
        return jsonify({"success": False, "message": "Invalid request body"}), 400

    crop = data.get("crop")
    target_price = data.get("targetPrice")
    sms = 1 if data.get("sms") else 0
    app_notification = 1 if data.get("app") else 0
    email = 1 if data.get("email") else 0

    conn = get_db()
    conn.execute("""
        INSERT INTO alerts
        (crop, target_price, sms, app, email)
        VALUES (?, ?, ?, ?, ?)
    """, (crop, target_price, sms, app_notification, email))
    conn.commit()
    conn.close()

    return jsonify({
        "success": True,
        "message": "Price alert created successfully"
    })


# ---------------- GET ALERTS ----------------

@app.route("/api/alerts", methods=["GET"])
def get_alerts():
    conn = get_db()
    alerts = conn.execute("SELECT * FROM alerts").fetchall()
    conn.close()
    return jsonify([dict(alert) for alert in alerts])


# ---------------- RUN ----------------

if __name__ == "__main__":
    create_database()
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "True").lower() in ("true", "1")
    app.run(debug=debug, host=host, port=port)