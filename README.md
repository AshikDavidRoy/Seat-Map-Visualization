# Seat-Map-Visualization
### HTML Structure

```html
<!DOCTYPE html>
<html lang="en">
```
- This line declares the document type and defines the language of the document as English.

```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Movie Theater Seat Map</title>
```
- **`<head>`**: Contains metadata and links to resources.
- **`<meta charset="UTF-8">`**: Sets the character encoding for the document to UTF-8.
- **`<meta name="viewport" content="width=device-width, initial-scale=1.0">`**: Ensures proper scaling on mobile devices.
- **`<title>Movie Theater Seat Map</title>`**: Sets the title of the webpage.

```html
<style>
```
- This opens a `<style>` block where CSS styles will be defined.

### CSS Styles

The CSS section defines styles for the seat map, rows, seats, the booking form, and the overlay. Here are key parts:

```css
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    margin: 0;
    padding: 20px;
}
```
- Styles the body with a font, background color, and padding.

```css
h1 {
    color: #333;
    text-align: center;
}
```
- Styles the main heading (h1) with a text color and centers it.

```css
#seat-map {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 20px;
}
```
- Centers the seat map and adds a margin at the bottom.

```css
.row {
    display: flex;
    justify-content: center;
    margin: 5px 0;
}
```
- Styles each row to be flex containers, centering their content with a vertical margin.

```css
.seat {
    width: 40px;
    height: 40px;
    margin: 0 5px;
    text-align: center;
    line-height: 40px;
    border-radius: 5px;
    border: 1px solid #ccc;
    cursor: pointer;
    transition: background-color 0.3s;
}
```
- Styles each seat with dimensions, borders, and rounded corners. The cursor changes to a pointer on hover.

```css
.seat.available {
    background-color: #4CAF50; /* Green for available */
}
```
- Colors available seats green.

```css
.seat.unavailable {
    background-color: #f44336; /* Red for unavailable */
    cursor: not-allowed;
}
```
- Colors unavailable seats red and changes the cursor to indicate they can't be selected.

```css
.seat.selected {
    background-color: #2196F3; /* Blue for selected */
}
```
- Colors selected seats blue.

```css
#booking-form {
    display: none;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: #fff;
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 20px;
    width: 300px;
    box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.3);
    z-index: 100;
}
```
- Styles the booking form as a fixed popup, centered on the screen with a shadow for depth.

```css
#overlay {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    z-index: 50;
}
```
- Styles an overlay behind the booking form, giving it a darkened background to focus on the form.

### Body Content

```html
<body>
    <h1>Movie Theater Seat Map</h1>
    <div id="seat-map"></div>
    <button onclick="openBookingForm()" id="book-btn" disabled>Book Selected Seats</button>
```
- The body contains a title, a div for the seat map, and a button to book selected seats.

### Popup Form

```html
<div id="overlay" onclick="closeBookingForm()"></div>
<div id="booking-form">
    <h2>Booking Form</h2>
    <label for="teacher-name">Teacher's Name:</label>
    <input type="text" id="teacher-name" placeholder="Enter teacher's name">
    
    <div id="student-names-container"></div>
    
    <input type="button" value="Confirm Booking" onclick="confirmBooking()">
    <input type="button" value="Cancel" onclick="closeBookingForm()">
</div>
```
- Creates an overlay and a booking form with inputs for the teacher's name and student names. It also includes buttons to confirm the booking or cancel.

### JavaScript Functionality

```javascript
<script>
    // Sample seat data
    const sampleSeatsData = {
        "seats": [
            {"row_number": 1, "seat_number": 1, "status": "available"},
            {"row_number": 1, "seat_number": 2, "status": "available"},
            {"row_number": 1, "seat_number": 3, "status": "available"},
            {"row_number": 1, "seat_number": 4, "status": "unavailable"},
            {"row_number": 1, "seat_number": 5, "status": "available"},
            {"row_number": 2, "seat_number": 1, "status": "available"},
            {"row_number": 2, "seat_number": 2, "status": "unavailable"},
            {"row_number": 2, "seat_number": 3, "status": "available"},
            {"row_number": 2, "seat_number": 4, "status": "available"}
        ]
    };
```
- Declares a JavaScript object containing sample seat data with their row numbers, seat numbers, and availability status.

