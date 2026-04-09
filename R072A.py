N = input() # 1339 => "1339"
print(type(N))
even_sum = 0
odd_sum = 0
for index in range(len(N)):
    digit = int(N[index])
    if (index + 1) % 2 == 1:
        odd_sum += digit
    else:
        even_sum += digit
        
diff = odd_sum - even_sum
if diff == 0 or diff % 11 == 0:
    print("YES")
else:    
    print("NO")