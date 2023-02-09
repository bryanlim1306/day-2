#Day 2 Project - Tip Calculator
# Returns how much to tip for a group
n = int(input("How many people in your group?" ))
b = int(input("How much is the bill?" ))
t = int(input("What percentage tip?" ))/100

amount = (b/n) * (1+t)
print(round(amount, 2))
