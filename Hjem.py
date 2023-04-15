import streamlit as st

st.set_page_config(page_title="Helpr", page_icon=":tada", layout="wide")

with open("style.css") as source_des:
        st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)

st.header("Velkommen til!")
st.subheader("Dette er en hjemmeside beregnet til at hjælpe dig med at gøre dit arbejde som konsulent lettere.")
st.write("Start med at udforske menuen til venstre. Tryk på pilen i venstre øverste hjørne for at komme i gang med at benytte hjemmesiden!")

st.text("Denne hjemmeside er lavet af Nicolai Schultz (NISCH)")