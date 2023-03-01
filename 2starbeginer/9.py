# https://www.codechef.com/problems/SNAKPROC

test_cases = int(input())

for i in range(test_cases):
    n = int(input())
    string = input().replace('.','')

    flag = False
    
    if string.startswith('T') or string.endswith("H"):
        flag = True
    else:
        for i in range(len(string)):
            if i % 2 == 0:
                if string[i]=='H':
                    pass
                else:
                    flag = True
                    break
            else:
                if string[i]=='T':
                    pass
                else:
                    flag = True
                    break
    if not flag:
        print("valid")
    else:
        print("Invalid")





    
        


