# https://www.codechef.com/problems/REDALERT

for _ in range(int(input())):
    N,D,H = input().split()
    N, D, H = int(N), int(D), int(H)
    A = list(map(int, input().split()))
    
    sum = 0
    sumflag = False
    for i in A:
        
        if i == 0:
            sum -= D
            if sum < 0:
                sum = 0
        if i>0:
            sum+=i
            
        if sum > H:
            sumflag = True
            
    if sumflag:
        print("YES")
    else:
        print("NO")