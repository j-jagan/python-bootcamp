print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster")
    amount_to_pay = 0
    age = int(input("What is your age? "))
    if age < 12:
        amount_to_pay += 5
        print(f"Child tickets are ${amount_to_pay}")
    elif age >= 12 and age < 18:
        amount_to_pay += 7
        print(f"Youth ticket are ${amount_to_pay}")
    else:
        amount_to_pay += 12
        print(f"Adult ticket are ${amount_to_pay}")

    wants_photo = input("Do you want photos? Type y for Yes and n for No: ")
    if wants_photo == 'y':
        amount_to_pay += 3
        print(f"The total bill is ${amount_to_pay}")
else:
    print("Sorry you have to grow taller before you can ride.")
