## problem:-  https://www.codechef.com/problems/TIMELY
test_case = int(input())

list1 = []
for i in range(test_case):
    n  = int(input())
    list1.append(n)

for i in list1:
    if i<30:
        print("NO")
    else:
        print("YES")