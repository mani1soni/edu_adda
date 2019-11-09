print("for loops")
### basic for loop
datas = ["a", "b", "c"]
print("will print all value in datas a,b,c")
for x in datas:
    print(x)


## basic range for loop

print("print out the numbers 0,1,2,3,4")
for i in range(5):
    print(i)

print("print out 4,5,6")
for i in range(4,7):
    print(i)

print("print out the numbers 0,2,4,6,8")
for i in range(0,10,2):
    print(i)


## while loops

print("while loops")
print("print out the number 0,1,2")
counter = 0
while counter < 3:
    print(counter)
    counter += 1



print("break and continue")

print("will only print 0,1,2,3,4,5")
counter = 0
while counter < 10:
    print(counter)
    if counter == 5:
        break
    counter +=1


print("will only printt even number")
for i in range(11):
    if i%2 == 1:
        continue
    print(i)

print("use else clause with loop")
for i in range(5):
    print(i)
else:
    print("counter reach", i)

print("use else clause with loop")
for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("will not be printed because stop using break")

