import streamlit as st
import pandas as pd
import plotly.express as px

st.title("In Search of Happiness")
df = pd.read_csv("happy.csv")
datax = st.selectbox("Select the data for the X-axis", df.columns[1:]) #("GDP", "Happiness", "Generosity"...))
datay = st.selectbox("Select the data for the Y-axis", df.columns[1:])
st.subheader(f"{datax} and {datay}")
print(datay)

def get_data(datax, datay):
    datax = datax.lower()
    datay = datay.lower()
    dataX = df[datax]
    dataY = df[datay]
    return dataX, dataY

x, y = get_data(datax, datay)

figure = px.scatter(x=x,y=y, labels={"x": datax, "y": datay})
st.plotly_chart(figure)


