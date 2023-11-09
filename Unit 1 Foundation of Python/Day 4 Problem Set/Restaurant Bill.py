drink = float(input("How much was the drink: "))
appetizer = float(input("How much was the appetizer: "))
entree = float(input("How much was the entree: "))
dessert = float(input("How much was the dessert: "))

subtotal = drink + appetizer + entree + dessert

tip_rate = int(input("How much is the tip: "))

tip = subtotal * tip_rate / 100

total_cost = subtotal + tip

print("Bill Summary: ")
print(f"Subtotal: {subtotal} Dollars")
print(f"Tip ({tip_rate}%): {tip} Dollars")
print(f"Total Cost: {total_cost} Dollars")

