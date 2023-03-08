#   

test_cases = int(input())

for _ in range(test_cases):
    string = input()
    count=0
    i = 0
    while True:
        if i >= len(string) - 1:
            break
        if string[i] == 'x' and string[i+1]=='y':
            i+=2
            count+=1
        elif string[i] == 'y' and string[i+1]=='x':
            i+=2
            count+=1
        else:
            i+=1
            pass

        
    print(count)
