# 🌾 KisanSetu - Smart Farmer Agriculture Platform

KisanSetu is an integrated platform designed for farmers to get optimal market rates, consult an AI agricultural advisor, scan vegetable harvest quality, and track daily Mandi prices.

---

## 🚀 Key Features

1. **🤖 Kisan AI Chatbot (`/chatbot.html`)**
   - AI-powered farmer assistant connected to Google Gemini API (`gemini-1.5-flash`).
   - Answers queries on crop cultivation, pest and disease identification, organic & chemical fertilizer dosages, drip irrigation schedules, weather risks, and market price tips.
   - Includes voice speech input support and quick prompt suggestions.
   - Built-in offline fallback with domain knowledge if the API key is not configured.

2. **📊 Live / Daily Mandi Crop Prices (`/market.html`)**
   - Live backend API (`/api/prices`) tracking daily rates across regional APMC Mandis (Coimbatore Mandi, Mettupalayam, Pollachi, Tiruppur, Ooty, Nashik, etc.).
   - Dynamically supports: **Tomato, Onion, Potato, Paddy, Maize, Chilli, Banana, Brinjal, Carrot, Cabbage, Cauliflower, Garlic, Ginger, Wheat, Groundnut, Cotton**.
   - Displays modal price (₹/kg), min/max range, market name, and daily last updated date.
   - Interactive Leaflet map with locator for regional agricultural dealers and Mandis.

3. **🔬 Vegetable Quality Detection (`/quality-detection.html`)**
   - Upload produce photo or snap directly using smartphone/webcam camera.
   - AI Vision service analyzes surface texture, blemishes, decay, and color uniformity.
   - Classifies produce into **GOOD** (Grade A - Premium), **AVERAGE** (Grade B - Fair Market), or **BAD** (Severe Rot/Discard).
   - Generates confidence rating, freshness score (1-10), defect list, and practical storage/mandi selling advice.
   - One-click transfer to "Sell My Crop" pre-filling the detected crop and grade.

4. **🌾 Expanded Crop Catalog & Visual Cards (`static/images/crops/`)**
   - 16 vector SVG illustrations organized in `frontend/static/images/crops/`.
   - Rich visual cards for crop selection in `sell-crop.html` and the dashboard carousel.

---

## 🛠️ Installation & Setup (VS Code)

### 1. Open in VS Code
Open the project directory in VS Code:
```bash
cd c:\Users\DELL\Desktop\KisanSetu\kisansetu
```

### 2. Install Dependencies
Ensure Python 3.9+ is installed, then run:
```bash
pip install -r requirements.txt
```
*(Dependencies: `flask`, `python-dotenv`, `requests`, `pillow`)*

### 3. Configure API Key in `.env`
Open the `.env` file in the `kisansetu/` directory:
```env
# Get a free Gemini API key from https://aistudio.google.com/app/apikey
GEMINI_API_KEY=your_actual_gemini_api_key_here

FLASK_ENV=development
FLASK_DEBUG=True
PORT=5000
HOST=127.0.0.1
```
> **Note**: Even without an API key, KisanSetu will run smoothly with its built-in intelligent agricultural advisor and image heuristic analysis!

### 4. Run the Application
Start the Flask backend server:
```bash
python app.py
```

Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

---

## 🧪 Running Automated Tests

To run the automated test suite verifying all routes, APIs, and image assets:
```bash
python -m unittest tests/test_backend.py
```

---

## 📁 Project Structure

```
kisansetu/
├── app.py                      # Main Flask application & routes configuration
├── kisansetu.db                # SQLite database (users, crops, alerts, daily_prices, quality_scans)
├── .env                        # Local environment variables (Gemini API Key)
├── .env.example                # Example environment template
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation & run guide
├── routes/
│   ├── __init__.py
│   ├── chatbot.py              # POST /api/chatbot
│   ├── prices.py               # GET /api/prices, /api/prices/summary, /api/prices/crops
│   └── quality.py              # POST /api/quality-detect
├── services/
│   ├── __init__.py
│   ├── gemini_service.py       # Gemini Chat & Vision service with offline fallback
│   └── price_service.py        # Mandi price database management & daily updates
├── tests/
│   └── test_backend.py         # Automated integration test suite
└── frontend/
    ├── index.html              # Farmer Dashboard with AI banners & crop rates
    ├── chatbot.html            # Dedicated Kisan AI Chatbot page
    ├── quality-detection.html  # Vegetable Quality Detection page
    ├── market.html             # Nearby Markets & dynamic daily prices with Leaflet map
    ├── sell-crop.html          # Sell Crop with rich visual cards & AI deal score
    ├── buyers.html             # Verified buyers list
    ├── alerts.html             # Price alert configuration
    ├── earning.html            # Farmer earnings & transaction history
    ├── login.html              # Farmer login
    ├── register.html           # Farmer registration
    ├── script.js               # Frontend JavaScript logic (Chat, Vision, Maps, Prices)
    ├── style.css               # Responsive styling across mobile & desktop
    └── static/
        └── images/
            └── crops/          # SVG crop illustrations (16 crops)
```
