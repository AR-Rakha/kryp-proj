import streamlit as st
import streamlit.components.v1 as components
import pathlib

st.set_page_config(
   page_title="Main",
   page_icon="🖥️",
   layout="wide",
   initial_sidebar_state="expanded",
)


heightCanvas=600
widthCanvas=600

# Read the sketch.js file
sketch_path = pathlib.Path("sketch.js")
sketch_code = sketch_path.read_text()

dKrypt=""

kryptList="abcdefghijklmnopqrstuvxyzæøå"

def updateKrypt():
  global dKrypt
  dKrypt =""
  
  if not text or not text2:  # hvis en af dem er tom, gør ingenting
    return

  for tC in range(len(text)):
    cIndex=kryptList.find(text[tC].lower())
    kIndex=kryptList.find(text2[tC%len(text2)].lower())
    if cIndex !=-1 and kIndex !=-1:

      dKrypt+=kryptList[((cIndex-kIndex)%len(kryptList)-1)]
  
  dKryptText.write(dKrypt)



st.title("Vigenère dekryptering")

text=st.text_input("Krypteret Besked", value="", max_chars=20, placeholder="Indtast din tekst")
text2=st.text_input("Nøgle", value="", max_chars=20, placeholder="Indtast din tekst")


dKryptText=st.empty()

updateKrypt()
    
p5_code = f"""
<script src="https://cdn.jsdelivr.net/npm/p5@1.4.0/lib/p5.min.js"></script>
<script charset="UTF-8">let startText = "{text}";
let endText = "{dKrypt}";
{sketch_code}</script>
"""

components.html(p5_code, height=heightCanvas)

