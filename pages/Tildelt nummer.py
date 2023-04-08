import streamlit as st

with open("style.css") as source_des:
        st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)

st.title("Tildelt nummer udregner")


pris = st.number_input("Skriv pris på abonnement", step=10.0)

date_1 = st.date_input("Skriv startdato" ) 
date_2 = st.date_input("Skriv slutdato")

ab_pris = pris/30.42
#ab_2_pris = 30.42
delta = date_2 - date_1
num_days = delta.days  # Number of days between start and end date
num_seconds = delta.total_seconds()  # Number of seconds between start and end date
udregning = num_days * ab_pris

if(st.button("BEREGN")):
    formatted_string = "{:.2f}".format(udregning)
# format to two decimal places
    float_value = float(formatted_string)
    st.write(f"Følgende beløb skal krediteres: {float_value:.2f} kr")
    st.write(f"Kopier denne udregning i kreditnota-log: {num_days:.2f} dage * {pris:.2f} kr / 30,44 dage = {float_value:.2f} kr")
    st.warning("OBS: Erhvervskonsulenter. Har du husket at tilføje moms til abonnementspris? Hvis ikke skal du gange ovenstående resultat med 1.25.")
    



