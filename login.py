import streamlit as st
from streamlit_extras.switch_page_button import switch_page as sp
import json

from customs.custom import css
#로그인 전 사이드바 제거
st.set_page_config(initial_sidebar_state="collapsed")
st.markdown(css,unsafe_allow_html=True)
with open('C:\\Users\\USER\\ve_1\\proj_web\\db\\login.json', 'r') as f:
    home_login = json.load(f)
user_id = home_login['ms']['id']
user_pw = home_login['ms']['pw']

with st.form("login"):
    id = st.text_input("id")
    pw = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")
if submit and id==user_id and pw==user_pw:
    sp("IlIllIlI")
elif submit and id!=user_id and pw!=user_pw:
    st.error("Login failed")
else:
    pass