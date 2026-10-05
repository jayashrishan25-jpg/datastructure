# Movie Ticket Booking using Quick Sort

bookings = [
    [105, "Raj", 3],
    [102, "Kumar", 2],
    [101, "Anu", 4],
    [104, "Priya", 1],
    [103, "Arun", 2]
]

def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]

    left = [x for x in data[1:] if x[0] < pivot[0]]
    right = [x for x in data[1:] if x[0] >= pivot[0]]

    return quick_sort(left) + [pivot] + quick_sort(right)


bookings = quick_sort(bookings)

print("Sorted Booking Details:")

for booking in bookings:
    print("Ticket ID:", booking[0],
          "Name:", booking[1],
          "Tickets:", booking[2])