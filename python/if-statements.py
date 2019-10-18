# if statements will help your program to more or less "decide" between two or more options by testing
# a statement.

# Example 1:
list = [1, 2, 3]

if list[0] == 1:
    print("first element of the list is 1")

# the program checks if the statement(in this case: if the first element of the list is one) is True (with ==)
# if the statement is True the program will do the code execute the code beneath the if clause.
# You can also check if the statement is False (with !=)

if list[0] != 1:
    print("the first element of the list is not 1")

# The if-else-statements let your program do thing even when the statement is wrong. So the program will do either the
# code beneath the if- or beneath the else-statement. So the program will do something in every case.

# Example 2:
for i in list:
    if list[i-1] == 1:
        print("the "+str(i)+". element of the list is 1")
    else:
        print("the " + str(i) + ". element of the list is not 1")



# the third option of if statements is the elif. With this option you can test more than one statement.

# Example 3:
for i in list:
    if list[i-1] == 1:
        print("the "+str(i)+". element of the list is 1")
    elif list[i-1] == 2:
        print("the " + str(i) + ". element of the list is 2")
    elif list[i-1] == 3:
        print("the " + str(i) + ". element of the list is 3")

# The fourth example allows for a loop to be exited.

# Example 3:
for i in list:
    if list[i-1] == 1:
        print("the "+str(i)+". element of the list is 1")
    elif list[i-1] == 2:
        print("the " + str(i) + ". element of the list is 2")
    elif list[i-1] == 3:
        print("This loop only supports searching 2 items in a list. Exiting loop...")
        break
