
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
st.markdown('this text is :red[colored red], and this is :blue[colored pencil]')

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")