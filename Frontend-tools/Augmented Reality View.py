import streamlit as st
from PIL import Image
st.set_page_config(page_title = "Augmented Reality View", page_icon = ":computer:", layout = "wide")
def main():
    st.title("Locations under consideration")
    st.write("We used Computer vision to identify traffic congestion bottlenecks near Russell Market and the Atal Bihari Vajpayee Medical College and Research Institute (ABVMCRI) Gate in Bangalore. Through a meticulous annotation process involving data collection, image labeling, and semantic segmentation, computer vision experts annotate traffic data to detect vehicles, pedestrians, and congestion patterns")
    # Create a dropdown menu with options
    page_choice = st.selectbox("Select a location:", ["ABVMCRI Gate", "Russel Market"])

    # Display content based on the user's choice
    if page_choice == "ABVMCRI Gate":
        st.subheader("ABVMCRI Gate - Video")
        st.write("Includes the annotated video around the ABVMCRI Gate, identifying different kind of bottlenecks like Wrong parking, footpath encroachment, pothole detection along with the appropriate time stamps.")

        # Display a local video file
        # Path to your local video file
        video_path = "E:/Smruthi/PROJECTS/KSP DATATHON/SHIT IS REAL/SAB.mov"

        # Display the local video
        st.video(video_path)
        #video_url2 = "https://drive.google.com/file/d/138-Ds5DsdjKaApsXbPcjt5qOnJxUzdFh/view?usp=sharing"
       # st.video(video_url2)
        st.subheader("ABVMCRI Gate - AR Visuals")
        st.subheader("[Click here for the AR Visuals of ABVMCRI Gate traffic flow >](https://ar-nr-abvmcri-gate.glitch.me/)")
        st.subheader("Use the given marker to locate the position of the AR :")
        image4 = Image.open("E:\Smruthi\PROJECTS\KSP DATATHON\SHIT IS REAL\marker.jpg")
        st.image(image4)
       
    elif page_choice == "Russel Market":
        st.subheader("Russell Market - Video")
        st.write("Includes the annotated video around the Russel Market, identifying different kind of bottlenecks like Wrong parking, footpath encroachment, pothole detection along with the appropriate time stamps.")
        video_path = "E:/Smruthi/PROJECTS/KSP DATATHON/SHIT IS REAL/russ.mov"

        # Display the local video
        st.video(video_path)
        # Display a local video file
       #video_url1 = "https://drive.google.com/file/d/1pBx1LT-GDNU5waLFQQLkiwsRr6SQW8rL/view?usp=sharing"
        #st.video(video_url1)
           
        st.subheader("Russel Market - AR Visuals")
        st.subheader("[Click here for the AR Visuals of Russell Market traffic flow >](https://russel-market-ar.glitch.me/)")
        st.subheader("Use the given marker to locate the position of the AR :")
        image3 = Image.open("E:\Smruthi\PROJECTS\KSP DATATHON\SHIT IS REAL\marker.jpg")
        st.image(image3)
if __name__ == "__main__":
    main()
