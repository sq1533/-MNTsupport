import requests
import json
import pandas as pd

import streamlit as st
from streamlit_extras.row import row
from streamlit_extras.switch_page_button import switch_page as sp

from customs.custom import css
#사이드바 제거
st.markdown(css, unsafe_allow_html=True)
DF = pd.read_json('C:\\Users\\USER\\ve_1\\proj_web\\db\\info_.json',
                orient='records',
                dtype={'mid':str,'info':str,'char':str})

url = "http://127.0.0.1:8000/mk_info"
url_d = "http://127.0.0.1:8000/mk_info_d"
def create():
    requests.post(url,json.dumps(mk_info))
def change():
    requests.put(url,json.dumps(mk_ch))
def delete():
    requests.post(url_d,json.dumps(mk_d))

mid_L = DF['mid'].to_list()
#네비게이터 버튼 'ilillili', 'lliilliill', 'iillilill', 'iillliiilll'
row_ = row(4, vertical_align="top")
if row_.button("모니터링", use_container_width=True):
    sp("IlIllIlI")
if row_.button("조회", use_container_width=True):
    sp("llIIllIIll")
row_.button("DB관리", use_container_width=True)
if row_.button("RM증액 및 공지", use_container_width=True):
    sp("iilllIIIlll")

tab1,tab2,tab3 = st.tabs(["생성","수정","삭제"])

with tab1:
    with st.form(key="mk_info"):
        mid: str = st.text_input("mid", max_chars=20)
        info: str = st.text_area("info")
        char: str = st.text_area("char")
        mk_info = {
            "mid":mid,
            "info":info.replace('\n','  \n'),
            "char":char.replace('\n','  \n')
        }
        btn = st.form_submit_button(label="생성")
        if btn:
            if mk_info["mid"] not in mid_L:
                create()
                st.markdown("생성완료")
            else:
                st.markdown("MID가 이미 존재합니다.")

with tab2:
    with st.form(key="mk"):
        mid: str = st.text_input("mid", max_chars=20)
        mk = {
            "mid":mid
        }
        btn_1 = st.form_submit_button(label="조회")
        if btn_1:
            if mk["mid"] not in mid_L:
                st.markdown("MID가 존재하지 않습니다.")
    with st.form(key="mk_ch"):
        mid: str = st.text_input("mid",DF[DF["mid"]==mk["mid"]]["mid"].to_string(index=False),max_chars=20)
        info: str = st.text_area("info(수정 전 info는 지워주세요)",DF[DF["mid"]==mk["mid"]]["info"].to_markdown(index=False,tablefmt="plain"),height=250)
        char: str = st.text_area("char(수정 전 char는 지워주세요)",DF[DF["mid"]==mk["mid"]]["char"].to_markdown(index=False,tablefmt="plain"),height=100)
        mk_ch = {
            "mid":mid,
            "info":info.replace('\n','  \n'),
            "char":char.replace('\n','  \n')
        }
        btn_2 = st.form_submit_button(label="수정")
        if btn_2:
            if mk["mid"] not in mid_L:
                st.markdown("MID가 존재하지 않습니다.")
            else:
                change()
                st.markdown("수정완료")
with tab3:
    with st.form(key="mk_d"):
        mid: str = st.text_input("mid", max_chars=20)
        mk_d = {
            "mid":mid
        }
        btn = st.form_submit_button(label="삭제")
        if btn:
            if mk_d["mid"] not in mid_L:
                st.markdown("MID가 존재하지 않습니다.")
            else:
                delete()
                st.markdown("삭제완료")