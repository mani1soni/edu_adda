"""a program that takes input from the user and when the user press enter
 to quit the program gives the sum of all even numbers and the sum of
 all odd numbers."""
even = [] #empty list
odd = []
while 1:
    x = input("Please enter a number and press enter or just enter to exit: ")
    if x == "":
        break
    elif int(x) % 2 == 0:
        even.append(x) #add number into even list
    else:
        odd.append(x)  #add number into odd list

print(even) #print the lists

print(odd) #print the lists

AddEven = 0 #blank numbers to count
AddOdd = 0 #blank numbers to count
for number in even: #
    AddEven = AddEven + int(number) #add 1 to the count
for number in odd:
    AddOdd = AddOdd + int(number) #add 1 to the count

print("Sum of even number: ", str(AddEven)) #print results
print("Sum of odd number: ", str(AddOdd)) #print results
