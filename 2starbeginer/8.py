test_cases = int(input())

for _ in range(test_cases):

    N, W = input().split()
    N,W = int(N), int(W)

    list1 = []
    list1.extend(input().split())

    list2 = sorted([int(x) for x in list1], reverse=True)

    sum = 0
    for count,j in enumerate(list2):
        sum += int(j)
        if sum > W:
            break
    
    holiday = len(list2) - count - 1

    print(holiday)


