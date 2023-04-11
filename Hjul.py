import streamlit as st

html_code = '''
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>
<body>
	<button id="spin">Spin</button>
	<span class="arrow"></span>
	<div class="container">
		<div class="one">1</div>
		<div class="two">2</div>
		<div class="three">3</div>
		<div class="four">4</div>
		<div class="five">5</div>
		<div class="six">6</div>
		<div class="seven">7</div>
		<div class="eight">8</div>
	</div>
</body>
</html>
'''

st.markdown(html_code, unsafe_allow_html=True)

js_code = """
let container = document.querySelector(".container");
let btn = document.getElementById("spin");
let number = Math.ceil(Math.random() * 1000);

let clicks = 0;
btn.onclick = function () {
  clicks += 1;
  if(clicks == 1 ){
	container.style.transform = "rotate(" + number + "deg)";
	number += Math.ceil(Math.random() * 1000);
  }
}
"""

# Render the JavaScript code using st.markdown()
st.markdown(f"<script>{js_code}</script>", unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")



with open("style.css") as source_des:
        st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)
