number = int(input("Please Enter any Number: "))
total = 0
value = 1
while (value <= number):
    total = total + value
    value = value + 1
print("The Sum of Natural Numbers from 1 to {0} =  {1}".format(number, total))