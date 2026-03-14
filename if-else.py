# #Tarmoqlash operatorlari . if - agar , else - boshqa
# age = int(input("Yoshingizni kiriting: "))
# if age < 18:
#     print("Siz hali yoshsiz, kirishga ruxsat yo'q")
# else:
#     print("Sizga kirishga ruxsat bor")

# ball = int(input("Imtihondan olgan ballingizni kiriting: "))
# if ball < 56:
#     print("Siz imtihondan o'ta olmadingiz")
# elif ball >= 56 and ball < 70:
#     print("3 baho oldingiz")
# elif ball >= 70 and ball < 80:
#     print("4 baho oldingiz")
# elif ball >= 86 and ball < 100:
#     print("5 baho oldingiz")
# else:
#     print("Siz 0 dan 100 gacha ball kiriting")
# else:
#     print("Siz imtihondan o'ta oldingiz")

# age = int(input("Yoshingizni kiriting"))
# if age < 16:
#     print("Siz hali yoshsiz")
# else:
#     print("Tabriklaymiz siz pasport oldingiz")

# #2 - mashq
# son = int(input("Xohlagan sonni kiriting: "))
# if son % 2 == 0:
#     print("Juft son")
# else:
#     print("Toq son")

# # 3-mashq
# son = int(input("Xohlagan sonni kiriting: "))
# if son % 5 == 0:
#     print("Son 5 ga bo'linadi")
# else:
#     print("Son 5 ga bo'linmaydi")

# # 4-mashq
# son = int(input("Xohlagan sonni kriting: "))
# if son % 2 == 0 and son % 3 == 2:
#     print("Son 6 ga bo'linadi ")
# else:
#     print("Son 6 ga bo'linmaydi")

# # 5-mashq
# a = int(input("Birinchi sonni kiriting"))
# b = int(input("Ikkinchi sonni kiriting"))
# c = int(input("Uchinchi sonni kiriting"))
# if a + b > c and b + c and a + c > b:
#     print("Uchburchak yasab bo'ladi")
# else:
#     print("Uchburchak yasab bo'lmaydi")

# # 6-mashq
# a = int(input("Birinchi sonni kiriting"))
# b = int(input("Ikkinchi sonni kiriting"))
# if a <= b:
#     print(a,b)
# else:
#     print(a,b)

# import math
# a = int(input("1-sonni kiriting"))
# b = int(input("2-sonni kiriting"))
# c = int(input("3-sonni kiriting"))
# D = b ** 2 - 4 * a * c
# if D > 0:
#    x1 = (- b + math.sqrt(D)) / (2 * a)
#    x2 = (- b - math.sqrt(D)) / (2 * a)
#    print("%.2f" % x1, "%.2f" % x2)
# elif D == 0:
#    x = - b / (2 * a)
#    print(x)
# else:
#    print("NO")

# x = int(input("1-sonni kiriting"))
# y = int(input("2-sonni kiriting"))
# z = int(input("3-sonni kiriting"))
# if x> 0:
#     x = x ** 2
# if y > 0:
#     y = y ** 2
# if z > 0:
#     z = z ** 2

#     print(x, y, z)

# x = float(input("1-sonni kiriting"))
# y = float(input("2-sonni kiriting"))
# z = float(input("3-sonni kiriting"))
# if 1 <= x <= 3:
#     print(x)
# if 1 <= y <= 3:
#     print(y)
# if 1 <= z <= 3:
#     print(z)

a = float(input("1-sonni kiriting"))
b = float(input("2-sonni kiriting"))
c = float(input("3-sonni kiriting"))
d = float(input("4-sonni kiriting"))

max_value = max(a, b, c, d)
min_value = min (a, b, c, d)
if a <= b <= c <= d:
      a = b = c = d = max_value
else:
      a = b = c = d = min_value

print(a, b, c, d)

