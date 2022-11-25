print("Welcome to the tip calculator!")
bill = float(input("How much it's the bill ? "))
people = int(input("How many people to split the bill? "))
tip = int(input("Tip percentage (10,12,15)? "))

bill_people = bill/people
tip_amount = (tip/100)+1

final_bill = round(bill_people * tip_amount,2)


print(f"Each person should pay: ${final_bill}")