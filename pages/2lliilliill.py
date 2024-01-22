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
#네비게이터 버튼 'ilillili', 'lliilliill', 'iillilill', 'iillliiilll'
row_ = row(4, vertical_align="top")
if row_.button("모니터링", use_container_width=True):
    sp("IlIllIlI")
row_.button("조회", use_container_width=True)
if row_.button("DB관리", use_container_width=True):
    sp("IIllIlill")
if row_.button("RM증액 및 공지", use_container_width=True):
    sp("iilllIIIlll")

mid = st.text_input("MID조회(입력 후 Enter)")
if mid:
    st.markdown(':blue[**정보**]')
    st.markdown(DF[DF['mid']==mid]["info"].to_markdown(index=False,tablefmt="plain"))
    st.markdown(':blue[**담당자**]')
    st.markdown(DF[DF['mid']==mid]["char"].to_markdown(index=False,tablefmt="plain"))