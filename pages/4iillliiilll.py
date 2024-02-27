import streamlit as st
from streamlit_extras.row import row
from streamlit_extras.switch_page_button import switch_page as sp

from customs.custom import css
#사이드바 제거
st.markdown(css, unsafe_allow_html=True)

#네비게이터 버튼 'ilillili', 'lliilliill', 'iillilill', 'iillliiilll'
row_ = row(4, vertical_align="top")
if row_.button("모니터링", use_container_width=True):
    sp("IlIllIlI")
if row_.button("조회", use_container_width=True):
    sp("llIIllIIll")
if row_.button("DB관리", use_container_width=True):
    sp("IIllIlill")
row_.button("은행지연/모계좌", use_container_width=True)

with st.form(key="은행지연/모계좌"):
    with open("C:\\Users\\USER\\ve_1\\proj_web\\db\\notice.txt","r+",encoding="utf-8") as f:
        notice: str = st.text_area("내용",value=f.read().replace("  \n","\n"),height=500)
        if st.form_submit_button("입력"):
            nf = open("C:\\Users\\USER\\ve_1\\proj_web\\db\\notice.txt","w+",encoding="utf-8")
            nf.write(notice.replace("\n","  \n"))
            nf.close()