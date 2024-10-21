import streamlit as st
import os

st.title("TGCF Web Interface")

# Load environment variable
password = os.getenv("PASSWORD", "Not Set")
st.write(f"Password: {password}")

st.write("TGCF is running...")

# Placeholder for future TGCF controls
if st.button("Run TGCF"):
    st.write("TGCF command executed!")

