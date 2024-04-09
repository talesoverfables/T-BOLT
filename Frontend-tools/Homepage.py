import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json
from PIL import Image

st.set_page_config(page_title = "T-BOLT : Traffic Bottleneck Out-tracing Logical Tech-Assistant", page_icon = ":light_bulb", layout = "wide")
st.sidebar.success("Select a page above.")


def get(path:str):
    
    with open(path, "r") as f:
        return json.load(f)
    animation_data = f.read()
path = get("./ani.json")

#img_contact_form = Image.open("./i-freakin-love-this-logo.jpeg")
#st.image(img_contact_form, width=200, channels = "RGB")
with st.container():
    st.title("Welcome to T-BOLT : Traffic Bottleneck Out-tracing Logical Tech-Assistant! ")
   # st.button('💡')
    st.subheader("The Concept we work on! 💡 ")
    #st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        img_contact_form = Image.open("./i-freakin-love-this-logo.jpeg")
        st.image(img_contact_form, width=100, channels = "RGB")
        st.write("""Imagine a police officer wearing an AR headset or using a smartphone or tablet with AR capabilities. As the officer walks or drives through the city, the
    AR app displays real-time information about traffic congestion, parking issues, encroachment of roads and footpaths, and poor road conditions. The
    AR experience is overlaid on the real world, allowing the officer to see the actual environment with additional valuable information.""")
        st.write("[Learn More >](https://smruo.blogspot.com)")
        #st.image(img_contact_form, width=200, channels = "RGB")
    with right_column:
       # st.title("Welcome to T-BOLT : Traffic Bottleneck Out-tracing Logical Tech-Assistant!")
        st_lottie(path, height=500, width=600)

with st.container():
    st.write("---")
    st.header("My projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        pass
    with text_column:
        st.subheader("We are nuts")
        st.write("Hehehe brooo")
        
import streamlit as st
import pandas as pd

# Create a sample DataFrame with latitude and longitude columns
data = pd.DataFrame({
   'lat': [12.97076, 12.9823, 12.98506],  # Example latitude values
    'lon': [77.58057, 77.6034, 77.60587]  # Example longitude values
})

# Display the map
st.map(data)
#12.97075600, 12.97076,
#77.58056900, 77.58057,
