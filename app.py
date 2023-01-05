import streamlit as st 
import pandas as pd


st.title('수학클리닉:blue[🞧]필요와충분')

st.header('정답제출 시험 시스템')

stu_name = st.text_input('*:blue[이름]을 입력하세요: ', '홍길동')
st.write('현재 응시자는 '+stu_name+'입니다')

test_num = st.text_input('*:red[시험지코드]를 입력하세요 ', '0001')
st.write('현재 시험지는 '+test_num+'입니다')

num = 0
ans = []
test_list = {'문항번호':num, '학생답':ans}

df = pd.DataFrame(test_list)

if st.button('1'):
    num = num+1
    ans.append(1)
    st.dataframe(df)


