n = int(input())
# print(amt_withdraw)
# print(type(amt_withdraw[0]))

binary_v = []
for i in range(n):

    num_p, Amount = input().split()
    num_p = int(num_p)
    Amount = int(Amount)
    amt_withdraw = input().split()
    amt_withdraw = map(int, amt_withdraw)

    str1 = ''
    for i in amt_withdraw:
        if i <= Amount:
            Amount-=i
            str1 + '1' 
            binary_v.append(1)
        else:
            binary_v.append(0)
            str1 + '0'

    print(str1)
    print(binary_v)


