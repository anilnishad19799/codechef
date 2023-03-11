# https://www.codechef.com/problems/MAKEDIV3

for _ in range(int(input())):
    n = int(input())
    
    X = '1'
    zeros = '0'*(n-1)
    val = X+zeros

    final_val = int(val)
    while final_val%3!=0:
        final_val+=1
        
    while True:
        if (final_val%3==0 and final_val%9!=0 and final_val%2==1):
            break
        final_val+=3
    print(final_val)
