size = int(input("Enter the size of the pattern: "))

i = 0
while i < size:
    for j in range(0, size):
        print("*", end="")
        j +=1
    i += 1
    print()