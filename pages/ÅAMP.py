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
#url_input = "https://www.youtube.com/watch?v=FOULV9Xij_8&ab_channel=CodingIsFun"

#1. test om den kan åbne Onescreen og veris gennem VPN
#2. lav checkbox for at filtrere hvilke hjemmesider der skal åbnes.


#if "Veris" in sider and knap_clicked:
   # webbrowser.open_new_tab("https://github.com/victoryhb/streamlit-option-menu")
#if "OneScreen" in sider and knap_clicked:
   # webbrowser.open_new_tab("https://www.w3schools.com/howto/howto_css_contact_form.asp")

# TODO lav en multiselect hvor man kan bestemme hvilke links der skal vises

links = {
    "Rubix": "https://rubix.rezponz.dk/default_login.asp",
    "OSE": "https://login.microsoftonline.com/1676489c-5c72-46b7-ba63-9ab90c4aad44/oauth2/v2.0/authorize?client_id=2c777776-6551-48b6-be94-d3515b9d9e65&redirect_uri=https%3A%2F%2Finternal-ose-epi.prod.telenor.eu%2Fagent-view%2Flogin%2FCallback%2F&response_mode=form_post&response_type=id_token&scope=openid+profile&nonce=3b1430b6-fdc5-4cb4-bded-4fcf4afed441&state=%252fagent-view%252f",
    "Outlook": "https://outlook.office.com/mail/",
    "Køoversigt": "https://ivabtweb01/rtd/",
    "Callback klient": "http://ivabpurect01/book/index.html",
    "Antal kald pr. dag": "http://ivabccr04/Reports/report/Customer/Calls%20per%20employee",
    "Klartid": "https://klartid.nu/login.asp",
}
label = "Open links"

sider = st.multiselect("Hvilke sider skal åbnes?..", 
                      ["Vis links til alle programmer",'Rubix', 'OneScreen', 'Outlook', "Køoversigt", "Callback klient", "Antal kald pr. dag", "Klartid"])  

if "Vis links til alle programmer" in sider:
   for name, link in links.items():
        st.markdown(f"[{name}]({link})", unsafe_allow_html=True)
if "Rubix" in sider:
        st.markdown(f"[Rubix]({links['Rubix']})", unsafe_allow_html=True)
if "OneScreen" in sider:
        st.markdown(f"[OSE]({links['OSE']})", unsafe_allow_html=True)
if "Outlook" in sider:
        st.markdown(f"[Outlook]({links['Outlook']})", unsafe_allow_html=True)
if "Køoversigt" in sider:
        st.markdown(f"[Køoversigt]({links['Køoversigt']})", unsafe_allow_html=True)
      
if "Callback klient" in sider:
        st.markdown(f"[Callback klient]({links['Callback klient']})", unsafe_allow_html=True)
if "Antal kald pr. dag" in sider:
        st.markdown(f"[Antal kald pr. dag]({links['Antal kald pr. dag']})", unsafe_allow_html=True)
if "Klartid" in sider:
        st.markdown(f"[Klartid]({links['Klartid']})", unsafe_allow_html=True)



# Create a button that opens all the links when clicked
#if st.button(label):
    


