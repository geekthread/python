courses=["History","Math","Physics","CompSci"]
print(courses)
print(len(courses))    # Output: 4
print(courses[0])     # Output: 'History'
print(courses[1])     # Output: 'Math'
print(courses[2])     # Output: 'Physics'
print(courses[3])     # Output: 'CompSci'
print(courses[-1])    # Output: 'CompSci'
print(courses[-2])    # Output: 'Physics'
print(courses[-3])    # Output: 'Math'
print(courses[-4])    # Output: 'History'
print(courses[0:2])   # Output: ['History', 'Math']
print(courses[2:])    # Output: ['Physics', 'CompSci']
print(courses[:2])    # Output: ['History', 'Math']
print(courses[:])     # Output: ['History', 'Math', 'Physics', 'CompSci']

courses.append("Art")  # Add 'Art' to the end of the list
print(courses)  # Output: ['History', 'Math', 'Physics', 'CompSci', 'Art']

courses.insert(0, "Biology")  # Insert 'Biology' at index 0
print(courses)  # Output: ['Biology', 'History', 'Math', 'Physics', 'CompSci', 'Art']
courses_2 = ["Education", "Economics"]
courses.extend(courses_2)  # Extend the list with another list
print(courses)  # Output: ['Biology', 'History', 'Math', 'Physics', 'CompSci', 'Art', 'Education', 'Economics']

courses.remove("Math")  # Remove 'Math' from the list
print(courses)  # Output: ['Biology', 'History', 'Physics', 'CompSci', 'Art', 'Education', 'Economics']
courses.pop()  # Remove the last item from the list
print(courses)  # Output: ['Biology', 'History', 'Physics', 'CompSci', 'Art', 'Education']
courses.reverse()  # Reverse the order of the list
print(courses)  # Output: ['Education', 'Art', 'CompSci', '

# courses.sort()  # Sort the list in ascending order
# print(courses)  # Output: ['Art', 'CompSci', 'Education', '

# Not changing the original list, but creating a new sorted list
sorted_courses = sorted(courses)
print(sorted_courses)  # Output: ['Art', 'CompSci', 'Education', 'Education', 'CompSci', 'Art']
print(courses)  # Output: ['Education', 'Art', 'CompSci', 'Education', 'CompSci', 'Art']

#Index of an item in the list
print(courses.index("CompSci"))  # Output: 2
print(courses.index("Education"))  # Output: 0 (first occurrence of 'Education') 

# Check if an item is in the list
print("****Checking if an item is in the list****")
print("Math" in courses)  # Output: False
print("Art" in courses)   # Output: True


# Min and Max functions
numbers = [1,5,2,4,3]
print(min(numbers))  # Output: 1
print(max(numbers))  # Output: 5
print(sum(numbers))  # Output: 15
print(avg := sum(numbers) / len(numbers)) # Output: 3.0 (using the walrus operator to assign and print the average)


#Loops with lists
print("****Looping through the list****")
for course in courses:
    print(course)  # Output: Each course in the list printed on a new line

print ("****Looping with index using enumerate****")
for index, course in enumerate(courses):
    print(index, course)  # Output: Each index and corresponding course printed on a new line   


print ("****Looping with index using enumerate with index****")
for index, course in enumerate(courses, start=2):  # Start index    from 2 instead of 0
    print(index, course)  # Output: Each index and corresponding course printed on a new line  

print("****Joining the list into a string****")
courses_str = " - ".join(courses)  # Join the list into a string with ', ' as a separator
print(courses_str)  # Output: 'Education, Art, CompSci, Education, CompSci, Art'

print("****Checking the type of the joined string****")
print(type(courses_str))  #     Output: <class 'str'>


new_list = courses_str.split(" - ") # Split the string back into a list using ', ' as a separator (which matches the one used in join)

print(new_list)  # Output: ['Education, Art, CompSci, Education, CompSci, Art'] (the entire string is treated as one item in the list since the separator used in split does not match the one used in join)

