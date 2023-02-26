# https://www.codechef.com/problems/AIRLINE

test_cases = int(input())

for _ in range(test_cases):
    l = input().split()
    l = [int(i) for i in l]

    flag = False
    for i in range(3):
        for j in range(i+1,3):
            k = [i for i in range(3)]
            k.remove(i)
            k.remove(j)
            if l[i] + l[j] <= l[3] and l[k[0]] <= l[4]:
                flag = True
                break
        
    if flag:
        print("YES")
    else:
        print("NO")