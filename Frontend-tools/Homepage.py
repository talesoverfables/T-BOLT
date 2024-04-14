import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json
import pandas as pd
import pydeck as pdk
from PIL import Image

st.set_page_config(page_title = "T-BOLT : Traffic Bottleneck Out-tracing Logical Tech-Assistant", page_icon = ":computer:", layout = "wide")
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
        st.write("""Imagine a police officer wearing an AR headset or using a smartphone or tablet with AR capabilities. As the officer walks or drives through the city, this
    Web-app displays real-time information about traffic congestion, parking issues, encroachment of roads and footpaths, and poor road conditions. The
    AR experience is overlaid on the real world, allowing the officer to see the actual environment with additional valuable information.""")
        st.write("[Learn More >](https://docs.google.com/presentation/d/1SfAv4E1dG_Os59Px8zseLoBFlciG5gAL7fWOfxQ8Lw8/edit#slide=id.g26a99bbe636_1_45)")
        #st.image(img_contact_form, width=200, channels = "RGB")
    with right_column:
       # st.title("Welcome to T-BOLT : Traffic Bottleneck Out-tracing Logical Tech-Assistant!")
        st_lottie(path, height=500, width=600)

with st.container():
    st.write("---")
    st.header("THE LOCATIONS CONSIDERED:")
   # st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.write("\n")
        st.write("\n")
 
        st.write("\n")
        image1 = Image.open('E:/Smruthi/PROJECTS/KSP DATATHON/SHIT IS REAL/ABV.jpg')
        st.image(image1, caption='ABVMCRI Gate', use_column_width=True)
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        image2 = Image.open("E:/Smruthi/PROJECTS/KSP DATATHON/SHIT IS REAL/RM.jpg")
        st.image(image2, caption='Russell Market, Shivajinagar', use_column_width=True)
    with text_column:
        st.subheader("1. Atal Bihari Vajpayee Medical College and Research Institute Gate")
        text = "What we saw :"
        st.write(f"**{text}**", "The traffic junction outside the institute gate experienced significant congestion during peak hours, with a mix of private vehicles, public transport, pedestrians, and cyclists all vying for space. Traffic signals and police presence might struggle to efficiently manage the flow, leading to frustration among commuters and potential safety concerns for pedestrians.")
        st.subheader("2. Russell Market")
        st.write(f"**{text}**", "Due to the heavy flow of vehicles, including buses, cars, auto-rickshaws, and two-wheelers, navigating through the junction is challenging and time-consuming. The lack of dedicated lanes for different types of vehicles and insufficient traffic management measures further worsened the situation. The traffic junction near Russell Market in Bangalore could be characterized as congested and chaotic, posing challenges for commuters and pedestrians alike, especially during peak hours.")    

import pandas as pd

# Create a sample DataFrame with latitude and longitude columns
data = pd.DataFrame({
   'latitude': [ 12.9823, 12.98506],  # Example latitude values
    'longitude': [ 77.6034, 77.60587]  # Example longitude values
})


# Display the map
st.map(data)
#12.97075600, 12.97076,
#77.58056900, 77.58057,
