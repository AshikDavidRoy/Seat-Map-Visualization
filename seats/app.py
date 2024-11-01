from flask import Flask, render_template, jsonify
import mysql.connector
import json

app = Flask(__name__)

# Database connection
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'database': 'seat_booking'
}

@app.route('/')
def index():
    return render_template('2.html')  # Render the main HTML page

@app.route('/api/seats')
def get_seats():
    # Sample JSON data as defined previously
    sample_seats_data = {
        "seats": [
            {"row_number": 1, "seat_number": 1, "status": "available"},
            {"row_number": 1, "seat_number": 2, "status": "available"},
            {"row_number": 1, "seat_number": 3, "status": "available"},
            {"row_number": 1, "seat_number": 4, "status": "available"},
            {"row_number": 1, "seat_number": 5, "status": "available"},
            {"row_number": 1, "seat_number": 6, "status": "unavailable"},
            {"row_number": 1, "seat_number": 7, "status": "available"},
            {"row_number": 1, "seat_number": 8, "status": "available"},
            {"row_number": 1, "seat_number": 9, "status": "available"},
            {"row_number": 1, "seat_number": 10, "status": "available"},
            {"row_number": 2, "seat_number": 1, "status": "available"},
            {"row_number": 2, "seat_number": 2, "status": "available"},
            {"row_number": 2, "seat_number": 3, "status": "unavailable"},
            {"row_number": 2, "seat_number": 4, "status": "available"},
            {"row_number": 2, "seat_number": 5, "status": "available"},
            {"row_number": 2, "seat_number": 6, "status": "available"},
            {"row_number": 2, "seat_number": 7, "status": "available"},
            {"row_number": 2, "seat_number": 8, "status": "unavailable"},
            {"row_number": 2, "seat_number": 9, "status": "available"},
            {"row_number": 2, "seat_number": 10, "status": "available"},
            {"row_number": 3, "seat_number": 1, "status": "available"},
            {"row_number": 3, "seat_number": 2, "status": "available"},
            {"row_number": 3, "seat_number": 3, "status": "available"},
            {"row_number": 3, "seat_number": 4, "status": "available"},
            {"row_number": 3, "seat_number": 5, "status": "unavailable"},
            {"row_number": 3, "seat_number": 6, "status": "available"},
            {"row_number": 3, "seat_number": 7, "status": "available"},
            {"row_number": 3, "seat_number": 8, "status": "available"},
            {"row_number": 3, "seat_number": 9, "status": "available"},
            {"row_number": 3, "seat_number": 10, "status": "available"},
            {"row_number": 4, "seat_number": 1, "status": "available"},
            {"row_number": 4, "seat_number": 2, "status": "available"},
            {"row_number": 4, "seat_number": 3, "status": "available"},
            {"row_number": 4, "seat_number": 4, "status": "available"},
            {"row_number": 4, "seat_number": 5, "status": "available"},
            {"row_number": 4, "seat_number": 6, "status": "available"},
            {"row_number": 4, "seat_number": 7, "status": "unavailable"},
            {"row_number": 4, "seat_number": 8, "status": "available"},
            {"row_number": 4, "seat_number": 9, "status": "available"},
            {"row_number": 4, "seat_number": 10, "status": "available"},
            {"row_number": 5, "seat_number": 1, "status": "unavailable"},
            {"row_number": 5, "seat_number": 2, "status": "available"},
            {"row_number": 5, "seat_number": 3, "status": "available"},
            {"row_number": 5, "seat_number": 4, "status": "available"},
            {"row_number": 5, "seat_number": 5, "status": "available"},
            {"row_number": 5, "seat_number": 6, "status": "available"},
            {"row_number": 5, "seat_number": 7, "status": "available"},
            {"row_number": 5, "seat_number": 8, "status": "available"},
            {"row_number": 5, "seat_number": 9, "status": "available"},
            {"row_number": 5, "seat_number": 10, "status": "available"}
        ]
    }
    return jsonify(sample_seats_data)

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, render_template, jsonify
# import mysql.connector

# app = Flask(__name__)

# # Database configuration
# db_config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': '',
#     'database': 'seat_booking'
# }

# # Function to fetch seat data from the database
# def fetch_seat_data():
#     connection = mysql.connector.connect(**db_config)
#     cursor = connection.cursor(dictionary=True)
#     cursor.execute("SELECT * FROM seatsss")  # Use your correct table name
#     seats = cursor.fetchall()
#     cursor.close()
#     connection.close()
#     return seats

# @app.route('/')
# def index():
#     return render_template('index.html')  # Render the main HTML page

# @app.route('/api/seats')
# def get_seats():
#     seats = fetch_seat_data()
#     return jsonify({'seats': seats})  # Return the data as JSON

# if __name__ == '__main__':
#     app.run(debug=True)
