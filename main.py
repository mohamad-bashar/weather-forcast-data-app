import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the nuber of days to forecast")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))


if place:
    if days > 1:
        st.subheader(f"{option} for the next {days} days in {place}")
    else:
        st.subheader(f"{option} for the next day in {place}")
    try:

        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict['main']['temp']/10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={
                'x': 'Date', 'y': 'Temperature (C)'})
            st.plotly_chart(figure)
        elif option == "Sky":
            filtered_data = ['imgs/' + dict['weather'][0]['main'].lower() +
                             '.png' for dict in filtered_data]
            st.image(filtered_data, width=115)
    except KeyError:
        st.error('city not found')
