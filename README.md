🛒 ShopGenius AI Assistant
AI-Powered Virtual Shopping Assistant (FastAPI + Streamlit + MongoDB + NLP)

🚧 STATUS: PROJECT UNDER ACTIVE DEVELOPMENT
This project is NOT fully completed. Several features are still being built, refined, and optimized.
We are actively working on:

Improving NLP accuracy

Adding more API integrations

Enhancing UI/UX

Stabilizing FastAPI backend

Fixing detected bugs

Expanding admin features

So expect quick updates and improvements!

🌟 Overview

ShopGenius AI Assistant is a smart, interactive virtual shopping chatbot that helps users:

Search products

Compare two items

Translate multi-language queries

Track price history

Chat with an AI-driven UI

View clean product cards

Login & signup

Manage users through an admin panel

🚀 Live Demo

(You will paste your Streamlit Cloud link here after deployment)

https://your-streamlit-app-url.streamlit.app

🧠 Features
🔍 Smart Product Search

Search any product like:

iPhone 13 under 50000

Samsung s22 mobile

Laptop below 40000

🌐 Multi-Language Support

Automatic translation using Google Translator API.

🆚 Product Comparison

Ask:

compare iphone 13 and samsung s22

💰 USD → INR Price Conversion

All prices automatically converted to INR.

📊 Price History Tracking

Every product search is stored in MongoDB.

🔐 Auth System

User signup

Login

Role-based access

🛠 Admin Panel

Admin can:

View users

Delete users

Upgrade to admin

💬 Chat-Based UI

Modern Streamlit chat interface.

🏗 Tech Stack
Layer	Technology
Frontend	Streamlit
Backend	FastAPI
Database	MongoDB Atlas
NLP	spaCy
Translation	GoogleTranslator
Product API	RapidAPI Amazon Search
📁 Project Structure
project/
 ├── app.py
 ├── main.py
 ├── api_handler.py
 ├── nlp_engine.py
 ├── database.py
 ├── pages/
 │     ├── login.py
 │     ├── signup.py
 │     ├── admin.py
 │     └── dashboard.py
 ├── requirements.txt
 └── .env

⚙️ Setup Instructions
1️⃣ Clone Repository
git clone https://github.com/your-username/shopgenius-ai-assistant
cd shopgenius-ai-assistant

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Configure Environment Variables

Create a .env file:

MONGO_URI=your_mongodb_atlas_url
RAPID_AMAZON_KEY=your_rapid_api_key
RAPID_AMAZON_HOST=your_amazon_host

▶️ Run Backend (FastAPI)
uvicorn main:app --reload

▶️ Run Frontend (Streamlit)
streamlit run app.py

☁️ Deploy on Streamlit Cloud

Push the project to GitHub

Open share.streamlit.io

Select your repository

Choose app.py as the entry point

Add secrets under Manage Secrets

Deploy 🚀

🔮 Future Enhancements

(These are planned and will be added soon)

Flipkart product API

Voice search

Real-time price alerts

Smart product recommendations

More NLP intent detection

Better UI improvements

⭐ Support

If you like this project, please ⭐ star the repository.
It motivates further development and improvements!

📬 Contact

Developer: Subham Maity
📧 Email: work.subham2004@gmail.com
