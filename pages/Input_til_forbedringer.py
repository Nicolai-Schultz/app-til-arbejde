import streamlit as st

st.header("Skriv en email med forbedringspunkter/ideer til appen!")


contact_form = """
<form action="https://formsubmit.co/nico@schultzzz.net" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Dit navn .." required>
     <input type="email" name="email" placeholder="Din email .." required>
     <textarea name="message" placeholder="Din besked skrives her .." required></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")



with open("style.css") as source_des:
        st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)

