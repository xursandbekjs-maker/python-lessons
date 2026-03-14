import math
r1 = int(input("Birinchi doiraning radiusini kiriting ; "))
r2 = int(input("Ikkinchi doiraning radiusini kiriting ; "))
r3 = int(input("Uchinchi doiraning radiusini kiriting ; "))
# s = pi * r ** 2
s1 = math.pi*r1**2
s2 = math.pi*r2**2
s3 = math.pi*r3**2
print(f"radiusi {r1} bolgan doiraning yuzasi {s1}")
print(f"radiusi {r2} bolgan doiraning yuzasi {s2}")
print(f"radiusi {r3} bolgan doiraning yuzasi {s3}")