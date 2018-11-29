m = int(raw_input())
x = 0
temp = m
while temp > 0:
    digit = temp % 10
    x += digit ** 3 
    temp //= 10
if m == x:
    print("yes")
else:
    print("no")
