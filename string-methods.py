# String methods
ism = "James"
familiya = "Lebron"
ism_sharif = f"{ism} {familiya}"
# upper() va lower()
print(ism_sharif.upper())
print("Adminjon".upper())
print(ism_sharif.lower())
print("Adminjon".lower())
print(ism_sharif) # Jame Lebron
ism_sharif = ism_sharif.upper()
print(ism_sharif) # JAMES LEBRON
# title() va capitalize()
print('donald trump'.title())
print(ism_sharif.title())
print('vladimir putin'.capitalize())
print(ism_sharif.capitalize())

meva = "     olma     "
print("Men " + meva.lstrip() + " yaxshi ko'raman")
print("Men " + meva.rstrip() + " yaxshi ko'raman")
print("Men " + meva.strip() + " yaxshi ko'raman")
print("Men " + meva + " yaxshi ko'raman")
print(meva)
meva = meva.strip()
print(meva)

# input()
username1 = 'norboyeva001'
print("Kumushxonni github username: " + username1)
username2 = input("Iltimos, github username kiriting: ")
print(f"Sizning github usernameingiz: {username2}")

firstname = input("Ismingizni kiriting: ")
lastname = input("Familiyangizni kiriting: ")
print(f"Sizning ism familiyangiz: {firstname} {lastname}")

kocha = input("Iltimos kochangizni kiriting: ")
mahalla = input("Iltimos, mahallangizni kiriting: ")
tuman = input("Iltimos, tumaningizni kiriting: ")
viloyat = input("Iltimos, viloyatingizni kiriting: ")
manzil = f"{kocha.title()} ko'chasi, \n{mahalla.upper()} mahallasi, \n{tuman.lower()} tumani, \n{viloyat.capitalize()} viloyati"
print(manzil)
