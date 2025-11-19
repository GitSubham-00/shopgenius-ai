import streamlit as st

st.set_page_config(page_title="AI Shopping Assistant")

# -------------------------------------
# SESSION INIT (Important)
# -------------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = {}

# -------------------------------------
# MAIN ROUTER
# -------------------------------------
# If not logged in → go to login page
if not st.session_state.logged_in:
    st.switch_page("pages/login.py")

# If user is admin → go to admin panel
elif st.session_state.user.get("role") == "admin":
    st.switch_page("pages/admin.py")

# If normal user → go to dashboard
else:
    st.switch_page("pages/dashboard.py")
