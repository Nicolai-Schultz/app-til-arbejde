import streamlit as st

with open("style.css") as source_des:
        st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)

st.title("Tildelt nummer udregner")
st.write("Beregneren kan også bruges til at udregne et hvilket som helst beløb over X antal dage: fx. hvis der skal krediteres for tidal i X dage, mobilforsikring, netsikker plus eller andet!")

#Main er inddelt i if sætninger - ændres der i én skal der ændres i alle. Ved ændringer, tryk ctrl + shift + l for at ændre lignende highligts samtidigt. 

def main():
        antal_ab = st.selectbox(
             "Hvor mange abonnementer er der tale om?",
             ('1','2','3','4','5'), format_func=int)
        
        if antal_ab == '1':
            pris = (st.number_input("Skriv pris på abonnement:", step=10.0))

            date_1 = st.date_input("Skriv startdato") 
            date_2 = st.date_input("Skriv slutdato")
            konst_måned = 30.42
            ab_pris = pris
            delta = date_2 - date_1
            num_days = delta.days  
            udregning = (num_days * ab_pris) / konst_måned
            
            #TODO lav en if else hvor hvis der trykkes på knap "Er der flere ab?", kreer nyt input felt og medregn dette. 
            beregn_knap = st.button("BEREGN")
            if(beregn_knap):
                if udregning == 0:
                    st.warning("Antal dage kan ikke være 0. Ændr start og slutdato for udregning.")
                else:
                    formatted_string = "{:.2f}".format(udregning)
                    float_value = float(formatted_string)
                    st.write(f"Følgende beløb skal krediteres: {float_value:.2f} kr")
                    st.write(f"Kopier denne udregning i kreditnota-log: ({num_days:.2f} dage * {ab_pris:.2f} kr) / 30,42 dage = {float_value:.2f} kr")
                    st.warning("OBS: Erhvervskonsulenter. Har du husket at tilføje moms til abonnementspris? Hvis ikke skal du gange ovenstående resultat med 1.25.")
        elif antal_ab == '2':
            pris = (st.number_input("Skriv pris på abonnement:", step=10.0))
            pris_2 = (st.number_input(f"Skriv pris på abonnement nr. {int(antal_ab)}:", step=10.0))

            date_1 = st.date_input("Skriv startdato") 
            date_2 = st.date_input("Skriv slutdato")
            konst_måned = 30.42
            ab_pris = (pris+pris_2) 
            delta = date_2 - date_1
            num_days = delta.days  
            udregning = (num_days * ab_pris) / konst_måned
            
            #TODO lav en if else hvor hvis der trykkes på knap "Er der flere ab?", kreer nyt input felt og medregn dette. 
            beregn_knap = st.button("BEREGN")
            if(beregn_knap):
                if udregning == 0:
                    st.warning("Antal dage kan ikke være 0. Ændr start og slutdato for udregning.")
                else:
                    formatted_string = "{:.2f}".format(udregning)
                    float_value = float(formatted_string)
                    st.write(f"Følgende beløb skal krediteres: {float_value:.2f} kr")
                    st.write(f"Kopier denne udregning i kreditnota-log: ({num_days:.2f} dage * {ab_pris:.2f} kr) / 30,42 dage = {float_value:.2f} kr")
                    st.warning("OBS: Erhvervskonsulenter. Har du husket at tilføje moms til abonnementspris? Hvis ikke skal du gange ovenstående resultat med 1.25.")
        elif antal_ab == '3':
            pris = (st.number_input("Skriv pris på abonnement:", step=10.0))
            pris_2 = (st.number_input(f"Skriv pris på abonnement {int(antal_ab) - 1}", step=10.0))
            pris_3 = (st.number_input(f"Skriv pris på abonnement {int(antal_ab)}", step=10.0))

            date_1 = st.date_input("Skriv startdato") 
            date_2 = st.date_input("Skriv slutdato")
            konst_måned = 30.42 
            ab_pris = (pris+pris_2+pris_3) 
            delta = date_2 - date_1
            num_days = delta.days  
            udregning = (num_days * ab_pris) / konst_måned
            
            #TODO lav en if else hvor hvis der trykkes på knap "Er der flere ab?", kreer nyt input felt og medregn dette. 
            beregn_knap = st.button("BEREGN")
            if(beregn_knap):
                if udregning == 0:
                    st.warning("Antal dage kan ikke være 0. Ændr start og slutdato for udregning.")
                else:
                    formatted_string = "{:.2f}".format(udregning)
                    float_value = float(formatted_string)
                    st.write(f"Følgende beløb skal krediteres: {float_value:.2f} kr")
                    st.write(f"Kopier denne udregning i kreditnota-log: ({num_days:.2f} dage * {ab_pris:.2f} kr) / 30,42 dage = {float_value:.2f} kr")
                    st.warning("OBS: Erhvervskonsulenter. Har du husket at tilføje moms til abonnementspris? Hvis ikke skal du gange ovenstående resultat med 1.25.")
        elif antal_ab == '4':
            pris = (st.number_input("Skriv pris på abonnement:", step=10.0))
            pris_2 = (st.number_input(f"Skriv pris på abonnement {int(antal_ab)-2}", step=10.0))
            pris_3 = (st.number_input(f"Skriv pris på abonnement {int(antal_ab)-1}", step=10.0))
            pris_4 = (st.number_input(f"Skriv pris på abonnement {int(antal_ab)}", step=10.0))

            date_1 = st.date_input("Skriv startdato") 
            date_2 = st.date_input("Skriv slutdato")
            konst_måned = 30.42
            ab_pris = (pris+pris_2+pris_3+pris_4) 
            delta = date_2 - date_1
            num_days = delta.days  
            udregning = (num_days * ab_pris) / konst_måned
            
            #TODO lav en if else hvor hvis der trykkes på knap "Er der flere ab?", kreer nyt input felt og medregn dette. 
            beregn_knap = st.button("BEREGN")
            if(beregn_knap):
                if udregning == 0:
                    st.warning("Antal dage kan ikke være 0. Ændr start og slutdato for udregning.")
                else:
                    formatted_string = "{:.2f}".format(udregning)
                    float_value = float(formatted_string)
                    st.write(f"Følgende beløb skal krediteres: {float_value:.2f} kr")
                    st.write(f"Kopier denne udregning i kreditnota-log: ({num_days:.2f} dage * {ab_pris:.2f} kr) / 30,42 dage = {float_value:.2f} kr")
                    st.warning("OBS: Erhvervskonsulenter. Har du husket at tilføje moms til abonnementspris? Hvis ikke skal du gange ovenstående resultat med 1.25.")
        elif antal_ab == '5':
            pris = (st.number_input("Skriv pris på abonnement:", step=10.0))
            pris_2 = (st.number_input(f"Skriv pris på abonnement {int(antal_ab)-3}", step=10.0))
            pris_3 = (st.number_input(f"Skriv pris på abonnement {int(antal_ab)-2}", step=10.0))
            pris_4 = (st.number_input(f"Skriv pris på abonnement {int(antal_ab)-1}", step=10.0))
            pris_5 = (st.number_input(f"Skriv pris på abonnement {int(antal_ab)}", step=10.0))

            date_1 = st.date_input("Skriv startdato") 
            date_2 = st.date_input("Skriv slutdato")
            konst_måned = 30.42
            ab_pris = (pris+pris_2+pris_3+pris_4+pris_5)
            delta = date_2 - date_1
            num_days = delta.days  
            udregning = ((num_days * ab_pris)) / konst_måned        
            #TODO lav en if else hvor hvis der trykkes på knap "Er der flere ab?", kreer nyt input felt og medregn dette. 
            beregn_knap = st.button("BEREGN")
            if(beregn_knap):
                if udregning == 0:
                    st.warning("Antal dage kan ikke være 0. Ændr start og slutdato for udregning.")
                else:
                    #formatted_string = "{:.2f}".format(udregning)
                    #float_value = float(formatted_string)
                    st.write(f"Følgende beløb skal krediteres: {udregning:.2f} kr")
                    st.write(f"Kopier denne udregning i kreditnota-log: ({num_days:.2f} dage * {ab_pris:.2f} kr) / 30,42 dage = {udregning:.2f} kr")
                    st.warning("OBS: Erhvervskonsulenter. Har du husket at tilføje moms til abonnementspris? Hvis ikke skal du gange ovenstående resultat med 1.25.")
            
        
            

if __name__ == "__main__":
    main()



    



