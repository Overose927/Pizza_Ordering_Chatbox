#James Smidt
#CIS110 Pizza Ordering Chatbot
#Week 6

print("Hello, my name is Alex, your virtual assistant.I will help you order a pizza")
print("I am going to ask you a few questions. After typing an answer, press enter.")
userName = input("\nEnter your name:  ")
while len(userName) == 0:
    userName = input("Name cannot be blank! Please enter your name:  ")
if userName.lower() == "james smidt":
    print(f"\nWelcome back, {userName}. Let's order a pizza!")
else:
    print(f"\nHello, {userName}. Nice to meet you!")
keepGoing = "y"
while keepGoing.lower() == "y":
    size = input("\nWhat size do you wnat? Enter small, medium, or large:  ")
    while size.lower() not in ["small", "medium", "large"]:
        size = input("\nInvalid value! Please enter small, medium, or large:  ")
    flavor = input("\nEnter the flavor of pizza:  ")
    while len(flavor) == 0:
        flavor = input("\nFlavor cannot be blank! Please enter a flavor:  ")
    crustType = input("\nWhat crust type would you like?:  ")
    while len(crustType) == 0:
        crustType = input("\nCrust type cannot be blank! What type of crust would you like?:  ")
    while True:
        try: 
            quantity = int(input("\nHow many of these do you want to order?  Enter a numeric value:  "))
            break
        except ValueError:
            print("\nValue not recognized.  Please enter a numeric value:  ")
    method = input("\nIs this carryout or delivery?:  ")
    while method.lower() not in ["carryout", "delivery"]:
        method = input("\nInvalid value! Please enter carryout or delivery:  ")
    if method.lower() == "delivery":
        deliveryFee = 5
    else:
        deliveryFee = 0
    salesTax = 1.1
    if size.lower() == "small":
        pizzaCost = 8.99
    elif size.lower() == "medium":
        pizzaCost = 14.99
    elif size.lower() == "large":
        pizzaCost = 17.99
    total = (pizzaCost * quantity) * salesTax + deliveryFee
    print("=" *10)
    print(f"Thank you, {userName}, for your order!")
    print(f"Your {quantity} {size} {flavor} pizza(s) with {crustType} crust costs ${total:,.2f}.")
    if total >= 50:
        print("\nCongratulations! You've been awarded a $10 off coupon for your next order!")
    else:
        print("\nOrders over $50 will receive a free $10 off coupon!")
    print("=" * 10)
    print("\nOrder has been recieved.  ETA 3 minutes!")
    for min in range(3,0,-1):
        print(min, "minutes remaining!")
        for seconds in range(60,0,-1):
            print(seconds, end= "\r")
            import time
            time.sleep(3)
    print("\nOrder is ready!")
    keepGoing = input("\nDo you want to place another order? Enter y or n:  ")
    while keepGoing.lower() not in ["y", "n"]:
        keepGoing = input("\nInvalid Value: Enter y or n:  ")