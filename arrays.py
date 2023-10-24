courses = ["MIT", "Cybersecurity", "Data science"]
print(courses)

# Accessing an element in an array
print(courses[1])

#Looping through an array
for course in courses:
    print(course)

#Adding an element in an array
courses.append("Android development")
print(courses)


#Removing an element from an array
courses.remove("MIT")
print(courses)