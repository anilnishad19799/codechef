for _ in range(int(input())):
    n = int(input())
    X = list(map(int, input().split()))
    
    # X.sort()
    
    # min_x = 1
    # max_x = 1
    # min_xflag = True
    # for i in range(len(X)-1):
    #     if (X[i+1] - X[i]) <= 2:
            
    #         if min_xflag:
    #             min_x+=1
            
    #         max_x+=1
    #     else:
    #         min_xflag = False
    #         max_x=1
    
        
    list1 = []
    count = 1
    for i in range(len(X)-1):
        if (X[i+1] - X[i]) <= 2:
            count+=1
        else:
            list1.append(count)
            count=1
    
    list1.append(count)
    
    print(min_x,max_x)
    print(min(list1),max(list1))