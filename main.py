import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help= "Select the nuber of days to forecast")
option = st.selectbox("Select data to view",
                      ("Weather", "Sky"))
    
st.subheader(f"{option} for the next {days} days in {place}")

def get_data(days):
    dates = ["2022-25-10",
            "2022-26-10",
            "2022-27-10",
            "2022-28-10",
            "2022-29-10",
            "2022-30-10"]
    data = [22, 32, 13, 17, 22, 14]
    data = [days * i for i in data]
    return dates, data

d, t = get_data(days=days)

figure = px.line(x=d, y=t, labels={'x':'Date', 'y':'Temperature (C)'})

st.plotly_chart(figure)

