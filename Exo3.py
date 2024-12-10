def calculate_discount():
    
    total_amount = float(input("Total amount: "))
    number_of_items = int(input("Number of items: "))
    day_of_week = input("Day of the week: ").strip().capitalize()

    
    if day_of_week in ["Saturday", "Sunday"]:
        discount = 0.20  
        discount = 0.10 

 
    if number_of_items > 5:
        discount += 0.05  

    
    discounted_price = total_amount * (1 - discount)

    # Print the result
    print(f"Total price after discount: {discounted_price:.1f} dinars")

# Run the program
calculate_discount()
