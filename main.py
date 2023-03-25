import streamlit as st

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help= "Select the nuber of days to forecast")
option = st.selectbox("Select data to view",
                      ("Weather", "Sky"))
    
st.subheader(f"{option} for the next {days} days in {place}")


