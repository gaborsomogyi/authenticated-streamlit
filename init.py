import streamlit as st
import streamlit_authenticator as stauth

from app import show_data

st.set_page_config(layout="wide")

names = ['Test User']
usernames = ['test',]
hashed_passwords = ['$2b$12$vdrqRxZm6myxbJKOKFYCsekFuEuyY74.lzJ0ngb.Eu67X9byQwAAq']

authenticator = stauth.authenticate(names,usernames,hashed_passwords,
    'some_cookie_name','some_signature_key',cookie_expiry_days=30)
name, authentication_status = authenticator.login('Login','main')

if authentication_status:
    show_data()

elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')