```javascript
const seatMap = document.getElementById('seat-map');
let selectedSeats = [];
```
- Retrieves the seat map div element and initializes an array to hold selected seats.

```javascript
sampleSeatsData.seats.forEach(seat => {
```
- Loops through each seat in the sample data.

```javascript
let rowDiv = document.getElementById(`row-${seat.row_number}`);
if (!rowDiv) {
    rowDiv = document.createElement('div');
    rowDiv.className = 'row';
    rowDiv.id = `row-${seat.row_number}`;
    seatMap.appendChild(rowDiv);
}
```
- Checks if a row div exists for the seat's row number; if not, it creates a new div for that row and appends it to the seat map.

```javascript
const seatDiv = document.createElement('div');
seatDiv.className = `seat ${seat.status}`;
seatDiv.textContent = `${seat.seat_number}`;
seatDiv.onclick = () => toggleSeatSelection(seatDiv, seat);
```
- Creates a seat div, assigns its class based on availability, sets its text to the seat number, and assigns an `onclick` event to toggle selection.

```javascript
rowDiv.appendChild(seatDiv);
```
- Appends the seat div to the corresponding row div.

### Seat Selection Logic

```javascript
function toggleSeatSelection(seatDiv, seat) {
    if (seat.status === "available") {
        seatDiv.classList.toggle('selected');
        if (seatDiv.classList.contains('selected')) {
            selectedSeats.push(seat);
        } else {
            selectedSeats = selectedSeats.filter(s => s !== seat);
        }
        document.getElementById('book-btn').disabled = selectedSeats.length === 0;
    }
}
```
- **`toggleSeatSelection` function**: 
  - Checks if the seat is available.
  - Toggles the 'selected' class for the seat div.
  - Adds or removes the seat from the `selectedSeats` array based on its selection state.
  - Enables or disables the booking button depending on whether any seats are selected.

### Booking Form Logic

```javascript
function openBookingForm() {
    document.getElementById('overlay').style.display = 'block';
    document.getElementById('booking-form').style.display = 'block';
```
- **`openBookingForm` function**: 
  - Displays the overlay and booking form.

```javascript
const studentContainer = document.getElementById('student-names-container');
studentContainer.innerHTML = '';
```
- Resets the student names container to prepare for new input fields.

```javascript
selectedSeats.slice(1).forEach((_, index) => {
    const label = document.createElement('label');
    label.textContent = `Student ${index + 1} Name:`;
    const input = document.createElement('input');
    input.type = 'text';
    input.placeholder = `Enter Student ${index + 1}'s Name`;
    studentContainer.appendChild(label);
    studentContainer.appendChild(input);
});
```
- Dynamically creates input fields for student names based on the number of selected seats (excluding the teacher's seat).

```javascript
function closeBookingForm() {
    document.get

ElementById('overlay').style.display = 'none';
    document.getElementById('booking-form').style.display = 'none';
    selectedSeats = [];
    document.querySelectorAll('.seat.selected').forEach(seat => {
        seat.classList.remove('selected');
    });
    document.getElementById('book-btn').disabled = true;
}
```
- **`closeBookingForm` function**: 
  - Hides the booking form and overlay, clears the selected seats, and resets the booking button.

### Booking Confirmation Logic

```javascript
function confirmBooking() {
    const teacherName = document.getElementById('teacher-name').value;
    const studentNames = Array.from(document.querySelectorAll('#student-names-container input')).map(input => input.value);
```
- **`confirmBooking` function**: 
  - Retrieves the teacher's name and the names of the students from input fields.

```javascript
console.log(`Booking confirmed for ${teacherName}`);
console.log(`Students: ${studentNames.join(', ')}`);
```
- Logs the booking confirmation details in the console.

```javascript
closeBookingForm();
}
</script>
```
- Calls the `closeBookingForm` function to reset the form and hide it after confirmation.

### Summary

This code creates a simple movie theater seat map application, allowing users to select available seats, open a booking form, and confirm their bookings. It handles visual feedback for selected, available, and unavailable seats and provides a user-friendly interface for making reservations.
