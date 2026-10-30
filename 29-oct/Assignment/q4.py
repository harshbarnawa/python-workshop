# Program to print odd number series 1 3 5 7 ... n

n = int(input("Enter a number: "))

for i in range(1, n + 1, 2):
    print(i, end=" ")