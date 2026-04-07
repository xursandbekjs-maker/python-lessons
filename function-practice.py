# Amaliyot
# 1.
def tugilgan_yilni_hisobla(ism, yosh):
    """Foydalanuvchining ismi va yoshini qabul qilib,
      uning tug'ilgan yilini hisoblaydigan funksiya"""
    yil = 2026 - yosh
    print(f"{ism}, siz {yil}-yilda tug'ilgan")

name = input("Ismingizni kiriting: ")
age = int(input("Yoshingizni kiriting: "))
tugilgan_yilni_hisobla(name, age)

# 2.
def kvadrat_kub_hisobla(son):
    """Foydalanuvchidan son qabul qilib, uning kvadrati va kubini hisoblaydigan funksiya"""
    kvadrat = son ** 2
    kub = son ** 3
    print(f"{son} ning kvadrati {kvadrat} ga teng, kubi esa {kub} ga teng.")

son = int(input("Son kiriting: "))
kvadrat_kub_hisobla(son)
# 3.
def toq_juft_hisobla(son):
    """Foydalanuvchidan son qabul qilib, uning toq yoki juft ekanligini aniqlaydigan funksiya"""
    if son % 2 == 0:
        print(f"{son} juft son.")
    else:
        print(f"{son} toq son.")

son = int(input("Son kiriting: "))
toq_juft_hisobla(son)
# 4.
def katta_kichik_hisobla(a, b):
    """Foydalanuvchidan ikkita son qabul qilib, qaysi biri katta yoki kichik ekanligini aniqlaydigan funksiya"""
    if a > b:
        print(f"{a} {b} dan katta.")
    elif a < b:
        print(f"{a} {b} dan kichik.")
    else:
        print("Ikkala son teng.")
# 5.
def daraja_hisobla(x, y):
    """Foydalanuvchidan ikkita son qabul qilib, birinchi sonni ikkinchi son darajasiga ko'taradigan funksiya"""
 