import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Sales Data", page_icon=":bar_chart:", layout="wide")

data = pd.read_excel(
    io='C:\\Users\\blanc\\OneDrive\\Documentos\\Clean_Sales_Data.xlsx',
    engine='openpyxl',
    sheet_name='Clean_Sales_Data'
)

st.sidebar.header("Use Filters Below:")

Region = st.sidebar.multiselect(
    "Select Region", options=data["Region"].unique(),default=data["Region"].unique())
Country = st.sidebar.multiselect(
    "Select Country", options=data["Country"].unique(), default=data["Country"].unique())
Source_Channel = st.sidebar.multiselect(
    "Select Marketing Campaign", options=data["Source_Channel"].unique(),default=data["Source_Channel"].unique())

df_selection = data.query(
    "Region == @Region &Country == @Country & Source_Channel == @Source_Channel")

st.title(":bar_chart: Marketing DashBoard 2022")
st.markdown("<h1 style='text-align: center; color: White;'>Sales Report 2022</h1>",
            unsafe_allow_html=True)

total_units_sales = int(df_selection["Sales"].sum())
average_sales = round(df_selection["Sales"].mean(), 1)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Sales:")
    st.subheader(f"US ${total_units_sales:,}")
with right_column:
    st.subheader("Average Sales:")
    st.subheader(f"US ${average_sales}")

st.markdown("---")

sales_by_country = (
    df_selection.groupby(by=["Country"]).sum()[["Sales"]].sort_values(by="Sales"))

fig_sales = px.bar(
    sales_by_country,
    x="Sales",
    y=sales_by_country.index,
    orientation="h",
    title="<b>Sales by Country</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_country),
    template="plotly_white",
)
fig_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

sales_by_channel = (
    df_selection.groupby(by=["Source_Channel"]).sum()[["Sales"]].sort_values(by="Sales"))

fig_sales2 = px.bar(
    sales_by_channel,
    x="Sales",
    y=sales_by_channel.index,
    orientation="h",
    title="<b>Sales by Channel</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_channel),
    template="plotly_white",
)
fig_sales2.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

sales_by_region = (
    df_selection.groupby(by=["Region"]).sum()[["Sales"]].sort_values(by="Sales"))

fig_sales3 = px.bar(
    sales_by_region,
    x="Sales",
    y=sales_by_region.index,
    orientation="h",
    title="<b>Sales by Region</b>",
    color_discrete_sequence=["#0096d2"] * len(sales_by_region),
    template="plotly_white",
)
fig_sales3.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

st.plotly_chart(fig_sales)
st.markdown("---")
st.plotly_chart(fig_sales2)
st.markdown("---")
st.plotly_chart(fig_sales3)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
