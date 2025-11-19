# dashboard.py

import streamlit as st
import requests
from deep_translator import GoogleTranslator as Translator
from datetime import datetime

API_URL = "https://shopgenius-ai-backend.onrender.com/"

st.set_page_config(page_title="AI Shopping Assistant", layout="centered")

# -------------------------------------------------
# LOGIN CHECK
# -------------------------------------------------
if not st.session_state.get("logged_in", False):
    st.switch_page("pages/login.py")

user = st.session_state["user"]
name = user.get("name", "User")

st.title("🤖 AI Shopping Assistant")
st.caption(f"Welcome, {name} 👋")

# -------------------------------------------------
# LOGOUT
# -------------------------------------------------
if st.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.user = {}
    st.switch_page("pages/login.py")

# -------------------------------------------------
# CHAT MEMORY
# -------------------------------------------------
if "chat" not in st.session_state:
    st.session_state.chat = []

if "last_input" not in st.session_state:
    st.session_state.last_input = None

# Display chat history
for msg in st.session_state.chat:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
        if msg.get("ts"):
            st.caption(msg["ts"])


# -------------------------------------------------
# USER INPUT
# -------------------------------------------------
query = st.chat_input("Search products or ask for comparison...")

if query:

    if query == st.session_state.last_input:
        st.stop()
    st.session_state.last_input = query

    # Save user message
    msg_user = {
        "role": "user",
        "content": query,
        "ts": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    }
    st.session_state.chat.append(msg_user)

    # Assistant typing placeholder
    with st.chat_message("assistant"):
        loader = st.empty()
        loader.write("🔎 Processing...")

    # Translate
    try:
        translated = Translator(source="auto", target="en").translate(query)
    except:
        translated = query

    # -------------------------------------------------
    # CALL BACKEND API
    # -------------------------------------------------
    try:
        r = requests.get(API_URL, params={"query": translated}, timeout=10)
        data = r.json()

        mode = data.get("mode")

        # -------------------------------------------------
        # 🟢 GREETING MODE
        # -------------------------------------------------
        if mode == "greeting":
            reply = data.get("reply", "👋 Hello! How can I help you today?")

        # -------------------------------------------------
        # 🟦 COMPARISON MODE
        # -------------------------------------------------
        elif mode == "compare":
            p1 = data.get("product_1", {})
            p2 = data.get("product_2", {})

            reply = (
                "🆚 **Comparison Result**\n\n"
                f"📌 **{p1.get('title','Product A')}** — {p1.get('price','N/A')}\n"
                f"🔗 [Link]({p1.get('url','#')})\n\n"
                f"📌 **{p2.get('title','Product B')}** — {p2.get('price','N/A')}\n"
                f"🔗 [Link]({p2.get('url','#')})\n\n"
            )

        # -------------------------------------------------
        # 🔍 NORMAL SEARCH MODE
        # -------------------------------------------------
        else:
            products = data.get("results", [])

            if not products:
                reply = "😕 No products found."
            else:
                reply = f"🔍 Found **{len(products)}** products:\n\n"
                for p in products[:5]:
                    reply += (
                        f"🛒 **{p.get('title','No Title')}**\n"
                        f"💰 {p.get('price','N/A')}\n"
                        f"🔗 [Open]({p.get('url','#')})\n\n"
                    )

    except Exception as e:
        reply = f"❌ Backend error: {e}"

    # Display assistant reply
    loader.write(reply)

    # Save message
    st.session_state.chat.append({
        "role": "assistant",
        "content": reply,
        "ts": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    })

    st.rerun()

