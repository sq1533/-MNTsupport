import pandas as pd
import json
import requests
from datetime import datetime

import streamlit as st
from streamlit_extras.row import row
from streamlit_extras.switch_page_button import switch_page as sp

from customs.custom import css
#사이드바 제거
st.markdown(css, unsafe_allow_html=True)
RM = pd.read_json('C:\\Users\\USER\\ve_1\\proj_web\\db\\RM_.json',
                    orient='records',
                    dtype={'mid':str,'name':str,'month':str})
now = datetime.now().strftime('%Y년 %m월')

url_RM = "http://127.0.0.1:8000/RM"
#네비게이터 버튼 'ilillili', 'lliilliill', 'iillilill', 'iillliiilll'
row_ = row(4, vertical_align="top")
if row_.button("모니터링", use_container_width=True):
    sp("IlIllIlI")
if row_.button("조회", use_container_width=True):
    sp("llIIllIIll")
if row_.button("DB관리", use_container_width=True):
    sp("IIllIlill")
row_.button("RM증액 및 공지", use_container_width=True)

def RM_inc():
    requests.post(url_RM,json.dumps(RM))
tab1,tab2 = st.tabs(["RM 한도 증액 가맹점","공지"])
with tab1:
    st.markdown(f"### {now} RM 한도증액 가맹점")
    with st.form(key="RM"):
        mid: str = st.text_input("한도증액 mid",max_chars=30)
        name: str = st.text_input("가맹점 이름",max_chars=30)
        RM = {
            "mid":mid,
            "name":name,
            "month":str(now)
        }
        btn = st.form_submit_button("생성")
        if btn:
            RM_inc()
            st.write("RM 증액")
with tab2:
    with st.form(key="공지"):
        with open("C:\\Users\\USER\\ve_1\\proj_web\\db\\notice.txt","r+",encoding="utf-8") as f:
            notice: str = st.text_area("내용",value=f.read(),height=500)
            if st.form_submit_button("입력"):
                nf = open("C:\\Users\\USER\\ve_1\\proj_web\\db\\notice.txt","w+",encoding="utf-8")
                nf.write(notice.replace("\n","  \n"))
                nf.close()