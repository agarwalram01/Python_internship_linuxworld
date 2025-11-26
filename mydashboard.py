import streamlit as st

with st.sidebar:
    st.header('Settings Panel')
    # Ab iske andar ke saare items sidebar mein dikhenge
    option = st.selectbox(
        'Kaunsa option chunenge?',
        ('Option 1', 'Option 2', 'Option 3')
    )
    st.write('Chuna gaya option:', option)

st.write('Yeh text main page par dikhega.')