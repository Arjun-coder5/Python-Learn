name =  "Arjun" #- > Strings are immutable
#name[0] = "Karan"#You cannot do this
a = len(name)
print(a)

# method :
#1.uppercase :
print(name.upper())
#1.lowercase :
print(name.lower())
#1.capitalize :
print(name.capitalize())


#Find:
text = "Python there"
print(text.find("there"))
#Replace:
print(text.replace("Python","Java"))

text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)  # Output: ['apple', 'banana', 'orange']

new_text = " - ".join(fruits)
print(new_text)  # Output: "apple - banana - orange"


text = "Python123"
print(text.isalpha())  # Output: False
print(text.isdigit())  # Output: False
print(text.isalnum())  # Output: True
print(text.isspace())  # Output: False

print(ord('A'))  # Output: 65
print(chr(65))   # Output: 'A'