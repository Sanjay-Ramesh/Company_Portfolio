import streamlit as st
from send_email import send_email

st.header("Contact Us")

with st.form(key="email_forum"):
    user_email = st.text_input("Your Email Address")
    selectionbox = st.selectbox("Select an Option", ["Job Inquires", "Project Proposals", "Others"])
    row_message = st.text_area("Your Message")
    message = f"""\
Subject: New Email from {user_email}

From: {user_email}
Topic: {selectionbox}
{row_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was Sent Successfully")