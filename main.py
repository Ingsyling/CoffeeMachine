
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0


# TODO: 1 create a function to print report
def report():
    print(f"water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


# TODO: 2 create a function to check if the resources for the selected coffee is enough
def is_resource_enough(ingredients_list):
    """returns true if ingredient available is sufficient to make the selected coffee"""
    for item in ingredients_list:
        if resources[item] < ingredients_list[item]:
            print(f"Sorry, there is not enough {item}")
            return False
        return True


# TODO: 3 create a function to ask the user to pay and process the user's money also check if the payment is enough,
#  return change where necessary, and add the cost to our money
def process_payment(item_cost):
    customer_money = int(input("how many quarters?: "))*0.25
    customer_money += int(input("how many dime?: "))*0.1
    customer_money += int(input("how many nickel?: "))*0.05
    customer_money += int(input("how many penny?: "))*0.01
    if customer_money < item_cost:
        print(f"Sorry,that is not enough money, take your ${customer_money}")
        return False

    elif customer_money > item_cost:
        change = round(customer_money - item_cost, 2)
        print(f"Here is your ${change} change.")
        global money
        money += item_cost
    return True


# TODO: 4 make a function to the coffee
def make_coffee(item_name, ingredients):
    """enter tne coffee name, the ingredients_list, and the resources"""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is our {item_name}☕, enjoy.")


# TODO: 5 make the actual game
go_on = True
while go_on:
    choice = input("What coffee do you want:espresso, latte, or cappuccino: ").lower()
    if choice == "off":
        go_on = False
    elif choice == "report":
        report()
    elif choice == "latte" or choice == "cappuccino" or choice == "espresso":
        ingredient_list = MENU[choice]["ingredients"]
        cost = MENU[choice]['cost']
        if is_resource_enough(ingredient_list):
            if process_payment(cost):
                make_coffee(choice, ingredient_list)
    else:
        print("Please, make a valid input")












