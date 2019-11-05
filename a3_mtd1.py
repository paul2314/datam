import random

print("A3 algo")
m = random.getrandbits(128)
print("RAND number provided is: ", m)
c,d = input("Enter key Ki present in SIM: ").split()

# Any operation can be chosen below. Addition/Subtraction/Combination of them
n = int(c)**int(d)
ans = m + n

y = 3 ** 100
z = m + y

if (z==ans):
    print("Generated SRES has matched. User is authenticated.")
else:
    print("Generated SRES does not match. Please retry.")