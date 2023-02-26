# https://www.codechef.com/problems/TYRES

test_cases = int(input())

if test_cases<=1000 and test_cases>=1:
    for i in range(test_cases):
        car_flag = False
        n = int(input())
        if n%2==0:
            if n%4==0:
                car_flag=True

            if car_flag:
                print("NO")
            else:
                print('YES')