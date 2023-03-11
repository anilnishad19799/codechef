# The Smallest Pair
for _ in range(int(input())):
    n = int(input())
    n_list1 = list(map(int, input().split()))
    
    # sum = 10000000
    # for i in range(len(n_list1)):
    #     for j in range(i+1, n):
    #         print(n_list1[i], n_list1[j])
    #         if n_list1[i]+n_list1[j]<sum:
    #             sum = n_list1[i] + n_list1[j]
    
    n_list1.sort()
    print(n_list1[0], n_list1[1])

    print(sum)