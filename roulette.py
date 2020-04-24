import random
start = []
for i in range(38):
    if i < 36:
        start.append(str(i))
    elif i == 37:
        start.append("0")
    elif i == 38:
        start.append("00")
my_random = random.randint(1, 38)
if my_random == 37:
    my_random = "0"
    print("The spin resulted in", my_random)
    print("Pay", my_random)
elif my_random == 38:
    my_random = "00"
    print("The spin resulted in", my_random)
    print("Pay", my_random)
else:
    print("The spin resulted in", my_random)
    print("Pay", my_random)
    if my_random % 2 == 0:
        print("Pay Red")
        print("Pay Even")
    else:
        print("Pay Black")
        print("Pay Odd")
    if my_random <= 18:
        print("Pay 1 to 18")
    else:
        print("Pay 19 to 36")