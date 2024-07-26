# Conditionals and Booleans

# if statement
if True:
    print("Condition was True")
if False:  # Conditional after an if statement evaluates to true
    print("Condition was True")  # if statements are not only used as true / false

# Test of equality
language = "Python"  # single = is assigine values

if language == "Python":  # double = is testing for equality
    print("Python is the language learnt")

# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is ()

# Else Statements

language = "Python"

if language == "Python":
    print("Language is Python!")
else:
    print("No match!")

language = "Java"

if language == "Python":
    print("Language is Python!")
else:
    print("No match!")

# Checking for 2 or more values one by one
language = "Java"

if language == "Python":
    print("Language is Python!")
elif language == "Java":  # Python doesnt have a switch statemant(check multiple values)
    print("Language is Java")
else:
    print("No match!")

# Booleans Ops
user = "Admin"
logged_in = True
# and
if user == "Admin" and logged_in == True:  # Both value should match
    print("Admin in Logged in!")
else:
    print("Admin Not Online!")
# or (Any one str can be true )
user = "Admin"
logged_in = False
if user == "Admin" or logged_in == True:
    print("Admin in Logged in!")
else:
    print("Admin Not Online!")

# not ( Changes a true statement into a false or vise versa)

user = "Admin"
logged_in = False
if not logged_in:
    print("Please Log in!")
else:
    print("Welcome")


# Object Identity ( Tests if the two objects have the same identity [Same object in the memory])
a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))  # 'is' checks wheather these IDs or different
print(id(b))
print(a == b)
print(a is b)

# To make the Id in memory the same
a = [1, 2, 3]
a = b
print(id(a))
print(id(b))
print(a is b)
print(id(a) == id(b))

# What Python thinks as true/false

# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For example, '', (), [].
# Any empty Dictionay. For example, {}.

condition = False

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")
# There are some user defined that evaluate to false
# Other than these all are true like
condition = "True"

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")