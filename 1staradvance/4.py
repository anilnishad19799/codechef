# https://www.codechef.com/problems/MAX_DIFF

for _ in range(int(input())):
    NS = list(map(int, input().split()))
    N = NS[0]
    S = NS[1]
    
    if N>S:
        print(S)
    elif (N==S):
        print(N)
    else:
        print(N - (S-N))