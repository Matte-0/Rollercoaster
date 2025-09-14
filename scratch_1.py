print("Welcome to the rollercoaster!")
height = int(input("Please enter your height in cm: "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Please enter your age: "))

    if age <= 12:
        bill = 5
        print("For children ticket costs $5.")
    elif 12 < age < 18:
        bill = 7
        print("For teens ticket costs $7.")
    else:
        bill = 12
        print("For adults ticket costs $12.")

    answer = input("Do you want to take a photo? Type yes or no: ")
    if answer.lower() == "yes":
        bill += 3
    print(f"You need to pay ${bill}.")
else:
    print("You can't ride the rollercoaster!")



