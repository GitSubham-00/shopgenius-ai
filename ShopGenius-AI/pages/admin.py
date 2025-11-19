# admin.py

import streamlit as st
from database import get_all_users, delete_user, update_user_role

st.set_page_config(page_title="Admin Panel")

# If not logged in → login
if not st.session_state.get("logged_in", False):
    st.switch_page("pages/login.py")

user = st.session_state.get("user", {})
role = user.get("role", "user")

# Only admin can access this page
if role != "admin":
    st.error("❌ You are not authorized to access the Admin Panel.")
    st.page_link("pages/dashboard.py", label="🏠 Go to Dashboard")
    st.stop()

# UI
st.title("🛠 Admin Panel")
st.caption("Manage all registered users")

st.markdown("---")

users = get_all_users()

if not users:
    st.info("No users found.")
else:
    st.subheader("👥 Registered Users")

    for u in users:
        col1, col2, col3 = st.columns([4, 2, 2])

        col1.write(f"**{u['name']}** ({u['email']}) — Role: `{u['role']}`")

        # DELETE USER
        if col2.button("🗑 Delete", key=f"del_{u['_id']}"):
            delete_user(u["email"])
            st.success(f"Deleted {u['email']}")
            st.rerun()

        # MAKE ADMIN
        if u["role"] != "admin":
            if col3.button("⭐ Make Admin", key=f"admin_{u['_id']}"):
                update_user_role(u["email"], "admin")
                st.success(f"{u['email']} is now Admin")
                st.rerun()
        else:
            col3.write("🟢 Already Admin")

st.markdown("---")

st.page_link("pages/dashboard.py", label="🏠 Dashboard")
st.page_link("pages/login.py", label="🔐 Logout")
