print("Welcome to tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 , or 15? "))
split = int(input("How many people to split the bill? " ))

each_person = ((bill * (1 + tip / 100)) / split)
each_person = round(each_person, 2)

print(f"Each person should pay: ${each_person} ")