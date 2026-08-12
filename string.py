#text = "Python Programming"
#consider the given string and perform the following operations on the string
#1. display Python.
#2. Display programming
#3. Find if text java is there in the string or not. If not then include Java in between python and Programming.
#4. Find the length of the new string.
# 5. Count the no of words in the string.
# 6. Capitalize each word in the string.
# 7. Remove all the spaces and print the string.
# 8. Print the frequency of 'A', 'P', 'R', 'M' (in capital letters).

# text = "Python Programming"

text = "Python Programming"

# Display Python
print(text[:6])

# Display Programming
print(text[7:])

# Find if Java is present. If not, include Java between Python and Programming
if "Java" not in text:
    text = text[:6] + " Java " + text[7:]

print(text)

# Find the length of the new string
print(len(text))

# Count the number of words in the string
print(len(text.split()))

# Capitalize each word in the string
print(text.title())

# Remove all the spaces and print the string
print(text.replace(" ", ""))

# Convert the string to uppercase and find the frequency of A, P, R and M
text_upper = text.upper()

print("A =", text_upper.count("A"))
print("P =", text_upper.count("P"))
print("R =", text_upper.count("R"))
print("M =", text_upper.count("M"))