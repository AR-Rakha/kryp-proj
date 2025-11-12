import streamlit as st

st.set_page_config(
   page_title="",
   page_icon="👨‍💻",
   layout="wide",
   initial_sidebar_state="expanded",
)

main = st.Page("main.py", title="Forside") # Creates a page with the main.py as its contents
ekrypt = st.Page("Krypt.py", title="Vigenère kryptering") # Creates a page with other.py as its contents
dkrypt = st.Page("Dekrypt.py", title="Vigenère dekryptering") # Creates a page with other.py as its contents


pg = st.navigation([main,ekrypt,dkrypt]) # Creates a side-navigation bar
pg.run() # Runs the side-navigation bar