import os

# Function to clear the database
def clear_database():
    # Check if the database file exists
    if os.path.exists('reports.db'):
        # Delete the database file
        os.remove('reports.db')
        print("Database cleared successfully.")
    else:
        print("Database does not exist.")

if __name__ == '__main__':
    clear_database()