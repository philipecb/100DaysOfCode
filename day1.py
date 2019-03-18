# Part I: Basics
# Chapter 2: Variables and Simple Data Types
# Strings

# Changing Case in a String with Methods

name = "philipe c b"
print(name.title())

name = "Philipe C B"
print(name.upper())
print(name.lower())

# Combining or Concatenating Strings

first_name = "philipe"
last_name = "c b"
full_name = first_name + " " + last_name
print(full_name)

print("Hello, " + full_name.title() + "!")

message = "Hello, " + full_name.title() + "!"
print(message)

# Adding Whitespace to Strings with Tabs or Newlines

print("Python")
print("\tPython")

print("Languages:\nPython\nC\nJavaScript")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Stripping Whitespace

favorite_language = 'Python '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language)

favorite_language = 'Python '
favorite_language = favorite_language.rstrip()
print(favorite_language)

favorite_language = ' Python '
print(favorite_language.rstrip())   # right side
print(favorite_language.lstrip())   # left side
print(favorite_language.strip())    # both sides
