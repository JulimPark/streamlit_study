import streamlit as st 
import pandas as pd


st.title('수학클리닉:blue[🞧]필요와충분')

st.header('실전연습용 시험 시스템')

stu_name = st.text_input('*이름을 입력하세요: ', '홍길동')
st.write('현재 응시자는 '+stu_name+'입니다')