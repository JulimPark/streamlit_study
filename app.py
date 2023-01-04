
import streamlit as st
import pandas as pd


a = [100,300,50]
st.bar_chart(a)
b = [1,2,3]

st.bar_chart(b)

c= [4,5,6]
jj = {'a':a, 'b':b,'c':c}

out = pd.DataFrame(jj)

st.bar_chart(c)
st.write('this is mouth')
st.write('Hello **world**!')
st.write(out)

st.markdown('Streamlit is **_really_ cool**.')
st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")