name = input("Please enter your name: ")
if name != "VIP" :
    nb_tickets=int(input("How many tickets would you like to buy?"))

    print(f"the Total cost is ", nb_tickets*46.5 )
    print("Enjoy ur tickets")
else:
    print("Enjoy the show for free!")