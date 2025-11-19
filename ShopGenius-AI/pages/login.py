# login.py

import streamlit as st
from database import validate_login

st.set_page_config(page_title="Login")

# Already logged in?
if st.session_state.get("logged_in", False):
    if st.session_state["user"]["role"] == "admin":
        st.switch_page("pages/admin.py")
    else:
        st.switch_page("pages/dashboard.py")

st.title("🔐 Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    user = validate_login(email, password)

    if user:
        st.session_state.logged_in = True
        st.session_state.user = {
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"],
            "role": user["role"]
        }

        st.success("Login successful! Redirecting...")

        if user["role"] == "admin":
            st.switch_page("pages/admin.py")
        else:
            st.switch_page("pages/dashboard.py")

    else:
        st.error("Invalid email or password.")

st.page_link("pages/signup.py", label="Don't have an account? Sign Up", icon="📝")
