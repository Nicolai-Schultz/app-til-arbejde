import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

with open("style.css") as source_des:
        st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)

st.header("Velkommen til Kreditmaksudregneren!")




kode = st.text_input("Indtast din kode for at se dine mål")
    
if kode == "Hej":
        data = {
        'kpt': [7.5, 8.5, 9.5],
        'ga': [2.5, 3, 3.5],
        'kt': [20, 30, 50],
        'csat': [100,100,100],
        'copc': [60, 65, 70],
        }
        data2 = {
              'point': [2,3,5],
        }
        data_penge = {
              'DKK': [200,300,500]
        }
        penge = pd.DataFrame(data_penge)
        penge.index=["20p","25p","30p"]

        st.table(penge)
        df = pd.DataFrame(data)
        df.index=["2p","3p","5p"]

        st.table(df)


        kpt_input = st.number_input("Hvad er din aktuelle KPT?", step=1.0, value = 7.5)
        ga_input = st.number_input("Hvad er din aktuelle GA%?", step=0.25, value = 2.5)
        kt_input = st.number_input("Hvad er din aktuelle mængde af kontakttilladelser?", step=5, value = 10)
        csat_input = st.number_input("Hvad er din aktuelle CSAT%?", step=5, value = 90)
        copc_input = st.number_input("Hvad er din aktuelle COPC%?", step=5, value = 90)
        tæller = 0

        st.subheader("Din leder har sat følgende mål for dig:")
        #KPT sætning
        if kpt_input >= data['kpt'][2]:
              tæller += data2['point'][2]
              st.write(f"Med en KPT på {kpt_input} opnår du {data2['point'][2]} antal point")
        elif kpt_input >= data['kpt'][1]:
              tæller += data2['point'][1]
              st.write(f"Med en KPT på {kpt_input} opnår du {data2['point'][1]} antal point")
        elif kpt_input >= data['kpt'][0]:
              tæller += data2['point'][0]
              st.write(f"Med en KPT på {kpt_input} opnår du {data2['point'][0]} antal point")
        else:
              st.write(f"Med en KPT på {kpt_input} opnår du 0 antal point")
        #GA sætning
        if ga_input >= data['ga'][2]:
              tæller += data2['point'][2]
              st.write(f"Med en GA% på {ga_input} opnår du {data2['point'][2]} antal point")
        elif ga_input >= data['ga'][1]:
              tæller += data2['point'][1]
              st.write(f"Med en GA% på {ga_input} opnår du {data2['point'][1]} antal point")
        elif ga_input >= data['ga'][0]:
              tæller += data2['point'][0]
              st.write(f"Med en GA% på {ga_input} opnår du {data2['point'][0]} antal point")
        else:
              st.write(f"Med en GA% på {ga_input} opnår du 0 antal point")
        #KT sætning
        if kt_input >= data['kt'][2]:
              tæller += data2['point'][2]
              st.write(f"Med en KT indsamling på {kt_input} opnår du {data2['point'][2]} antal point")
        elif kt_input >= data['kt'][1]:
              tæller += data2['point'][1]
              st.write(f"Med en KT indsamling på {kt_input} opnår du {data2['point'][1]} antal point")
        elif kt_input >= data['kt'][0]:
              tæller += data2['point'][0]
              st.write(f"Med en KT indsamling på {kt_input} opnår du {data2['point'][0]} antal point")
        else:
              st.write(f"Med en KT indsamling på {kt_input} opnår du 0 antal point")
        #CSAT sætning
        if csat_input >= data['csat'][2]:
              tæller += data2['point'][2]
              st.write(f"Med en CSAT% på {csat_input} opnår du {data2['point'][2]} antal point")
        elif csat_input >= data['csat'][1]:
              tæller += data2['point'][1]
              st.write(f"Med en CSAT% på {csat_input} opnår du {data2['point'][1]} antal point")
        elif csat_input >= data['csat'][0]:
              tæller += data2['point'][0]
              st.write(f"Med en CSAT% på {csat_input} opnår du {data2['point'][0]} antal point")
        else:
              st.write(f"Med en CSAT% på {csat_input} opnår du 0 antal point")
        #COPC sætning
        if copc_input >= data['copc'][2]:
              tæller += data2['point'][2]
              st.write(f"Med en COPC% på {copc_input} opnår du {data2['point'][2]} antal point")
        elif copc_input >= data['copc'][1]:
              tæller += data2['point'][1]
              st.write(f"Med en COPC% på {copc_input} opnår du {data2['point'][1]} antal point")
        elif copc_input >= data['copc'][0]:
              tæller += data2['point'][0]
              st.write(f"Med en COPC% på {copc_input} opnår du {data2['point'][0]} antal point")
        else:
              st.write(f"Med en COPC% på {copc_input} opnår du 0 antal point")
        
        st.write(f"Du har samlet set opnået {tæller} point!")
        if tæller == 25:
              st.success(f"Du har derfor optjent {data_penge['DKK'][2]} DKK i statkonkurrencen!")
        elif tæller >20<25: 
              st.success(f"Du har derfor optjent {data_penge['DKK'][1]} DKK i statkonkurrencen!")
        else:
              st.success(f"Du har derfor optjent {data_penge['DKK'][0]} DKK i statkonkurrencen!")

    
