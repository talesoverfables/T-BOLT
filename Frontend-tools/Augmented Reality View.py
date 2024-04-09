import streamlit as st

def main():
    st.title("Areas under consideration")

    # Create a dropdown menu with options
    page_choice = st.selectbox("Select a page:", ["ABVMCRI Gate", "Russel Market"])

    # Display content based on the user's choice
    if page_choice == "ABVMCRI Gate":
        st.header("ABVMCRI Gate - Video")

        st.write("Using Computer Vision")
        st.write("Its going to have the CV, AR visuals and little bit information about whats really happening")

        # Display a local video file
        st.video("E:/Smruthi/PROJECTS/KSP DATATHON/SHIT IS REAL/Sample-abvmcri.mp4")
        st.write("Its going to have the CV, AR visuals and little bit information about whats really happening")
    elif page_choice == "Russel Market":
        st.write("Its going to have the CV, AR visuals and little bit information about whats really happening")

if __name__ == "__main__":
    main()
