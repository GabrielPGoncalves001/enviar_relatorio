import streamlit as st

img = 'assets/cachorro_foda.png'

with open(img, "rb") as f:
  img_b = f.read()

st.download_button(
  label="CLIQUE AQUI IMEDIATAMENTE",
  data=img_b,
  file_name="carro.png",
  mime="image/png")
