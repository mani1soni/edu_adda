"""a program that takes input from the user and when the user press enter
 to quit the program gives the sum of all even numbers and the sum of
 all odd numbers."""
even = []
odd = []
while 1:
    x = input("Please enter a number and press enter or just enter to exit: ")
    if x == "":
        break
    elif int(x) % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

print(even)
print(odd)
AddEven = 0
AddOdd = 0
for number in even:
    AddEven = AddEven + int(number)
for number in odd:
    AddOdd = AddOdd + int(number)

print("Sum of even number: ", str(AddEven))
print("Sum of odd number: ", str(AddOdd))
