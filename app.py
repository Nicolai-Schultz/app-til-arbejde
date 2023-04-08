import streamlit as st

st.title("Hello World!")


vægt = st.number_input("Enter your weight in KGs")

højde = st.number_input("Enter your height in CMs")

bmi = vægt / ((højde/100) ** 2)

if(st.button("udregn")):
    st.text("Dit BMI index er {}".format(bmi))

if(bmi < 16):
        st.error("You are Extremely Underweight")
elif(bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
elif(bmi >= 18.5 and bmi < 25):
        st.success("Healthy")
elif(bmi >= 25 and bmi < 30):
        st.warning("Overweight")
elif(bmi >= 30):
        st.error("Extremely Overweight")

pris = st.number_input("skriv pris på abonnement")

date_1 = st.date_input("skriv startdato") 
date_2 = st.date_input("skriv slutdato")

ab_pris = pris/30.44
delta = date_2 - date_1
num_days = delta.days  # Number of days between start and end date
num_seconds = delta.total_seconds()  # Number of seconds between start and end date
udregning = num_days * ab_pris

if(st.button("beregn")):
    st.write("Udregningen er", udregning)
    
    
    
    #st.write(f"Number of days between {start_date} and {end_date}: {num_days}")
    #st.write(f"Number of seconds between {start_date} and {end_date}: {num_seconds}")



#else:
 #   st.error("Error: End date must be after start date.")


