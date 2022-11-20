MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 400,
    "milk": 300,
    "coffee": 100,
}
game_end = False

def turn_off():
    global game_end
    game_end = True
    print("The machine was turned off")

money = 0

def report( ):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    print(f"Money {money}$")

def check_resourses(drink):
    user_water = MENU[drink]["ingredients"]["water"]
    user_coffee = MENU[drink]["ingredients"]["coffee"]
    user_milk = 0
    if drink == "cappuccino" or drink == "latte":
        user_milk = MENU[drink]["ingredients"]["milk"]
    if resources["milk"] - user_milk >= 0:
        if resources["water"] - user_water >=0:
            if resources["coffee"] - user_coffee >=0:
                return True
            else:
                print("Sorry, that's not enough coffee")
                return False
        else:
            print("Sorry, that's not enough water")
            return False
    else:
        print("Sorry, that's not enough milk")
        return False

def sum_coins(pennies, nickles, dimes, quarters):
    total = pennies+nickles+dimes+quarters
    return total

def check_coins(drink):
    global money, game_end
    cost_of_drink = MENU[drink]["cost"]
    if sum_coins(pennies_in_usd, nickles_in_usd, dimes_in_usd, quarters_in_usd) >= cost_of_drink:
        money += cost_of_drink
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
        if drink == "cappuccino" or drink == "latte":
            resources["milk"] -= MENU[drink]["ingredients"]["milk"]
        if sum_coins(pennies_in_usd, nickles_in_usd, dimes_in_usd, quarters_in_usd) - cost_of_drink >0:
            change = round((sum_coins(pennies_in_usd, nickles_in_usd, dimes_in_usd, quarters_in_usd) - cost_of_drink),2)
            print(f"Your change is {change}$")
        print(f"Here is your {drink}. Enjoy!")
    else:
        print("Sorry that\'s not enough money. Money refunded.")
        game_end = True

while not game_end:
    question = input("What would you like? Type espresso/latte/cappuccino: ")
    if question not in MENU.keys():
        if question == "report":
            report()
        elif question == "turn off":
            turn_off()
        else:
            print("Please, specify the correct drink ")
            question = input("What would you like? Type espresso/latte/cappuccino: ")
    else:
        if check_resourses(question):
            print("Please, insert coins.")
            pennies_in_usd = int(input("Pennies: ")) * 0.01
            nickles_in_usd = int(input("Nickles: ")) * 0.05
            dimes_in_usd = int(input("Dimes: ")) * 0.1
            quarters_in_usd = int(input("Quarters: ")) * 0.25
            check_coins(question)
        else:
            game_end  = True
















