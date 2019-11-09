# Creating a List with   
List = ['Hello world'] 
print(List) 
  
# Creating a List with 
# the use of multiple values 
List = ["apple", "orange", "mango"] 
print("\nList containing multiple values: ") 
print(List[0])  
print(List[2]) 
  
# Creating a Multi-Dimensional List 
# (By Nesting a list inside a List) 
List = [['apple', 'orange'] , ['mango']] 
print("\nMulti-Dimensional List: ") 
print(List) 


# Creating a List with  
# mixed type of values 
# (Having numbers and strings) 
List = [1, 2, 'apple', 4, 'orange', 6, 'mango'] 
print("\nList with the use of Mixed Values: ") 
print(List) 

# Creating a List 
List = []
# Addition of Elements 
# in the List 
List.append(1) 
List.append(2) 
List.append(4) 
print("\nList after Addition of Three elements: ") 
print(List) 

# Adding elements to the List 
# using Iterator 
for i in range(1, 4): 
	List.append(i) 
print("\nList after Addition of elements from 1-3: ") 
print(List) 

# Adding Tuples to the List 
List.append((5, 6)) 
print("\nList after Addition of a Tuple: ") 
print(List) 

# Addition of List to a List 
List2 = ['99', '100'] 
List.append(List2) 
print("\nList after Addition of a List: ") 
print(List) 
  
# Removing elements from List 
# using Remove() method 
List.remove(5) 
List.remove(6) 
print("\nList after Removal of two elements: ") 
print(List) 
  
Sliced_List = List[:-1] 
print("\nElements sliced till 1st element from last: ") 
print(Sliced_List) 

