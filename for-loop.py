# Loop - sikl
# 1. for loop # 2. while loop
students = ['Charos','Kumush', 'Akmal', 'Ozodbek', 'Xudoyshukur'] 
for student in students:
    print(student)

    for student in students:
        print(f"Hurmatli")



nums = [12, -5, 15, 89, -75, 18]
s = 0
for son in nums:
    s += son
    ortacha = s / len(nums)
    print(ortacha)
import math
# o'rta geometrik qiymatini topish
k = 1
for son in nums:
    k *= (son)
    geo_ortacha = math.pow(k, 1/len(nums))
    print(geo_ortacha)