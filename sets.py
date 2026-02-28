courses = {"History", "Math", "Physics", "CompSci"}
#print(courses)  # Output: {'History', 'Math', 'Physics', 'ComSci'} (order may vary since sets are unordered)

art_courses = {"Art", "Design","History", "Math"}

print(courses.intersection(art_courses))  # Output: {'History', 'Math'} (common courses)

print(courses.difference(art_courses))  # Output: {'Physics', 'CompSci'} (courses in courses but not in art_courses)

print(art_courses.difference(courses))  # Output: {'Art', 'Design'} (courses in art_courses but not in courses)

print(courses.union(art_courses))  # Output: {'History', 'Math', 'Physics', 'CompSci', 'Art', 'Design'} (all unique courses from both sets)


print("Symmetric Difference:")
print(courses.symmetric_difference(art_courses))  # Output: {'Physics', 'CompSci', 'Art', 'Design'} (courses that are in either set but not in both)

print(courses.issubset(art_courses))  # Output: False (courses is not a subset of art_courses)


print(courses.issuperset(art_courses))  # Output: False (courses is not a superset of art_courses)


# Empty set list tuples

empty_set = set()  # This creates an empty set
print(len(empty_set))  # Output: set() (an empty set is represented as 'set

empty_list1 = []  # This creates an empty list
empty_list2 = list()  # This also creates an empty list
print(empty_list1)  # Output: []
print(empty_list2)  # Output: []

empty_tuple1 = ()  # This creates an empty tuple
empty_tuple2 = tuple()  # This also creates an empty tuple
print(empty_tuple1)  # Output: ()
print(empty_tuple2)  # Output: ()   