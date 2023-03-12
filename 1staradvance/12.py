for _ in range(int(input())):
    N,M = input().split()
    N,M = int(N), int(M)

    A = list(map(int, input().split()))

    if set(A) == M :
        print("NO")
    else:
        print("YES")
