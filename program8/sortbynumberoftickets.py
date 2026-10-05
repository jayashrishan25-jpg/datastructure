# Movie Ticket Booking sorted by Number of Tickets

bookings = [
    ["Jay", "Leo", 5],
    ["Ravi", "Jailer", 2],
    ["Anu", "Master", 4],
    ["Priya", "Vikram", 1],
    ["Kumar", "Beast", 3]
]

def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]

    left = [x for x in data[1:] if x[2] < pivot[2]]
    right = [x for x in data[1:] if x[2] >= pivot[2]]

    return quick_sort(left) + [pivot] + quick_sort(right)


bookings = quick_sort(bookings)

print("Bookings sorted by Number of Tickets:")

for booking in bookings:
    print("Name:", booking[0],
          "Movie:", booking[1],
          "Tickets:", booking[2])