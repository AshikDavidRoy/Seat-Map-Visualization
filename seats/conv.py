import mysql.connector
import json

# Database credentials
DB_HOST = 'localhost'
DB_USER = 'root'               # Default user for XAMPP
DB_PASSWORD = ''               # Default password (leave empty if you haven't set one)
DB_NAME = 'seat_booking'       # Your database name
TABLE_NAME = 'seatsss'         # Your table name

def fetch_data():
    conn = None
    cursor = None
    try:
        # Create a database connection
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        print("Database connection successful.")
        
        # Create a cursor to execute SQL queries
        cursor = conn.cursor(dictionary=True)  # Fetch rows as dictionaries
        
        # Query to fetch data
        sql = f"SELECT * FROM {TABLE_NAME}"
        cursor.execute(sql)

        # Fetch all rows from the executed query
        results = cursor.fetchall()

        if results:
            # Convert the results to JSON
            json_data = json.dumps(results, indent=4)  # JSON_PRETTY_PRINT equivalent
            print("Data retrieved successfully:")
            print(json_data)

            # Save the JSON output to a file
            with open('output.json', 'w') as json_file:
                json_file.write(json_data)
                print("JSON data saved to 'output.json'.")
        else:
            print("No data found in the table.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if cursor:
            cursor.close()
            print("Cursor closed.")
        if conn:
            conn.close()
            print("Database connection closed.")

if __name__ == '__main__':
    fetch_data()
