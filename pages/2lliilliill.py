import json

import streamlit as st
from streamlit_extras.row import row
from streamlit_extras.switch_page_button import switch_page as sp

from customs.custom import css
#사이드바 제거
st.markdown(css, unsafe_allow_html=True)

#실시간 알람 불러오기
with open('C:\\Users\\USER\\ve_1\\proj_web\\db\\info_.json','r',encoding="UTF-8") as f:
    DF = json.load(f)
#네비게이터 버튼 'ilillili', 'lliilliill', 'iillilill', 'iillliiilll'
row_ = row(4, vertical_align="top")
if row_.button("모니터링", use_container_width=True):
    sp("IlIllIlI")
row_.button("조회", use_container_width=True)
if row_.button("DB관리", use_container_width=True):
    sp("IIllIlill")
if row_.button("은행지연/모계좌", use_container_width=True):
    sp("iilllIIIlll")

mid = st.text_input("MID조회(입력 후 Enter)")
look = [i for i in range(len(DF)) if DF[i]['mid']==mid]

if mid:
    if look != []:
        st.markdown(':blue[**정보**]')
        st.write(DF[look[0]]['info'])
        st.markdown(':blue[**담당자**]')
        st.write(DF[look[0]]['char'])
    else:
        st.write('존재하지 않는 MID입니다.')