price = float(input("Please type in a price:"))

dinars=int(price)
Centimes = round((price - dinars) * 100)  # Get the decimal part as an integer
print(f"Dinars", dinars)
print(f"Centimes", Centimes)

