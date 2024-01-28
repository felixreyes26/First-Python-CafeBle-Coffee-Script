#Let's build robot Barista!!



print("Hello, welcome to CafeBle Coffee!" + "\n\n")


name = input("What is your name?\n")


print("Hello " + name + ", thank you so much for coming in today.\n")


menu = "Black Coffee, Espresso, Latte, Cappucino"


order = input(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu + "\n")

print()

price = 8

quantity = input("Sounds good, How many " + order + "'s would you like to order " + name + "\n")

total = price * int(quantity)

print()

print("Thank you, Your total will be $" + str(total) + " dollers\n")

Payment = input("Whould you like to pay in cash or card.\n")

print()

print("Awesome, We'll have your " + quantity + " " +  order + " ready in a moment. " + name)

