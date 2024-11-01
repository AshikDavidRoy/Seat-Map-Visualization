<?php
// Database credentials
$DB_HOST = 'localhost';
$DB_USER = 'root';             // Default user for XAMPP
$DB_PASSWORD = '';             // Default password (leave empty if you haven't set one)
$DB_NAME = 'seat_booking';     // Your database name
$TABLE_NAME = 'seatss';       // Your table name

// Create connection
$conn = new mysqli($DB_HOST, $DB_USER, $DB_PASSWORD, $DB_NAME);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
// echo "Database connection successful.\n";

// Query to fetch data
$sql = "SELECT * FROM $TABLE_NAME";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // Convert the results to an array
    $data = array();
    while ($row = $result->fetch_assoc()) {
        $data[] = $row;
    }
    // Convert to JSON
    $json_data = json_encode($data, JSON_PRETTY_PRINT);
    // echo "Data retrieved successfully:\n";
    // echo $json_data;

    // Optional: Save the JSON output to a file
    file_put_contents('output.json', $json_data);
    // echo "JSON data saved to 'output.json'.\n";
} else {
    // echo "No data found in the table.\n";
}

$conn->close();
?>
