from math import ceil
x = "012"
l = x.isnumeric()
print(l)

print("____")
# print()
# print("")
print("\n")
print("____")


print(ceil(4/3))

horizontals = [1, 2, 3]
peaked = [5, 6]

value = 4

if (value in peaked or horizontals):
    print("yes!")
else: print("no!!!!")



# Python program to explain os.get_terminal_size() method
	
# importing os module
import os

# Get the size
# of the terminal
size = os.get_terminal_size().columns


# Print the size
# of the terminal
print(size)

x = 0
import functools

@functools.lru_cache(maxsize=1)
def once(x):
    x += 1
    print(x)
    print("you are doing good, keep it up.")

once(x)
once(x)


name = "mahdi"

print("*"*len(name))
