import streamlit as st



import google.auth

from google.oauth2 import service_account


import pygsheets

import pandas as pd

from time import sleep

import plotly.express as px


st.set_page_config(layout="wide")




st.markdown("""
<style>
.streamlit-columns {
    border: 2px solid #000;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)






SCOPES = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
my_credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gsc"],
    scopes=SCOPES
   
)


credenciais = pygsheets.authorize(custom_credentials=my_credentials)


my_file = st.secrets['path']['sheets']



arquivo= credenciais.open_by_url(my_file)


aba = arquivo.worksheet_by_title('1')


        
df = aba.get_as_df()



st.title('Simulation Dashboard')



c1, c2, c3 = st.columns([1,1,1])


with c1:
    st.subheader('Output')
    st.data_editor(df)
    
with c2:
    st.subheader('Plot')
    fig = px.line(df,x = 'Vocab Train', y = ['ACC Train', 'ACC Val'], markers = True)
    fig.update_layout(margin=dict(t=0, b=0), height=300,yaxis_range=[0,1])
    st.plotly_chart(fig, use_container_width=True, theme="streamlit", key=None, on_select="ignore", selection_mode=('points', 'box', 'lasso'), config={"displayModeBar": False})
    

sleep(15)

st.rerun()
