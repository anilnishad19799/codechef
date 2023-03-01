import itertools
K,M = input().split()
K ,M = int(K), int(M)

list1 = []
for _ in range(K):
    list1.append(list(input().split())[1:])


print(list1)
list2 = list(itertools.product(*list1))
max_val = 0

for i in list2:
    sum = 0
    for j in i:
        sum+=(int(j)** 2)
    
    final_sum = sum % M
    if final_sum > max_val:
        max_val = final_sum
print(int(max_val))

# print(list1)