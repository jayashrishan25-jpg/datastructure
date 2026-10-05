# Movie Booking sorted by Customer Name

bookings = [
    ["Priya", "Leo", 2],
    ["Arun", "Jailer", 3],
    ["Kumar", "Vikram", 1],
    ["Anu", "Master", 4]
]

def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]

    left = [x for x in data[1:] if x[0].lower() < pivot[0].lower()]
    right = [x for x in data[1:] if x[0].lower() >= pivot[0].lower()]

    return quick_sort(left) + [pivot] + quick_sort(right)


bookings = quick_sort(bookings)

print("Bookings sorted by Customer Name:")

for booking in bookings:
    print("Name:", booking[0],
          "Movie:", booking[1],
          "Tickets:", booking[2])