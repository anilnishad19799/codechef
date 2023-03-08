for _ in range(int(input())):
    N,M,K = list(map(int, input().split()))

    # Enter value for N
    M = list(map(int,input().split()))
    K = list(map(int,input().split()))

    un_tra_ign = []
    v = list(set(M+K))
    for i in range(1, N+1):
        if i not in v:
            un_tra_ign.append(i)

    track_ign = list(set(M) & set(K))

    print(len(track_ign), len(un_tra_ign))


