print("Welcome to the tip calculator")


bill = float(input("What was the total bill? $"))

tip = float(input("What percent would you like to tip? 10, 12, or 15?\n"))

split = float(input("How many people to split the bill?\n"))
            
tip_amount = tip * .01

total_tip = bill * tip_amount

total = total_tip + bill

total_each = "%.2f" % round((total / split),2)

print(f"The total each person should pay is ${total_each}")