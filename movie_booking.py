# Simple Movie Ticket Booking

# List of movies. Each movie is a dictionary with name, price, and seats.
movies = [
    {"name": "Avengers", "price": 12, "seats": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
    {"name": "Lion King", "price": 10, "seats": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
    {"name": "Inception", "price": 11, "seats": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
]

def show_movies():
    print("\n--- Available Movies ---")
    for i in range(len(movies)):
        print(f"{i + 1}. {movies[i]['name']} - ${movies[i]['price']}")

def show_seats(movie_index):
    print("\nSeats (0 = Empty, 1 = Booked):")
    print(movies[movie_index]['seats'])

def book_ticket():
    show_movies()
    try:
        choice = int(input("Choose a movie number: ")) - 1
        
        if choice < 0 or choice >= len(movies):
            print("Invalid movie choice!")
            return

        show_seats(choice)
        seat_num = int(input("Enter seat number (1-10): ")) - 1
        
        if seat_num < 0 or seat_num >= 10:
            print("Invalid seat number!")
            return
            
        if movies[choice]['seats'][seat_num] == 1:
            print("Sorry, that seat is already booked.")
        else:
            movies[choice]['seats'][seat_num] = 1
            print("\nBooking successful!")
            print(f"Total cost: ${movies[choice]['price']}")
            
    except ValueError:
        print("Please enter numbers only.")


while True:
    print("\n1. Book Ticket")
    print("2. Exit")
    user_input = input("Enter option: ")
    
    if user_input == '1':
        book_ticket()
    elif user_input == '2':
        print("Goodbye!")
        break
    else:
        print("Invalid option, try again.")
