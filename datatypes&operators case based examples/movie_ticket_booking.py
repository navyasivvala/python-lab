ticketcost=250
ticketsnumber=input("enter no of tickets booked")
a=int(ticketsnumber)
totalcost=ticketcost*a
if totalcost >= 500:
    print("you got 100 rupees coupon")
    totalcost=totalcost-100
    print("total cost is",totalcost)
else:
    print("total cost is",totalcost)
