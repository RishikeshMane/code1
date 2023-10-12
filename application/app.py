import streamlit as st 
import numpy as np         
import pandas as pd 
import time 
import plotly.express as px 
import nltk
import altair as alt
nltk.download('stopwords')

#import data from csv after wards will get from azure realtime end point
df = pd.read_csv("../file5.csv")



#streamlit
st.set_page_config(
    page_title = 'Azure ETL with Streamlit',
    page_icon = '✅',
    layout = 'wide'
)

st.title("Azure ETL with Streamlit")
job_filter = st.selectbox("Select the Company name", pd.unique(df['name']))
#job_filter1 = st.selectbox("Select the Company name", pd.unique(df['name']),key="one")




ar = np.arange(1, 100)
rand_filter = st.selectbox("select the Numbers", ar)
df_sin=df[:rand_filter]



listofnames=['bank','hospital']
name_filter = st.selectbox("Types",listofnames)

bank_data=df_sin[df_sin['name'].str.lower().str.contains(name_filter)]



# df['text'] = df['text'].astype(str).str.lower()
# df.head(3)

# creating a single-element container.
placeholder = st.empty()

df = df[df['name']==job_filter]
df_save = df['ceo_approval']

data = {"name":df_sin["name"],"approval":df_sin["ceo_approval"]}



source = pd.DataFrame({
        'rating': df_sin['rating'],
        'company_name': df_sin['name']
     })
 
line_chart = alt.Chart(source).mark_line().encode(
        y='rating',
        x='company_name',
    )


source1 = pd.DataFrame({
        'ceo_approval1': df_sin['ceo_approval'],
        'company_name1': df_sin['name']
     })
 
line_chart1 = alt.Chart(source1).mark_line().encode(
        y='ceo_approval1',
        x='company_name1',
    )

 
st.altair_chart(line_chart, use_container_width=True)
st.altair_chart(line_chart1, use_container_width=True)

st.text(df_sin[:10])
st.text(bank_data[:10])
