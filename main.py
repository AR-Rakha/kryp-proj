import streamlit as st

st.set_page_config(
   page_title="Main",
   page_icon="👨‍💻",
   layout="wide",
   initial_sidebar_state="expanded",
)

st.title("Vigenère kryptering og dekryptering") #st.title creates a title, for the current page. It can be any datatype. Parameters: st.title(body, anchor=None, *, help=None, width="stretch")
   
Text=st.write("Af Abdulrahman og Nikolai")