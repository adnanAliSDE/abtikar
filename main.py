import streamlit as st

st.title("Abtikar- AI Tech articles")
st.sidebar.title('What type of articles you need today.')

i1=st.sidebar.text_input('Topic 1')
i2=st.sidebar.text_input('Topic 2')
i3=st.sidebar.text_input('Topic 3')

processBtn=st.sidebar.button('Show Articles')

if processBtn:
    st.write(i1)
    st.write(i2)
    st.write(i3)
