for _ in range(int(input())):
    X, Y = input().split()
    string = input()
    X = int(X)
    Y = int(Y)
    
    count = 0
    max_cooccurence = 0
    prev = 0
    for  i in range(len(string)):
        if string[i] == '1':
            count+=1
            max_cooccurence += 1
        else:
            max_cooccurence = 0

        if max_cooccurence > prev:
            prev = max_cooccurence

    sum = (count * X) + (prev * Y)
    print(sum)