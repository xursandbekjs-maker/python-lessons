# Ro'yxatdan nusxa olish 
sonlar = list(range(1, 6)) # [1, 2, 3, 4, 5, 6]
sonlar2 = sonlar 
# print(sonlar)
# print(sonlar2)
# shallow(sayoz) copy

sonlar2.append(6)
sonlar2.append(7)
print(sonlar2) # [1, 2, 3, 4, 5, 6, 7,]
print(sonlar) # [1, 2, 3, 4, 5, 6, 7, ]
# deep (chuqur) copy

sonlar3 = sonlar[:]
print(sonlar3)
sonlar3.append(6)
print(sonlar3) # [1, 2, 3, 4, 5, 6]
print(sonlar) # [1, 2, 3, 4, 5] 

# Tuple - o'zgarmas ro'yxat

toys = ('bus','car','bear','dino','snake','lizard')
print(toys[0])
print(toys[-1])
print(toys[2 : 5])

davlatlar = ('Uzbekiston', 'USA', 'Rossiya', )