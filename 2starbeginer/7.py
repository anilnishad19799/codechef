# https://www.codechef.com/problems/PETSTORE

test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    # for _ in range(n):
    list1 = []
    list2 = []
    list1.extend(input().split())
    list2 = [int(x) for x in list1]
    list2 = sorted(list2)

    set1 = set(list2)

    s = len(set1)

    print(s)

    if s>1:
        if len(list2)%2!=0:
            print("No")
        else:
            flag = False
            print(list2)
            for i in range(0, len(list2), 2):
                if list2[i]==list2[i+1]:
                    flag = True
                else:
                    
                    flag = False
                    break

            if flag:
                print("YES")
            else:
                print("NO")
    else:
        print("NO")

                        


