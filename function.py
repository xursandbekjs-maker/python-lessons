# Function - ma'lum bir vazifani bajaradigan kod blokidir. 
# Ularni qayta ishlatish mumkin va ular dastur tuzilishini yaxshilaydi.

def salom_ber():
    print("Assalomu alaykum!")

salom_ber() # Funksiyani chaqirish
salom_ber() # Funksiyani yana bir marta chaqirish

# FUNKSIYAGA QIYMAT UZATISH
# parametrlar.
# argumentlar.
def salom_ber (ism):
    print (f"Assalomu alaykum, {ism}!")

salom_ber("Ali") # Funksiyabi chaqirish 
salom_ber("Vali")
salom_ber("Akmal")


def yigindi(a, b):
    print(a + b)

yigindi(5, 10) # 15
yigindi(3, 7) # 10
# FUNKSIYAGA QIYMAT UZATISH (DEFAULT PARAMETR)
# Default parametr - bu funksiyaga qiymat uzatilmasa, avtomatik ravishda ishlatiladigan qiymat.
# Default parametrlar funksiyaning oxirida joylashishi kerak.

def yosh_hisobla(ism = "Akmal", tugilgan_yil = 1980):
    yosh = 2026 - tugilgan_yil
    print(f"{ism}ning yoshi: {yosh}") 

    yosh_hisobla("Ismoil", 2000) # Ismoilning yoshi: 26
    yosh_hisobla("Gulbor", 1995) # Gulborning yoshi: 31
    yosh_hisobla()
    yosh_hisobla("Jumagul", 1996) # Jumagulning yoshi: 30
    yosh_hisobla()

def yosh_hisobla(tugilgan_yil, joriy_yil = 2026):
    yosh = joriy_yil - tugilgan_yil