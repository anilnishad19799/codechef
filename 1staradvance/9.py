test_cases = int(input())
for _ in range(test_cases):
    n = list(map(int, input().split()))
    
    n.sort()
    
    if  n[1]!=n[2] or (n[1]==n[2] and n[2] != n[3] and n[0] != n[1]):
        print("2")
    elif n[0]==n[3]:
        print("0")
    else:
        print("1")