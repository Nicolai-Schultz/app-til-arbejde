import streamlit as st

with open("style.css") as source_des:
        st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)

st.header("Spørgsmål til kreditmaks.")

st.subheader("Hvad er kreditmaks?")
st.write("Kreditmaks er en grænse Telenor sætter sine kunder, baseret på en kreditvurdering af personen/selskabet. Hvis denne øvre grænse, for hvor meget kunden må skylde Telenor, overskrides spærres kunden indtil mere end 20% af kreditmaksen er indbetalt.")

st.subheader("Hvad skal jeg bede kunden gøre?")
st.write("Kunden skal betale mere end 20% af den samlede kreditmaks for at genåbne sine abonnementer. For at undgå spildtid, kan udregningen foregå via. kreditmaksudregneren på denne hjemmeside hvis link er nedenfor. Hvis ikke kunden har overskredet kreditmaks er vedkommende ikke spærret af denne årsag. Tjek derfor suspension/resumption under 'detail' på det pågældende abonnement for at se årsag. Hvis kunden ønsker at HÆVE sin kreditmaks skal kredit kontaktes - dog kun hvis der ikke er et udestående beløb på kundens konto!")

st.markdown('<a href="/Kreditmaks" target="_self">Tryk her for at tilgå kreditmaksudregneren!</a>', unsafe_allow_html=True)

st.subheader("Hvordan findes beløbet der er årsag til spærring?")
st.write("Det totale udestående beløb er ikke at finde på kundens konto, da det ikke registreres som unbilled efter d. 11 på erhverv og d. 16. på privat. Man kan derfor finde det under 'Notifications' under den pågældende konto, da beløbet er sendt til kunden som SMS. ")

st.subheader("Hvornår sparres der med kredit?")
st.write("Sparring med kredit kan opsøges hvis ikke kunden har mulighed for at indbetale beløbet. Oftest hæver kredit blot kreditmaksen - OBS. hvis beløbet der er årsag til spærringen er udestående (skyldigt) hæver kredit ikke kreditmaksen!")
