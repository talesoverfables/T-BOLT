import streamlit as st
import sqlite3

# Function to create database table if not exists
def create_table():
    conn = sqlite3.connect('reports.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS reports
                 (id INTEGER PRIMARY KEY,
                 name TEXT,
                 place TEXT,
                 report TEXT)''')
    conn.commit()
    conn.close()

# Function to insert report into database
def insert_report(name, place, report):
    conn = sqlite3.connect('reports.db')
    c = conn.cursor()
    c.execute("INSERT INTO reports (name, place, report) VALUES (?, ?, ?)", (name, place, report))
    conn.commit()
    conn.close()

# Function to retrieve all reports from database
def get_reports():
    conn = sqlite3.connect('reports.db')
    c = conn.cursor()
    c.execute("SELECT * FROM reports")
    reports = c.fetchall()
    conn.close()
    return reports

# Main function to run the Streamlit app
def main():
    st.title('Report Submission Form')

    # Input fields for name, place, and report
    name = st.text_input('Enter your name:')
    places = ['ABVMCRI Gate', 'Russel Market']  # Example list of places
    place = st.selectbox('Select your place:', places)
    report = st.text_area('Enter your report:')

    # Button to submit report
    if st.button('Submit'):
        if name.strip() == '' or report.strip() == '':
            st.error('Please fill in all fields!')
        else:
            insert_report(name, place, report)
            st.success('Report submitted successfully!')

    if st.button("Show All Reports"):
    # Display all reports stored in the database
        st.header('All Reports')
        reports = get_reports()
        for r in reports:
            st.write(f"**ID:** {r[0]}, **Name:** {r[1]}, **Place:** {r[2]}, **Report:** {r[3]}")

if __name__ == '__main__':
    create_table()
    main()
