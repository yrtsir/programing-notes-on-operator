# membership and identity operators

a = [1, 2, 3, 4, 5]
b=[1, 2, 3, 4, 5]
c=a
print(a is b)  # False, because a and b are different objects
print(a is c)  # True, because c references the same object as a
print(a == b)  # True, because a and b have the same content
print(id(a))  # Prints the memory address of a
print(id(b))  # Prints the memory address of b
print(id(c))  # Prints the memory address of c, which is the same as a