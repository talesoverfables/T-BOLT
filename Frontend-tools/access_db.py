import sqlite3

# Function to create a database connection
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

# Function to fetch all reports from the database
def fetch_reports(conn):
    reports = []
    cur = conn.cursor()
    cur.execute("SELECT * FROM reports")
    rows = cur.fetchall()
    for row in rows:
        reports.append(row[1])  # Assuming the report text is in the second column
    return reports

# Main function
def main():
    # Create a database connection
    conn = create_connection("reports.db")
    if conn is not None:
        # Fetch all reports from the database
        reports = fetch_reports(conn)
        if reports:
            print("Reports:")
            for report in reports:
                print(report)
        else:
            print("No reports found.")
        # Close the database connection
        conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == "__main__":
    main()
