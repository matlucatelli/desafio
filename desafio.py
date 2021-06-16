def maior(num):
    maior = 0
    if num[0] > num[1] and num[0] > num[2]:
        maior = num[0]
        
    if num[1] > num[2] and num[1] > num[0]:
        maior = num[1]
        
    if num[2] > num[0] and num[2] > num[1]:
        maior = num[2]
    return maior

def maior2(num):
    maior = num[0]
    if maior < num [1]:
        maior = num[1]
        
    if maior < num[2]:
        maior = num[2]
    return maior
    
num = [0,0,0]  
for x in range (0, 3):
    num[x] = int(input("Digite três números: "))


print(maior(num))
print(maior2(num))