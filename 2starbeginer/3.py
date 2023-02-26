# https://www.codechef.com/problems/MISSP

# test_cases = int(input())

# list1 = []
# for i in range(test_cases):
#     N = int(input())
#     for i in range(N):
#         list1.append(int(input()))

#     dict1 = {}
#     for i in list1:
#         if i in dict1:
#             dict1[i] = False
#         else:
#             dict1[i] = True

#     print(dict1)
#     for i,j in dict1.items():
#         if j:
#             print(i)

test_cases = int(input())

for i in range(test_cases):
    list1 = []
    N = int(input())
    for i in range(N):
        X = int(input())
        list1.append(X)

    list1 = sorted(list1)

    print(list1)
    for i in range(0, len(list1), 2):
        if list1[i] == list1[-1]:
            print(list1[i])
        elif list1[i]!=list1[i+1]:
            print(list1[i])
            break
        else:
            pass


##
test_cases = int(input())

for i in range(test_cases):
    list1 = []
    N = int(input())
    for i in range(N):
        X = int(input())
        
        if X not in list1:
            list1 = list1 + [X]
        else:
            list1.remove(X)
        
    print(list1[0])    
        
