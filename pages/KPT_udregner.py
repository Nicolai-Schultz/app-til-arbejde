import streamlit as st

with open("style.css") as source_des:
        st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)

st.title("Velkommen til KPT- og målsudregneren!")

kald = st.number_input("Indsæt antal kald her:", step = 10, value=1)
timer = st.number_input("Hvor lang er din vagt i dag?", step = 0.25, value=7.5)
udregning_kpt = kald/timer

if(kald == 0):
        st.warning("Antal kald og timer skal oplyses!")

if(timer == 0):
        st.warning("Antal kald og timer skal oplyses!")

if(kald != ""):
        st.write(f"Din KPT er indtil videre: {udregning_kpt:.2f}")

mål = st.number_input("Hvad er dit KPT mål i dag?", step = 0.5, value=7.5)
mål_salg = st.number_input("Hvad er dit GA% mål i dag? (angivet i procent)", step = 0.25, value= 2.5)
kald_til_opnået = round(mål * timer)
salg_til_opnået = round((kald_til_opnået * mål_salg)/100)

if(st.button("beregn")):
        st.write(f"Du skal sælge {salg_til_opnået} genstand(e) for at opnå dit mål i dag! Derudover, skal du tage {kald_til_opnået} kald for at opnå dit kaldsmål i dag!")
