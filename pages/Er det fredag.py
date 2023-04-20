import streamlit as st
import datetime
with open("style.css") as source_des:
        st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)
# Get the current day of the week as an integer (Monday = 0, Sunday = 6)
today = datetime.datetime.today().weekday()
image_url_nej = "https://media.cnn.com/api/v1/images/stellar/prod/190517103414-01-grumpy-cat-file-restricted.jpg?q=x_435,y_327,h_1683,w_2244,c_crop"
image_url_ja = "https://image.nordjyske.dk/users/nordjyske/images/66480980.jpg?t[crop][width]=2560&t[crop][height]=1376&t[crop][x]=0&t[crop][y]=322&t[resize][width]=1024&t[resize][height]=550&t[strip]=true&t[quality]=75&accessToken=e0168e1881c6939688555bbefd73a5c202d4581ad1f4f089562184b196c0cfb6"
image_url_vip = "data:image/jpeg;base64,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"

if today == 4:  # Check if it's Friday (4 is the index for Friday)
    st.header("Ja tak, så er det sgu' fredag!")
    st.image(image_url_ja, use_column_width=True)
elif today == 2:
    st.header("Nej, det er sgu' ikke fredag. Til gengæld er det vippedag!!!")
    st.image(image_url_vip, use_column_width=True)
else:
    st.header("Nej, det er sgu' ikke fredag. Hæng i!")
    st.image(image_url_nej, use_column_width=True)
    

