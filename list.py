# Ro'yxat elementlari ustida amallar
numbers = [12, -15, 88.99, 10, 15.93, -8.75]
# 1. Ro'yxat elementini o'zgartirish
numbers[1] = 20
print(numbers)

# Ro'yxatga yangi element qo'shish
# 1.  list.append(new_element) method
numbers.append(17)
numbers.append(-102.89)
print(numbers)

# 2. list.insert(index, element) method
numbers.insert(2, 13)
print(numbers)
numbers.insert(0, 0)
print(numbers)

# CRUD - create / read / update / delete
# Ro'yxat elementini o'chirish
# 1. list.remove(element)
numbers.remove(0)
print(numbers)
numbers.remove(numbers[3])
print(numbers)

# 2. del operator
del numbers[5]
print(numbers)

# Ro'yxatdagi elemenetni sug'urib olish
# list.pop(index?) method
number = numbers.pop(2)
print(number)

# Amaliyot
ismlar = ['akmal', 'hayitboy', 'xudoshukur' ]
print("salom" "{ismlar[0]}" "akmal botmi?")

