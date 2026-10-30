# Program to print even number series 2 4 6 8 ... n

n = int(input("Enter a number: "))

for i in range(2, n + 1, 2):
    print(i, end=" ")