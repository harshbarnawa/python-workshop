# Write a program to reverse a number (num = 56).

num = 56
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reverse =", rev)