# signup.py

import streamlit as st
from database import create_user

st.set_page_config(page_title="Sign Up")

# logged in users → dashboard
if st.session_state.get("logged_in", False):
    st.switch_page("pages/dashboard.py")

st.title("📝 Create Account")

name = st.text_input("Full Name")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
confirm = st.text_input("Confirm Password", type="password")

if st.button("Sign Up"):
    if not name or not email or not password:
        st.error("All fields are required.")
    elif password != confirm:
        st.error("❌ Passwords do not match!")
    else:
        ok, msg = create_user(name, email, password)

        if ok:
            st.success(msg)
            st.switch_page("pages/login.py")
        else:
            st.error(msg)

st.page_link("pages/login.py", label="Already have an account? Login", icon="🔑")
