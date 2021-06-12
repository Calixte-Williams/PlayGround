# Conditionals and Loops
#IF
n = 20
if n == 20:
    print("The number is 20")

# elif = else if // there so no limit to how many you can have in an if statement
n3 = 3
if n3 == 17:
    print('Number is 17')
elif n3 < 10:
    print('Number is less than 10')
elif n3 > 10:
    print('Number is greater than 10')
else:
    print('Number is invalid')
# ELSE can be used at the end as a fallback if the IF / ELIF statements were not true.

# For Loops
dataset = (1, 2, 3, 4, 5)
for variable in dataset:     # 'variable' here is a simply a placeholder variable to hold each sequence of data
    print(variable)
for x in range(3):    # range() used to iterate a specific number of times to run the loop, it starts from zero (0) & increments of one by default
    print(x)
for x in range(1,3):    # range(x, x) is used to indicate the number to start from
    print(x)
for x in range(1,11,3):     # A third attribute can be added to specify the increments to count by.
    print(x)