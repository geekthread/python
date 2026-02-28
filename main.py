name=input("What is your name? ")
city=input("Where do you live? ") 
print(len(name))
print(len(city))
print(name[0:5])
print(name[:5])
print(name[2:])
"""print("Hello my name is " + name.lower() + " and I live in " + city.lower() + ". Nice to meet you!") """
message="Hello my name is " + name.lower() + " and I live in " + city.lower() + ". Nice to meet you!"
print(message)
print("Count of ankit in message is: " + str(message.count("ankit")))
print("Index of the first occurrence of ankit in message is: " + str(message.find("ankit")))
message=message.replace("ankit", "Tathya")
print("Replace ankit with Tathya: " + message)
message=message.c