# Core Pkgs
import streamlit as st 

# Utils Pkgs
import codecs

# Components Pkgs
import streamlit.components.v1 as components

# Custom Components Fxn
def st_calculator(calc_html,width=700,height=500):
	calc_file = codecs.open(calc_html,'r')
	page = calc_file.read()
	components.html(page,width=width,height=height,scrolling=False)


def main():
    st.subheader("Simple Calculator")
    st_calculator('calculator.html')


if __name__ == '__main__':
	main()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")



with open("style.css") as source_des:
        st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)
