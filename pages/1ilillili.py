import pandas as pd
import json

import streamlit as st
from streamlit_autorefresh import st_autorefresh
from streamlit_extras.row import row
from streamlit_extras.switch_page_button import switch_page as sp

from customs.custom import css
#상단 빈칸제거 및 사이드바 제거
st.markdown(css,unsafe_allow_html=True)
#캐싱-info DB 12시간마다 갱싱
@st.cache_data(ttl=43200)
def data():
    DF = pd.read_json('C:\\Users\\USER\\ve_1\\proj_web\\db\\info_.json',
                      orient='records',
                      dtype={'mid':str,'info':str,'char':str})
    return DF
#실시간 알람 불러오기
with open('C:\\Users\\USER\\ve_1\\proj_web\\db\\Alarm_.json','r',encoding="UTF-8") as f:
    A_df = json.load(f)
for i in range(11):
    if A_df[i]['mid'] not in data()['mid'].to_list():
        A_df[i]['mid'] = "확인필요"
    else:
        pass
#자동 새로고침 코드
count = st_autorefresh(interval=3000,
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
    if row_.button("은행지연/모계좌", use_container_width=True):
        sp("iillliiilll")
    if count:
        with st.expander("은행지연/모계좌"):
            notice= open("C:\\Users\\USER\\ve_1\\proj_web\\db\\notice.txt",
                        mode="r",
                        encoding="utf-8",
                        closefd=True)
            st.write(notice.read())
            notice.close()
        st.write(A_df[-1]['Alarm'])
        st.write(A_df[-1]['mid'])
        st.markdown(':blue[**정보**]')
        st.write(data().loc[data()['mid']==A_df[-1]['mid']]['info'].to_list()[0])
        st.markdown(':blue[**담당자**]')
        st.write(data().loc[data()['mid']==A_df[-1]['mid']]['char'].to_list()[0])
        st.divider()
        st.write(A_df[-2]['Alarm'])
        st.write(A_df[-2]['mid'])
        st.markdown(':blue[**정보**]')
        st.write(data().loc[data()['mid']==A_df[-2]['mid']]['info'].to_list()[0])
        st.markdown(':blue[**담당자**]')
        st.write(data().loc[data()['mid']==A_df[-2]['mid']]['char'].to_list()[0])
        st.divider()
        st.write(A_df[-3]['Alarm'])
        st.write(A_df[-3]['mid'])
        st.markdown(':blue[**정보**]')
        st.write(data().loc[data()['mid']==A_df[-3]['mid']]['info'].to_list()[0])
        st.markdown(':blue[**담당자**]')
        st.write(data().loc[data()['mid']==A_df[-3]['mid']]['char'].to_list()[0])
        st.divider()
        st.write(A_df[-4]['Alarm'])
        st.write(A_df[-4]['mid'])
        st.markdown(':blue[**정보**]')
        st.write(data().loc[data()['mid']==A_df[-4]['mid']]['info'].to_list()[0])
        st.markdown(':blue[**담당자**]')
        st.write(data().loc[data()['mid']==A_df[-4]['mid']]['char'].to_list()[0])
        st.divider()
        st.write(A_df[-5]['Alarm'])
        st.write(A_df[-5]['mid'])
        st.markdown(':blue[**정보**]')
        st.write(data().loc[data()['mid']==A_df[-5]['mid']]['info'].to_list()[0])
        st.markdown(':blue[**담당자**]')
        st.write(data().loc[data()['mid']==A_df[-5]['mid']]['char'].to_list()[0])
        st.divider()
        st.write(A_df[-6]['Alarm'])
        st.write(A_df[-6]['mid'])
        st.markdown(':blue[**정보**]')
        st.write(data().loc[data()['mid']==A_df[-6]['mid']]['info'].to_list()[0])
        st.markdown(':blue[**담당자**]')
        st.write(data().loc[data()['mid']==A_df[-6]['mid']]['char'].to_list()[0])
        st.divider()
        st.write(A_df[-7]['Alarm'])
        st.write(A_df[-7]['mid'])
        st.markdown(':blue[**정보**]')
        st.write(data().loc[data()['mid']==A_df[-7]['mid']]['info'].to_list()[0])
        st.markdown(':blue[**담당자**]')
        st.write(data().loc[data()['mid']==A_df[-7]['mid']]['char'].to_list()[0])
        st.divider()
        st.write(A_df[-8]['Alarm'])
        st.write(A_df[-8]['mid'])
        st.markdown(':blue[**정보**]')
        st.write(data().loc[data()['mid']==A_df[-8]['mid']]['info'].to_list()[0])
        st.markdown(':blue[**담당자**]')
        st.write(data().loc[data()['mid']==A_df[-8]['mid']]['char'].to_list()[0])
        st.divider()
        st.write(A_df[-9]['Alarm'])
        st.write(A_df[-9]['mid'])
        st.markdown(':blue[**정보**]')
        st.write(data().loc[data()['mid']==A_df[-9]['mid']]['info'].to_list()[0])
        st.markdown(':blue[**담당자**]')
        st.write(data().loc[data()['mid']==A_df[-9]['mid']]['char'].to_list()[0])
        st.divider()
        st.write(A_df[-10]['Alarm'])
        st.write(A_df[-10]['mid'])
        st.markdown(':blue[**정보**]')
        st.write(data().loc[data()['mid']==A_df[-10]['mid']]['info'].to_list()[0])
        st.markdown(':blue[**담당자**]')
        st.write(data().loc[data()['mid']==A_df[-10]['mid']]['char'].to_list()[0])
        st.divider()

H_page()