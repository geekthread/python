list_1=['History','Math','Physics','CompSci']
list_2=list_1  # This creates a reference to the same list, not a copy
print(list_1)  # Output: ['History', 'Math', 'Physics', 'CompSci']
print(list_2)  # Output: ['History', 'Math', 'Physics', 'CompSci']  

list_1[0] = 'Art'  # Modifying list_1 will also affect list_2 since they reference the same list
print(list_1)  # Output: ['Art', 'Math', 'Physics', 'CompSci']


#list_1.append('Art')  # Modifying list_1 will also affect list_2 since they reference the same list
print(list_1)  # Output: ['History', 'Math', 'Physics', 'CompSci', 'Art']
print(list_2)  # Output: ['History', 'Math', 'Physics', 'CompSci', 'Art']  (list_2 also shows the change

# Immutable data type: Tuple
tuple_1=('History','Math','Physics','CompSci')
tuple_2=tuple_1  # This also creates a reference to the same tuple, but since tuples are immutable, it behaves differently than lists
print(tuple_1)  # Output: ('History', 'Math', 'Physics', 'CompSci')
print(tuple_2)  # Output: ('History', 'Math', 'Physics', 'CompSci') 



print(tuple_1)
#tuple_1 += ('Art',)  # This creates a new tuple and assigns it to tuple_1, tuple_2 remains unchanged

tuple_1 = tuple_1 + ('Art',)  # This creates a new tuple and assigns it to tuple_1, tuple_2 remains unchanged

print(tuple_1)  # Output: ('History', 'Math', 'Physics', 'CompSci', 'Art')
print(tuple_2)  # Output: ('History', 'Math', 'Physics', 'CompSci')  (tuple_2 remains unchanged)    
