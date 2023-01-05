import streamlit as st 
import pandas as pd

test_code = pd.read_csv('test_code.csv')
st.write(test_code['시험지코드'][3])

st.title('수학클리닉:blue[🞧]필요와충분')

st.header('정답제출 시험 시스템')

stu_name = st.text_input('*:blue[이름]을 입력하세요: ', '홍길동')
st.write('현재 응시자는 '+stu_name+'입니다')

test_num = st.text_input('*:red[시험지코드]를 입력하세요 ', '0001')
st.write('현재 시험지는 '+test_num+'입니다')

st.write(test_code['시험지코드']==test_num)
st.write(test_code.index[(test_code['시험지코드']==test_num)])



question_num = st.text_input(':green[문항 수]를 입력하세요', 5)
st.write('문항 수는 '+question_num+'문항 입니다')



# no1 = st.radio(
#     '1번 문항의 정답을 입력하세요.',('1','2','3','4','5')
# )
# st.write(no1)

no=[]
for i in range(0, int(question_num)):
    ns = 'no'+str(i)
    no.append(ns)

st.write(no)
for i in range(0, int(question_num)):
    no[i] = st.radio(str(i+1)+'번 문항의 정답을 입력하세요.',('1','2','3','4','5'))
    st.write(no[i])