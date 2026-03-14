import math
x = float("Birinchi sonni kiriting")
y = float("Ikkinchi sonni yozing")
a = x + y
b = math.pow(y, 2)
c = b + 2
d = x + math.pow(x, 3) / 5
e = math.exp(y+2)
c1 = a / (b + math.fabs(c / d)) + e
print(c1)

