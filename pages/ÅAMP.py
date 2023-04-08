import streamlit as st
import webbrowser

with open("style.css") as source_des:
        st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)

#beløb = 10
#c1,c2,c3 = st.columns(3)

#c1.metric(label="Hej", value = beløb, delta= beløb)
#style_metric_cards(border_left_color="#1E1E1E")

st.title("ÅbenAlleMineProgrammer")

# Text input for URL
url_input = "https://www.youtube.com/watch?v=FOULV9Xij_8&ab_channel=CodingIsFun"

#1. test om den kan åbne Onescreen og veris gennem VPN
#2. lav checkbox for at filtrere hvilke hjemmesider der skal åbnes.

sider = st.multiselect("Hvilke sider skal åbnes?..", 
                       ['Veris', 'OneScreen', 'Rubix'])

knap_clicked = st.button("Åbn hjemmesid(er)")   

if "Rubix" in sider and knap_clicked:
    webbrowser.open_new_tab("https://rubix.rezponz.dk/default_login.asp")
if "Veris" in sider and knap_clicked:
    webbrowser.open_new_tab("https://github.com/victoryhb/streamlit-option-menu")
if "OneScreen" in sider and knap_clicked:
    webbrowser.open_new_tab("https://www.w3schools.com/howto/howto_css_contact_form.asp")

