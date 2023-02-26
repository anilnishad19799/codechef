# https://www.codechef.com/problems/TSTROBOT

test_cases = int(input())

if test_cases>=1 and test_cases<=100:
    for i in range(test_cases):
        N, X = input().split()
        N,X = int(N), int(X)
        
        string_inp = input()
        list1 = []
        
        if len(string_inp)==N:
            for i in string_inp:

                if X not in list1:
                    list1.append(X)
                if i == 'R':
                    X = X+1
                else:
                    X = X - 1 

                if X not in list1:
                    list1.append(X)



        
        print(len(list1))
                    