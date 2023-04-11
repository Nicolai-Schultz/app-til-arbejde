import streamlit as st
from streamlit_option_menu import option_menu

with open("style.css") as source_des:
        st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)

#Redirect til kreditmaks hjælp side, path virker ikke.
#if st.button('Go to another file'):
   # subprocess.Popen("/Users/nicolaischultz/streamlit_forsøg/KPT_udregner.py")

st.header("Velkommen til Kreditmaksudregneren!")

#navbar


selected = option_menu(
        menu_title = None,
        options = ["Kreditmaksudregner", "Hjælp til kreditmaks"],
        icons = ["pencil-fill", "bar-chart-fill"],
        orientation = "horizontal",
)

if selected == "Kreditmaksudregner":
        kredit_input = st.number_input("Hvad er kundens kreditmaks?", step=1000.0)
        beløb_input = st.number_input("Indsæt det totale beløb der er årsag til kreditmaks-spærringen.", step=1000.0)
        udregning = beløb_input - (kredit_input*0.8)+1
        formatted_string = "{:.2f}".format(udregning)

        if(kredit_input < beløb_input):
                st.success(f"Kunden skal indbetale {udregning:.2f} for at deres abonnementer kan genåbnes.")
                st.write(f"Kopier følgende beskrivelse med udregning ind i loggen: Kunde ringer angående spærring, hvilket er grundet overskridelse af kreditmaks. Informerer at kunde skal indbetale ({beløb_input:.2f} kr - ({kredit_input:.2f} kr * 0.8) + 1 kr = {udregning:.2f} kr), således deres abonnementer genåbnes.")
        elif kredit_input > beløb_input:
                st.warning("Hvis ikke skyldige beløb overskrider kreditmaks, er dette ikke årsag til spærring.")


if selected == "Hjælp til kreditmaks":
        st.header("Spørgsmål til kreditmaks.")

        st.subheader("Hvad er kreditmaks?")
        st.write("Kreditmaks er en grænse Telenor sætter sine kunder, baseret på en kreditvurdering af personen/selskabet. Hvis denne øvre grænse, for hvor meget kunden må skylde Telenor, overskrides spærres kunden indtil mere end 20% af kreditmaksen er indbetalt.")

        st.subheader("Hvad skal jeg bede kunden gøre?")
        st.write("Kunden skal betale mere end 20% af den samlede kreditmaks for at genåbne sine abonnementer. For at undgå spildtid, kan udregningen foregå via. kreditmaksudregneren på denne hjemmeside hvis link er nedenfor. Hvis ikke kunden har overskredet kreditmaks er vedkommende ikke spærret af denne årsag. Tjek derfor suspension/resumption under 'detail' på det pågældende abonnement for at se årsag. Hvis kunden ønsker at HÆVE sin kreditmaks skal kredit kontaktes - dog kun hvis der ikke er et udestående beløb på kundens konto!")

        st.subheader("Hvordan findes beløbet der er årsag til spærring?")
        st.write("Det totale udestående beløb er ikke at finde på kundens konto, da det ikke registreres som unbilled efter d. 11 på erhverv og d. 16. på privat. Man kan derfor finde det under 'Notifications' under den pågældende konto, da beløbet er sendt til kunden som SMS. ")

        st.subheader("Hvornår sparres der med kredit?")
        st.write("Sparring med kredit kan opsøges hvis ikke kunden har mulighed for at indbetale beløbet. Oftest hæver kredit blot kreditmaksen - OBS. hvis beløbet der er årsag til spærringen er udestående (skyldigt) hæver kredit ikke kreditmaksen!")
