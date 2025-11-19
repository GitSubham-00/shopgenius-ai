# 🛒 ShopGenius AI Assistant  
### _AI-Powered Virtual Shopping Assistant (FastAPI + Streamlit + MongoDB + NLP)_

---

## 🚧 Project Status: UNDER ACTIVE DEVELOPMENT  
This project is **NOT fully completed**.  
Several features are still being built, refined, and optimized.

We are actively working on:

- Improving NLP accuracy  
- Adding more API integrations  
- Enhancing UI/UX  
- Stabilizing FastAPI backend  
- Fixing detected bugs  
- Expanding admin features  

➡️ **Expect rapid updates & improvements!**

---

## 🌟 Overview  

**ShopGenius AI Assistant** is a smart, interactive virtual shopping chatbot that helps users:

- 🔍 Search products  
- 🆚 Compare two items  
- 🌐 Translate multi-language queries  
- 📈 Track price history  
- 💬 Chat with an AI-style interface  
- 🔐 Login & signup securely  
- 🛠 Manage users through an Admin Panel  

---

## 🚀 Live Demo  
_(Add your Streamlit Cloud link here after deployment)_  



---

## 🧠 Features  

### 🔍 Smart Product Search  
Supports queries like:
- *iPhone 13 under 50000*
- *Samsung S22 mobile*
- *Laptop below 40000*

### 🌐 Multi-Language Support  
Automatic translation using Google Translator API.

### 🆚 Product Comparison  
Ask:
- *compare iphone 13 and samsung s22


### 💰 USD → INR Price Conversion  
Backend automatically converts all detected prices to Indian Rupees.

### 📊 Price History Tracking  
Every search is saved in MongoDB for analytics and trends.

### 🔐 Authentication System  
- User Signup  
- Login  
- Role-based access (User / Admin)

### 🛠 Admin Panel  
Admins can:
- View all users  
- Delete users  
- Upgrade users to admin  

### 💬 Chat-Based UI  
Modern Streamlit chat interface for smooth user experience.

---

## 🏗 Tech Stack  

| Layer | Technology |
|------|-------------|
| **Frontend** | Streamlit |
| **Backend** | FastAPI |
| **Database** | MongoDB Atlas |
| **NLP Engine** | spaCy |
| **Translation** | Deep Translator |
| **Product API** | RapidAPI Amazon Search |

---

## 📁 Project Structure  
project/
├── app.py
├── main.py
├── api_handler.py
├── nlp_engine.py
├── database.py
├── pages/
│ ├── login.py
│ ├── signup.py
│ ├── admin.py
│ └── dashboard.py
├── requirements.txt
└── .env


---

## ⚙️ Setup Instructions  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-username/shopgenius-ai-assistant
cd shopgenius-ai-assistant
```
### 2️⃣ Install Dependencies
```bash
-pip install -r requirements.txt
```
###3️⃣ Create .env file

MONGO_URI=your_mongodb_atlas_url
RAPID_AMAZON_KEY=your_rapid_api_key
RAPID_AMAZON_HOST=your_rapid_api_host
