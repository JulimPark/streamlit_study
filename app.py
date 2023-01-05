import streamlit as st 
import pandas as pd


st.title('수학클리닉:blue[🞧]필요와충분')

st.header('실전연습용 시험 시스템')

stu_name = st.text_input('*이름을 입력하세요: ', '홍길동')
st.write('현재 응시자는 '+stu_name+'입니다')

uploaded_file = st.file_uploader("응시할 시험지를 업로드하세요.")
# if uploaded_file is not None:
#     # To read file as bytes:
#     bytes_data = uploaded_file.getvalue()
#     st.write(bytes_data)

#     # To convert to a string based IO:
#     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
#     st.write(stringio)

#     # To read file as string:
#     string_data = stringio.read()
#     st.write(string_data)

#     # Can be used wherever a "file-like" object is accepted:
#     dataframe = pd.read_csv(uploaded_file)
#     st.write(dataframe)


def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)


if st.button('시험지 보기'):
    show_pdf(uploaded_file)
else:
    st.write('버튼을 클릭하세요')



