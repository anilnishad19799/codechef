# https://www.codechef.com/problems/LAPIN

test_case = int(input())

for i in range(test_case):
    n = input()
    if len(n)%2==0:
        mid = int(len(n) / 2)
        str1 = n[0:mid]
        str2 = n[mid:len(n)] 
    else:
        mid = int(len(n) / 2)
        str1 = n[0:mid]
        str2 = n[mid+1:len(n)] 

    for i in str1:
        if i in str2:
            str1 = str1.replace(i,'',1)
            str2 = str2.replace(i,'',1)
        
    print(str1,str2)
    if not (str1 and str2):
        print("YES")
    else:
        print("NO")
