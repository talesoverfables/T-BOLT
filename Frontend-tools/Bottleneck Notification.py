import streamlit as st
st.set_page_config(page_title = "Bottleneck Notifications", page_icon = ":computer:", layout = "wide")
def main():
   st.title("Bottleneck Notifications")

    # Display a button to trigger the notification
   st.subheader("AT ABVMCRI GATE - ")
   if st.button("Show New Reports At ABVMCRI Gate"):
       st.error('ID: 4, Name: Sharvari, Place: ABVMCRI Gate, Report: A huge lot of vegetable vendors creating a havoc, encroaching the footpath right infront of the ABVMCRI Gate.')

   if st.button("Resolved Reports At ABVMCRI Gate"):
      st.success("ID: 1, Name: Shree, Place: ABVMCRI Gate, Report: A huge lot of vegetable vendors creating a havoc, encroaching the footpath right infront of the ABVMCRI Gate.")
   
   st.subheader("AT RUSSELL MARKET - ")
   if st.button("Show New Reports At Russell Market"):
       st.error('None to show.')

   if st.button("Resolved Reports At Russell Market"):
       st.success("ID: 2, Name: Veena, Place: Russel Market, Report: Mess it is.")
       st.success("ID: 3, Name: Heera, Place: Russel Market, Report: Too much chaos.")
   
   st.subheader("Resolving the reports:")
   st.write("One report at ABVMCRI Gate : Contact Ashok Nagar Policestation ")
   contact_number = "+919945395632"  # Replace with the actual phone number

# Create a button to make the call
   #if st.button("Call Contact"):
       #st.write(f"Calling {contact_number}...")  
   
   if st.checkbox('Resolve all the Reports'):
      st.write('Resolved!')
      if st.button("Show the newly resolved Reports"):
         st.success("ID: 4, Name: Sharvari, Place: ABVMCRI Gate, Report: A huge lot of vegetable vendors creating a havoc, encroaching the footpath right infront of the ABVMCRI Gate.")


if __name__ == "__main__":
    main()

