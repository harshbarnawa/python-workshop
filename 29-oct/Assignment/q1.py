# Program to print sum of the series 1/1 + 1/2 + ... + 1/n

n = int(input("Enter a number: "))
sum = 0

for i in range(1, n + 1):
    sum = sum + (1 / i)

print("Sum of series =", sum)