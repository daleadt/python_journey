#examples

#  The Sardar Patel Cricket Stadium, Motera has the following rates for different types of seats:
# •	Ordinary – 2500
# •	Pavillion – 3500
# •	Upper Pavillion – 4500
# •	Commentary Box – 6000
# •	VIP – 8000
# i.	They are giving 10% discount for online booking and 8% discount for advance booking and no discount is given for booking
    #   on match day from ticket window.
# ii.	Ask user to enter the booking type like online, advance or window booking.
# iii.	Ask user to select the types of seats.
# iv.	Compute the amount and print the ticket with proper format.



ordinary = 2500
pavillion = 3500
upper_pavillion = 4500
commentary_box = 6000
vip = 8000

booking_type = input("Enter the booking type (online, advance, window): ")
seat_type = input("Enter the type of seat (ordinary, pavillion, upper_pavillion, commentary_box, vip): ")
no_of_seats = int(input("Enter the number of seats: "))


if seat_type == "ordinary":
    amount = ordinary
elif seat_type == "pavillion":
    amount = pavillion  
elif seat_type == "upper_pavillion":
    amount = upper_pavillion
elif seat_type == "commentary_box":
    amount = commentary_box
elif seat_type == "vip":
    amount = vip 
else:
    print("Invalid seat type")
    exit()

if booking_type == "online":
    final_amount = amount - (amount * 0.10)
elif booking_type == "advance":
    final_amount = amount - (amount * 0.08)
elif booking_type == "online+ advance":
    final_amount = amount - (amount * 0.18)
else:
    print("Invalid booking type")
    exit()
final_amount *= no_of_seats


print("--------TICKET BOOKING DETAILS--------")
print("Booking Type:",    booking_type)
print("Seat Type:",       seat_type)
print("Ticket Price:",    amount)
print("Number of Seats:", no_of_seats)
print("Final Amount:",  final_amount)
print("---------------------------------------")













































