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







credenciais = credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gsc"]
)


my_file = st.secrets['path']['sheets']



arquivo= credenciais.open_by_url(my_file)


aba = arquivo.worksheet_by_title('1')


        
df = aba.get_as_df()



st.title('Simulation Dashboard')



c1, c2 = st.columns([1,1])


with c1:
    st.data_editor(df)
    
with c2:
    fig = px.line(df,x = 'Vocab Train', y = 'ACC Train', markers = True)
    fig.update_layout(margin=dict(t=0, b=0), height=300,yaxis_range=[0,1])
    st.plotly_chart(fig, use_container_width=True, theme="streamlit", key=None, on_select="ignore", selection_mode=('points', 'box', 'lasso'), config={"displayModeBar": False})
    

sleep(5)

st.rerun()
