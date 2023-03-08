for _ in range(int(input())):
    N = int(input())
    P = list(map(int, input().split()))

    print(max(P) + sum(P))