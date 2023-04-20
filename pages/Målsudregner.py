import streamlit as st

with open("style.css") as source_des:
        st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)
#TODO Lav alle disse kategorier i dropdown i stedet, og hav en mulighed der hedder vælg alle som blot er standard layout.
st.title("Velkommen til KPT- og målsudregneren!")
st.subheader("Her kan du udregne mængden af kald du skal tage i dag.")
timer = (st.number_input("Hvor lang er din vagt i dag?", step = 0.25, value=7.5)-0.5)
mål_kald = st.number_input("Hvad er dit KPT mål i dag?", step = 0.25, value = 7.5)
udregning_kpt = round(timer * mål_kald)

if(timer != ""):
        st.success(f"Med dette mål skal du tage: {udregning_kpt} kald i dag!")

st.subheader("Her kan du udregne mængden af salg du skal lave for at opnå dit GA% mål.")
mål_salg = st.number_input("Hvad er dit GA% mål i dag? (angivet i procent)", step = 0.25, value= 2.5)
antal_kald = st.number_input("Hvor mange kald har du taget i dag?", step = 1, value= 1)

salg_til_opnået = (antal_kald * mål_salg)/100

if(mål_salg != ""):
        st.success(f"Du skal sælge ca. {salg_til_opnået:.2f} genstande for at opnå dit mål i dag!")

st.subheader("Her kan du udregne din GA%.")
mål_salg_tal_input = (st.number_input("Hvor mange genstande har du solgt i dag? Dette mål afhænger af antal kald og salg.", step = 1, value=1))
mål_salg_tal = (mål_salg_tal_input / antal_kald)*100

if (mål_salg_tal_input !=""):
        st.success(f"Din GA% er derfor: {mål_salg_tal:.2f}%")

