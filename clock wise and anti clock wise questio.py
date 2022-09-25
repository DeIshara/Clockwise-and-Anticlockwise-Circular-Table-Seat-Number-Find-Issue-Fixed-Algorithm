# clock wise and anti clock wise question. related who first find a seat

Seats = input("Enter number of seats: ")
is_build = True
try:
    seats = int(Seats)
except:
    is_build = False
    print("Invalid input number, Please input valid integer number of seats")
  
#clockwise_seats = [0, 1, 2, 3, 4]
#anticlockwise_seats = [0, 4, 3, 2, 1]
clockwise_seats =[]
anticlockwise_seats = [0]
i=0
if(is_build):
    while(i< seats):
        clockwise_seats.append(i)
        i+=1
    print("Clockwise seat numbers ",clockwise_seats)
    j=seats-1
    while(j>0):
        anticlockwise_seats.append(j)
        j-=1
    print("Anti clockwise seat numbers ",anticlockwise_seats)

    is_circulate = True
    seat_number_colokwise = 0
    seat_number_anti_colokwise = 0
    while (is_circulate): 
        seat_number_colokwise = seat_number_colokwise + 1
        seat_number_anti_colokwise = seat_number_anti_colokwise + 2
        if (seat_number_colokwise == seats ):
            seat_number_colokwise = 0
        if(seat_number_anti_colokwise == seats):
            seat_number_anti_colokwise = 0
        if (seat_number_anti_colokwise == seats+1):
            seat_number_anti_colokwise = 1
        if (clockwise_seats[seat_number_colokwise] == anticlockwise_seats[seat_number_anti_colokwise]):
            print("Clockwise and anti clockwise operations both get together seat number is:",
             clockwise_seats[seat_number_colokwise])
            is_circulate = False


