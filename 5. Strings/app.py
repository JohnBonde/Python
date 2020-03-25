course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[:3])
print(course[0:])
print(course[:])

print(id(course))
print(id(course[0]))

message = "Python \"Programming"
print(message)

# \"
# \'
# \\
# \n - New line
# """ - Multiple lines

first = "Jack"
last = "Bonde"
full = first + " " + last
full = f"{first} {last}"
print(full)

print(course.upper())
print(course.lower())
print(course.title())
# Remove white space
print(course.strip())
print(course.find("Pro"))
print(course.find("pro"))
print(course.replace("P", "-"))

print("Programming" in course)
print("Programming" not in course)
