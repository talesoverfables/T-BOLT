import streamlit as st

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
        video_url2 = "https://drive.google.com/file/d/138-Ds5DsdjKaApsXbPcjt5qOnJxUzdFh/view?usp=sharing"
        st.video(video_url2)
        st.subheader("ABVMCRI Gate - AR Visuals")
        st.write("About AR")
    elif page_choice == "Russel Market":
        st.subheader("Russell Market - Video")
        st.write("Includes the annotated video around the Russel Market, identifying different kind of bottlenecks like Wrong parking, footpath encroachment, pothole detection along with the appropriate time stamps.")

        # Display a local video file
        video_url1 = "https://drive.google.com/file/d/1YK12Fl70D8zYz91n8r1WrEEC1YCAyZtX/view?usp=sharing"
        st.video(video_url1)
           
        st.subheader("Russel Market - AR Visuals")
        st.write("About AR")
        
if __name__ == "__main__":
    main()
