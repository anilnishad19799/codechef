# https://www.codechef.com/problems/STRP?tab=statement

test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    string = input()

    i = 0
    while i <= len(string) - 1:    
        if string[i]==string[i+1]:
            i+=2
            n-=1
        else:
            i+=1

    print(n)