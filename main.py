import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the nuber of days to forecast")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    filtered_data = get_data(place, days)

if option == "Temperature":
    temperatures = [dict['main']['temp']-273.15 for dict in filtered_data]
    dates = [dict["dt_txt"] for dict in filtered_data]
    figure = px.line(x=dates, y=temperatures, labels={
                     'x': 'Date', 'y': 'Temperature (C)'})
    st.plotly_chart(figure)
elif option == "Sky":
    filtered_data = ['imgs/' + dict['weather'][0]['main'].lower() +
                     '.png' for dict in filtered_data]
    st.image(filtered_data, width=115)
