import random

def intro():

    print("Lemonade Stand is a business simulation game.")
    print("This game was originally created in 1973 by Bob Jamison.")
    print()
    print(" Hi! Welcome to Lemonsville, California!")
    print("In this small town, you are in charge of")
    print("running your own lemonade stand. You can")
    print("compete with as many other people as you")
    print("wish, but how much profit you make is up")
    print("to you (the other stands' sales will not")
    print("affect your business in any way). If you")
    print("make the most money, You're The Winner!!")
    print()
    print("Are you starting a new game? (Yes or No)")
    NewGame = str(input("Type your answer and hit return -->     "))

    if NewGame in ["yes","y","Yes","Y","YES"]:
        print("To manage your lemonade stand, you will ")
        print("need to make these decisions every day: ")
        print()
        print("1. How many glasses of lemonade to make ")
        print("   (only one batch is made each morning)")
        print()
        print("2. How many advertising signs to make   ")
        print("   (the signs cost fifteen coins each)  ")
        print()
        print("3. What price to charge for each glass  ")
        print()
        print("You will begin with 200 coins (assets). ")
        print("because your mother gave you some sugar,")
        print("your cost to make lemonade is two coins ")
        print("a glass (this may change in the future).")

    if NewGame in ["no","n","No","N","NO"]:
        print("You exited the game!")

def get_weather():
    weather = ["hot and dry","sunny","cloudy","rainy","thundery","snowy and icy"]
    return random.choice(weather)

def possible_customers_weather(weather, advertisements, price):
    
    #Hot and Dry

    if weather == "hot and dry" and 1 <= advertisements <= 5:
        possible_customers = random.randint(20, 45) + 10
    elif weather == "hot and dry" and 6 <= advertisements <= 10:
        possible_customers = random.randint(20, 45) + 25
    elif weather == "hot and dry" and advertisements >= 11:
        possible_customers = random.randint(20, 45) + 40
    else:
        possible_customers = random.randint(20, 45)

    #Sunny

    if weather == "sunny" and 1 <= advertisements <= 5:
        possible_customers = random.randint(10, 35) + 10
    elif weather == "sunny" and 6 <= advertisements <= 10:
        possible_customers = random.randint(10, 35) + 25
    elif weather == "sunny" and advertisements >= 11:
        possible_customers = random.randint(10, 35) + 40
    else:
        possible_customers = random.randint(10, 35)

    #Cloudy

    if weather == "cloudy" and 1 <= advertisements <= 5:
        possible_customers = random.randint(5, 15) + 1
    elif weather == "cloudy" and 6 <= advertisements <= 10:
        possible_customers = random.randint(5, 15) + 3
    elif weather == "cloudy" and advertisements >= 11:
        possible_customers = random.randint(5, 15) + 5
    else:
        possible_customers = random.randint(5, 15)

    #Rainy

    if weather == "rainy" and 1 <= advertisements <= 5:
        possible_customers = random.randint(5, 10) + 1
    elif weather == "rainy" and 6 <= advertisements <= 10:
        possible_customers = random.randint(5, 10) + 3
    elif weather == "rainy" and advertisements >= 11:
        possible_customers = random.randint(5, 10) + 5
    else:
        possible_customers = random.randint(5, 10)

    #Thundery

    if weather == "thundery" and 1 <= advertisements <= 5:
        possible_customers = random.randint(1, 5) + 1
    elif weather == "thundery" and 6 <= advertisements <= 10:
        possible_customers = random.randint(1, 5) + 3
    elif weather == "thundery" and advertisements >= 11:
        possible_customers = random.randint(1, 5) + 5
    else:
        possible_customers = random.randint(1, 5)

    #Snowy and Icy

    if weather == "snowy and icy" and 1 <= advertisements <= 5:
        possible_customers = random.randint(1, 3) + 1
    elif weather == "snowy and icy" and 6 <= advertisements <= 10:
        possible_customers = random.randint(1, 3) + 3
    elif weather == "snowy and icy" and advertisements >= 11:
        possible_customers = random.randint(1, 3) + 5
    else:
        possible_customers = random.randint(1, 3)

    multiplier = 1 - ((price - 4) / 4)

    return int(possible_customers * multiplier)
        
def player_input(assets):
    
    while True:
        print("1 glass (2 coins each)")
        amount = int(input("Number of glasses to make: "))
        print("1 advertisement (15 coins each)")
        advertisements = int(input("Number of advertisements to make: "))
        print("Price per glass is your choice")
        price = int(input("How many coins per glass: "))

        cost = amount * 2 + advertisements * 15

        if cost < assets:
            return amount, advertisements, price
        
        else:
            print("Cost exceeds Assets. Enter a valid response!")

def player_profit(price, advertisements, amount):
    
    profit = (price * amount) - ((amount * 2) + (advertisements * 15))
    return profit

def day():
    day = 1
    assets = 200
    
    while assets > 0:
        weather = get_weather()
        print(f"It is day {day} today!")
        print(f"The weather is {weather} today!")
        print(f"Your current assets are {assets} coins!")

        glasses_made, advertisements, price = player_input(assets)
        buyers = possible_customers_weather(weather, advertisements, price)
        if buyers > glasses_made:
            buyers = glasses_made

        profit = player_profit(price, advertisements, buyers)
        assets = assets + profit

        print()

        print(f"You made {glasses_made} cups of lemonade today!")
        print(f"You sold {buyers} cups for {price} coins each!")
        print(f"Your total profit was {profit}!")
        print(f"You have {assets} coins left in your assets!")

        continuethegame = str(input("Do you want to proceed to the next day (Yes or No): "))

        if continuethegame in ["no","n","No","N","NO"]:
            break
    
        day += 1

intro()

day()

print("You ended the game! Game is over!")