import pandas as pd
from datetime import datetime

import streamlit as st
from streamlit_autorefresh import st_autorefresh
from streamlit_extras.row import row
from streamlit_extras.switch_page_button import switch_page as sp

from customs.custom import css
#상단 빈칸제거 및 사이드바 제거
st.markdown(css,unsafe_allow_html=True)
#RM한도 적용 날짜
now = datetime.now().strftime('%Y년 %m월')
#캐싱-info DB 10분마다 갱싱
@st.cache_data(ttl=600)
def data():
    DF = pd.read_json('C:\\Users\\USER\\ve_1\\proj_web\\db\\info_.json',
                    orient='records',
                    dtype={'mid':str,'info':str,'char':str})
    return DF
#캐싱-RM한도증액 가맹점 5시간마다 갱신
@st.cache_data(ttl=18000)
def RM():
    RM = pd.read_json('C:\\Users\\USER\\ve_1\\proj_web\\db\\RM_.json',
                        orient='records',
                        dtype={'mid':str,'name':str,'month':str})
    RM_ = RM[RM['month']==now]
    return RM_[["mid","name"]]
#실시간 알람 불러오기
A_df = pd.read_json("C:\\Users\\USER\\ve_1\\proj_web\\db\\Alarm_.json",
                    orient='records',
                    dtype={'Alarm':str,'mid':str})
#자동 새로고침 코드
count = st_autorefresh(interval=2000,
                        limit=None,
                        key="refresh")
#네비게이터 버튼 'ilillili', 'lliilliill', 'iillilill', 'iillliiilll'
def H_page():
    row_ = row(4, vertical_align="top")
    row_.button("모니터링", use_container_width=True)
    if row_.button("조회", use_container_width=True):
        sp("lliilliill")
    if row_.button("DB관리", use_container_width=True):
        sp("iillilill")
    if row_.button("RM증액 및 공지", use_container_width=True):
        sp("iillliiilll")
    if count != 0:
        cul1,cul2 = st.columns(2)
        with cul1:
            with st.expander(f"{now} RM 한도 증액 가맹점"):
                st.dataframe(RM())
        with cul2:
            with st.expander("공지"):
                notice= open("C:\\Users\\USER\\ve_1\\proj_web\\db\\notice.txt",
                            mode="r",
                            encoding="utf-8",
                            closefd=True)
                st.write(notice.read())
                notice.close()
        Al = A_df.loc[::-1].head(10)
        call = pd.merge(Al,data(),how='left',left_on='mid',right_on='mid')
        st.write(call['Alarm'][0])
        st.write(call['mid'][0])
        st.markdown(':blue[**정보**]')
        st.write(call['info'][0])
        st.markdown(':blue[**담당자**]')
        st.write(call['char'][0])
        st.divider()
        st.write(call['Alarm'][1])
        st.write(call['mid'][1])
        st.markdown(':blue[**정보**]')
        st.write(call['info'][1])
        st.markdown(':blue[**담당자**]')
        st.write(call['char'][1])
        st.divider()
        st.write(call['Alarm'][2])
        st.write(call['mid'][2])
        st.markdown(':blue[**정보**]')
        st.write(call['info'][2])
        st.markdown(':blue[**담당자**]')
        st.write(call['char'][2])
        st.divider()
        st.write(call['Alarm'][3])
        st.write(call['mid'][3])
        st.markdown(':blue[**정보**]')
        st.write(call['info'][3])
        st.markdown(':blue[**담당자**]')
        st.write(call['char'][3])
        st.divider()
        st.write(call['Alarm'][4])
        st.write(call['mid'][4])
        st.markdown(':blue[**정보**]')
        st.write(call['info'][4])
        st.markdown(':blue[**담당자**]')
        st.write(call['char'][4])

H_page()