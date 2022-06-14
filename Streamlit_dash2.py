import streamlit as st
import pandas as pd
import numpy as np 
import plotly.express as px

st.set_page_config(
    page_title = 'Activation Info',
    page_icon = '📈',
    layout = 'wide'
)

#data = pd.read_excel(
#    io='C:\\Users\\blanc\\OneDrive\\Documentos\\Clean_Sales_Data.xlsx',
#    engine='openpyxl',
#   sheet_name='Clean_Sales_Data'

st.title("📈 May's Activation")

#st.markdown("<h1 style='text-align: center; color: White;'>General Stats</h1>",
#           unsafe_allow_html=True)

Activations, Active_subs = st.columns(2)

with Activations:
    #st.subheader("**Total of Activations**")
    st.markdown("<h1 style='text-align: center; color: Black;'>Total of Activations</h1>",unsafe_allow_html=True)
    number1 = 120000 
    st.markdown(f"<h1 style='text-align: center; color: red;'>{number1}</h1>", unsafe_allow_html=True)

with Active_subs:
    #st.subheader("**Total of Active Subs**")
    st.markdown("<h1 style='text-align: center; color: Black;'>Total of Active Subs</h1>",unsafe_allow_html=True)
    number2 = 100000 
    st.markdown(f"<h1 style='text-align: center; color: red;'>{number2}</h1>", unsafe_allow_html=True)

st.markdown("<hr/>",unsafe_allow_html=True)

chart1, chart2 = st.columns(2)

with chart1:
    chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

with chart2:
    chart_data = pd.DataFrame(np.random.randn(2000, 3),columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.markdown("<h1 style='text-align: center; color: Black;'>Activation by State</h1>",unsafe_allow_html=True)
st.map(df,use_container_width=True)

#fig = px.choropleth(
    #df,
    #locations="id",
    #color="DensityScale",
    #hover_name="State or union territory",
    #hover_data=["Density"],
    #title="India Population Density",)
#fig.update_geos(fitbounds="locations", visible=False)
#fig.show()
