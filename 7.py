def checkArmstrong(num):
    original = num
    digits = len(str(num))
    total = 0

    while num > 0:
        digit = num % 10
        total += digit ** digits
        num //= 10

    return total == original

n = int(input("Enter a number: "))

if checkArmstrong(n):
    print(n, "is an Armstrong Number")
else:
    print(n, "is not an Armstrong Number")