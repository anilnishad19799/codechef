# https://www.codechef.com/problems/WORDLE

test_case = int(input())

if test_case<=1000 and test_case>=1:
    for i in range(test_case):
        M = input()
        T = input()

        if len(M)==len(T):
            str1 = ''
            for i in range(len(M)):
                if M[i]!=T[i]:
                    str1+='B'
                else:
                    str1+='G'
        print(str1)
