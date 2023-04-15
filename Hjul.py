import streamlit as st
from mycomponent import mycomponent
value = mycomponent(my_input_value="hello there")
st.write("Received", value)

html_code = '''
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>
<body>

</body>
</html>
'''

st.markdown(html_code, unsafe_allow_html=True)

js_code = """

"""

# Render the JavaScript code using st.markdown()
st.markdown(f"<script>{js_code}</script>", unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")



with open("style.css") as source_des:
        st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)
