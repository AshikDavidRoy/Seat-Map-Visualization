document.addEventListener('DOMContentLoaded', () => {
    const seatMapDiv = document.getElementById('seat-map');

    // Function to fetch seat data and render the seat map
    function fetchSeats() {
        fetch('/seats')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(seats => {
                seatMapDiv.innerHTML = ''; // Clear existing seats
                if (seats.length === 0) {
                    seatMapDiv.textContent = 'No seats available.';
                    return;
                }
                seats.forEach(seat => {
                    const seatDiv = document.createElement('div');
                    seatDiv.className = `seat ${seat.status}`; // Set seat status class
                    seatDiv.textContent = `${seat.rownumber}-${seat.seat_number}`;
                    seatDiv.addEventListener('click', () => updateSeat(seat.rownumber, seat.seat_number, seat.status));
                    seatMapDiv.appendChild(seatDiv);
                });
            })
            .catch(error => {
                console.error('Error fetching seat data:', error);
                seatMapDiv.textContent = 'Error fetching seat data. Please try again.';
            });
    }

    // Function to update seat status
    function updateSeat(rownumber, seat_number, currentStatus) {
        const newStatus = currentStatus === 'available' ? 'selected' : 'available'; // Toggle selection
        fetch(`/seats/${rownumber}/${seat_number}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ status: newStatus }),
        })
        .then(response => {
            if (response.ok) {
                fetchSeats(); // Refresh seat map after updating
            } else {
                console.error('Error updating seat:', response.statusText);
            }
        })
        .catch(error => console.error('Error updating seat:', error));
    }

    // Initial fetch to load seats
    fetchSeats();
});
