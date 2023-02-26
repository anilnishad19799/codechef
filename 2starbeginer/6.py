# https://www.codechef.com/problems/FODCHAIN

test_cases = int(input())

for _ in range(test_cases):
    E,K  = input().split()
    E = int(E)
    K = int(K)

    x = E
    count = 0
    while True:
        
        x = x / K
        count+=1
        
        if int(x)==0:
            break
            

    print(count)