if kode == "Hej2":
        data = {
        'kpt': [8.5, 9.5, 10.5],
        'ga': [3.5, 4, 5.5],
        'kt': [20, 30, 50],
        'csat': [100,100,100],
        'copc': [60, 65, 70],
        }
        data2 = {
              'point': [2,3,5],
        }
        data_penge = {
              'DKK': [200,300,500]
        }
        penge = pd.DataFrame(data_penge)
        penge.index=["20p","25p","30p"]

        st.table(penge)
        df = pd.DataFrame(data)
        df.index=["2p","3p","5p"]

        st.table(df)


        kpt_input = st.number_input("Hvad er din aktuelle KPT?", step=1.0, value = 7.5)
        ga_input = st.number_input("Hvad er din aktuelle GA%?", step=0.25, value = 2.5)
        kt_input = st.number_input("Hvad er din aktuelle mængde af kontakttilladelser?", step=5, value = 10)
        csat_input = st.number_input("Hvad er din aktuelle CSAT%?", step=5, value = 90)
        copc_input = st.number_input("Hvad er din aktuelle COPC%?", step=5, value = 90)
        tæller = 0

        st.subheader("Din leder har sat følgende mål for dig:")
        #KPT sætning
        if kpt_input >= data['kpt'][2]:
              tæller += data2['point'][2]
              st.write(f"Med en KPT på {kpt_input} opnår du {data2['point'][2]} antal point")
        elif kpt_input >= data['kpt'][1]:
              tæller += data2['point'][1]
              st.write(f"Med en KPT på {kpt_input} opnår du {data2['point'][1]} antal point")
        elif kpt_input >= data['kpt'][0]:
              tæller += data2['point'][0]
              st.write(f"Med en KPT på {kpt_input} opnår du {data2['point'][0]} antal point")
        else:
              st.write(f"Med en KPT på {kpt_input} opnår du 0 antal point")
        #GA sætning
        if ga_input >= data['ga'][2]:
              tæller += data2['point'][2]
              st.write(f"Med en GA% på {ga_input} opnår du {data2['point'][2]} antal point")
        elif ga_input >= data['ga'][1]:
              tæller += data2['point'][1]
              st.write(f"Med en GA% på {ga_input} opnår du {data2['point'][1]} antal point")
        elif ga_input >= data['ga'][0]:
              tæller += data2['point'][0]
              st.write(f"Med en GA% på {ga_input} opnår du {data2['point'][0]} antal point")
        else:
              st.write(f"Med en GA% på {ga_input} opnår du 0 antal point")
        #KT sætning
        if kt_input >= data['kt'][2]:
              tæller += data2['point'][2]
              st.write(f"Med en KT indsamling på {kt_input} opnår du {data2['point'][2]} antal point")
        elif kt_input >= data['kt'][1]:
              tæller += data2['point'][1]
              st.write(f"Med en KT indsamling på {kt_input} opnår du {data2['point'][1]} antal point")
        elif kt_input >= data['kt'][0]:
              tæller += data2['point'][0]
              st.write(f"Med en KT indsamling på {kt_input} opnår du {data2['point'][0]} antal point")
        else:
              st.write(f"Med en KT indsamling på {kt_input} opnår du 0 antal point")
        #CSAT sætning
        if csat_input >= data['csat'][2]:
              tæller += data2['point'][2]
              st.write(f"Med en CSAT% på {csat_input} opnår du {data2['point'][2]} antal point")
        elif csat_input >= data['csat'][1]:
              tæller += data2['point'][1]
              st.write(f"Med en CSAT% på {csat_input} opnår du {data2['point'][1]} antal point")
        elif csat_input >= data['csat'][0]:
              tæller += data2['point'][0]
              st.write(f"Med en CSAT% på {csat_input} opnår du {data2['point'][0]} antal point")
        else:
              st.write(f"Med en CSAT% på {csat_input} opnår du 0 antal point")
        #COPC sætning
        if copc_input >= data['copc'][2]:
              tæller += data2['point'][2]
              st.write(f"Med en COPC% på {copc_input} opnår du {data2['point'][2]} antal point")
        elif copc_input >= data['copc'][1]:
              tæller += data2['point'][1]
              st.write(f"Med en COPC% på {copc_input} opnår du {data2['point'][1]} antal point")
        elif copc_input >= data['copc'][0]:
              tæller += data2['point'][0]
              st.write(f"Med en COPC% på {copc_input} opnår du {data2['point'][0]} antal point")
        else:
              st.write(f"Med en COPC% på {copc_input} opnår du 0 antal point")
        
        st.write(f"Du har samlet set opnået {tæller} point!")
        if tæller == 25:
              st.success(f"Du har derfor optjent {data_penge['DKK'][2]} DKK i statkonkurrencen!")
        elif tæller >20<25: 
              st.success(f"Du har derfor optjent {data_penge['DKK'][1]} DKK i statkonkurrencen!")
        else:
              st.success(f"Du har derfor optjent {data_penge['DKK'][0]} DKK i statkonkurrencen!")

              
              
              

              
              
              

