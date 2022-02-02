#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator")
bill = input("What was the total bill? $")
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
tips = (tip / 100)
people = input("How many people to split the bill? ")

pay = ((float(bill)) / int(people))
each_pay = pay * tips
# total_pay = round(pay + each_pay, 2)
total_pay = '{:.2f}'.format(pay + each_pay)

print(f"Each person should pay: ${total_pay}")