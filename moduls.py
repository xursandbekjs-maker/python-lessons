# random module
import random as r
print(r.random())# 0 va 1 oraliqdagi qiymat qaytaradi
print(r.randint(100, 100000))# 100 va 100000 oraliqdagi butun son qaytaradi

ismlar = ['Ali', 'Vali', 'Hasan', 'Husan']
ism = r.choice(ismlar) # ismlar ro'yxatidan random ism tanlaydi
print(ism)
print(r.choice(ism))# ismdan tasodifiy harf tanlaydi

x = list(range(11))
print(x)
r.shuffle(x) # x ro'yxatini aralashtiradi
print(x)