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
    c.execute('''CREATE TABLE IF NOT EXISTS place_counts
                 (place TEXT PRIMARY KEY,
                 count INTEGER)''')
    # Initialize count for each place
    c.execute("INSERT OR IGNORE INTO place_counts (place, count) VALUES (?, ?)", ('ABVMCRI Gate', 0))
    c.execute("INSERT OR IGNORE INTO place_counts (place, count) VALUES (?, ?)", ('Russel Market', 0))
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

# Function to retrieve counts of each place
def get_place_counts():
    conn = sqlite3.connect('reports.db')
    c = conn.cursor()
    c.execute("SELECT * FROM place_counts")
    counts = c.fetchall()
    conn.close()
    return counts

# Function to update count of a place
def update_place_count(place):
    conn = sqlite3.connect('reports.db')
    c = conn.cursor()
    c.execute("UPDATE place_counts SET count = count + 1 WHERE place = ?", (place,))
    conn.commit()
    conn.close()

# Main function to run the Streamlit app
def main():
    st.title('Report Submission Form')

    # Input fields for name, place, and report
    name = st.text_input('Enter your name:')
    place_options = ['ABVMCRI Gate', 'Russel Market']  # Options for place
    place = st.selectbox('Select your place:', place_options)

    # Button to submit report
    report = st.text_area('Enter your report:')
    if st.button('Submit'):
        if name.strip() == '' or report.strip() == '':
            st.error('Please fill in all fields!')
        else:
            insert_report(name, place, report)
            update_place_count(place)
            st.success('Report submitted successfully!')

    if st.button("Show the number of reports - location wise"):
    # Display counts for each place
        st.header('Show the number of reports - location wise')
        counts = get_place_counts()
        for count in counts:
            st.write(f"**Place:** {count[0]}, **Number of Reports** {count[1]}")
    
    # Display all reports stored in the database
    if st.button("Show All Reports"):
        st.header('All Reports')
        reports = get_reports()
        for r in reports:
            st.write(f"**ID:** {r[0]}, **Name:** {r[1]}, **Place:** {r[2]}, **Report:** {r[3]}")

if __name__ == '__main__':
    create_table()
    main()
