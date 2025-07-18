🚀 Insta Vibe Generator - Gen-Z Instagram Username AI
Yeh ek full-stack web application hai jo aapke naam, hobby, aur vibe ke hisaab se AI ka istemal karke creative aur unique Instagram usernames generate karta hai.

✨ Live Demo
Frontend (Netlify): [Yahaan apna Netlify URL daalein]

Backend (Render): [Yahaan apna Render URL daalein]

🛠️ Tech Stack (Kya-kya istemal hua hai)
Frontend:

React.js (with Vite)

Tailwind CSS

Backend:

Python

Flask (for the server)

Google Gemini API (for AI generation)

Deployment:

Render (for Backend)

Netlify (for Frontend)

💻 Local Development Setup (Apne Computer par Kaise Chalayein)
Is project ko apne computer par chalane ke liye, neeche diye gaye steps follow karein.

1. Backend Server Chalu Karein
Pehle hum Python wala server chalu karenge.

# Step 1: Backend folder ke andar jaayein
cd backend

# Step 2: Ek naya virtual environment banayein (agar pehle se nahi hai)
python3 -m venv env

# Step 3: Virtual environment ko activate karein
# macOS/Linux par:
source env/bin/activate
# Windows par:
# .\env\Scripts\activate

# Step 4: Saari zaroori libraries install karein
pip install -r requirements.txt

# Step 5: Backend server ko chalu karein
python app.py

Ab aapka backend server http://127.0.0.1:5000 par chal raha hai. Is terminal ko chalta hua chhod dein.

2. Frontend Server Chalu Karein
Ab hum React wala app chalu karenge.

# Step 1: Ek naya terminal kholein
# Step 2: Frontend folder ke andar jaayein
cd Frontend

# Step 3: Saari zaroori node modules install karein (sirf pehli baar)
npm install

# Step 4: Frontend development server ko chalu karein
npm run dev

Ab aapka frontend server http://localhost:5173 (ya kisi aur port) par chal raha hai. Is URL ko apne browser mein kholein.

🚀 Deployment (Internet par Live Kaise Karein)
Is app ko poori duniya ke liye live karne ke liye, humein backend aur frontend ko alag-alag deploy karna hoga.

Part A: Backend ko Render par Deploy Karna
Code ko GitHub par Push Karein: Sunishchit karein ki aapka saara code ek GitHub repository mein push kiya hua hai.

Render par Account Banayein: render.com par jaayein aur apne GitHub account se sign up karein.

New Web Service Banayein: Dashboard par, New + > Web Service par click karein aur apni GitHub repository ko connect karein.

Settings Bharein:

Name: insta-vibe-backend (ya jo bhi aapko pasand ho)

Root Directory: backend

Build Command: pip install -r requirements.txt

Start Command: gunicorn app:app

Instance Type: Free

Environment Variable Add Karein: "Advanced" section mein, ek environment variable add karein:

Key: GOOGLE_API_KEY

Value: Apni Gemini API key yahaan paste kar dein.

Deploy Karein: Create Web Service par click karein. Thodi der mein aapka backend live ho jaayega aur aapko ek URL mil jaayega.

Part B: Frontend ko Netlify par Deploy Karna
Code Update Karein: Apne Frontend/src/App.jsx mein fetch wali line ko Render se mile URL se update karein.

Netlify par Account Banayein: netlify.com par jaayein aur apne GitHub account se sign up karein.

New Site Banayein: "Add new site" > "Import an existing project" par click karein aur apni GitHub repository ko connect karein.

Build Settings Bharein:

Base directory: Frontend

Build command: npm run build

Publish directory: Frontend/dist

Environment Variable Add Karein: "
