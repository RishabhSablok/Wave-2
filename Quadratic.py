import math
a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))
no_of_roots = 0
discriminant = b ** 2 - (4 * a * c)
if discriminant > 0:
    no_of_roots = 2
elif discriminant == 0:
    no_of_roots = 1
elif discriminant < 0:
    no_of_roots = 0
print("There are", no_of_roots, "roots.")

if no_of_roots == 2:
    root1 = ((b * -1) + math.sqrt(discriminant)) / (2 * a)
    root2 = ((b * -1) - math.sqrt(discriminant)) / (2 * a)
    print("The roots are:")
    print(root1)
    print(root2)

elif no_of_roots == 1:
    root1 = ((b * -1) + math.sqrt(discriminant)) / (2 * a)
    print("The root is", root1)

else:
    print("There are no roots")
