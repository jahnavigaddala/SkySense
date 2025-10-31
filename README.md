🌦️ SkySense — “See the sky like never before.”

------------------------------------------------------------

📁 Folder Structure

SkySense/
│
├── server/
│   ├── server.js
│   ├── utils/
│   │   ├── compression.js
│   │   ├── encryption.js
│   │   └── logger.js
│   ├── db/
│   │   ├── database.py
│   │   └── schema.sql
│
├── client/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   ├── utils/
│   │   ├── compression.js
│   │   └── encryption.js
│   ├── assets/
│   │   └── icons/   (optional weather icons)
│
├── web_dashboard/
│   ├── app.py
│   ├── static/
│   │   ├── style.css
│   ├── templates/
│   │   └── dashboard.html
│
├── .env
├── .gitignore
├── package.json
├── README.txt
└── requirements.txt


------------------------------------------------------------
🌍 Project Overview

SkySense is a next-generation weather forecast web application built with Node.js, Express, and the OpenWeatherMap API.
It features a modern Pinterest-style UI, temperature-based theme colors, and a 7-day weather forecast graph.


------------------------------------------------------------
✨ Features

✅ Search weather by city name
✅ Detect weather using your current location
✅ Display temperature, humidity, wind speed, and conditions
✅ Interactive 7-day forecast chart
✅ Dynamic color themes based on temperature
✅ Responsive Pinterest-style UI
✅ Activity logging and local database support


------------------------------------------------------------
🧩 Tech Stack

Frontend: HTML, CSS, JavaScript
Backend: Node.js + Express
Database: SQLite (via database.py and schema.sql)
Visualization: Chart.js
API: OpenWeatherMap API
Optional Dashboard: Flask (for data display via web_dashboard/app.py)


------------------------------------------------------------
⚙️ Setup Instructions

1. Clone this repository:
   git clone https://github.com/yourusername/SkySense.git
   cd SkySense

2. Install backend dependencies:
   npm install

3. (Optional) For the dashboard:
   pip install -r requirements.txt

4. Create .env file in the root directory:
   WEATHER_API_KEY=your_api_key_here

5. Run the server:
   node server/server.js

6. Open in browser:
   http://localhost:3000


------------------------------------------------------------
🌈 How It Works

- User inputs a city or clicks “Use My Location.”
- The backend fetches real-time data from the OpenWeatherMap API.
- Frontend displays:
  • Current weather details
  • 7-day temperature and humidity chart
  • Dynamic background colors based on temperature
- The Flask dashboard (optional) can be used to view activity logs and database records.


------------------------------------------------------------
🚀 Deployment Guide

To deploy on Render / Vercel:

1. Push your project to GitHub (without .env).
2. On the Render/Vercel dashboard:
   - Connect your repo
   - Add an environment variable:
       Key: WEATHER_API_KEY
       Value: your_api_key_here
3. Deploy!
4. Open your hosted SkySense app online 🎉


------------------------------------------------------------
🔒 Security Notes

Do not upload your .env file to GitHub.
Your .gitignore must include:
   node_modules/
   .env
   __pycache__/


------------------------------------------------------------
🧠 Future Enhancements

🌤️ Weather icons and animations
🕶️ Dark/light mode toggle
💨 Air Quality Index integration
🌍 Multi-language support


------------------------------------------------------------
👩‍💻 Developer Info

Created by: Jahnavi
Project: SkySense
Tagline: “See the sky like never before.”

