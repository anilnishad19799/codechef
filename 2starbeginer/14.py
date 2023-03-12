# cook your dish here
import re
for _  in range(int(input())):
    S = input()
    
    if len(S)>=10:
        small_char = re.search('[a-z]' , S)        
        big_char = re.search('[A-Z]' , S[1:-1])
        num = re.search( '[0-9]', S[1:-1])
        punc = re.search("['@', '#', '%', '&', '?']", S[1:-1])
        
        if small_char and big_char and num and punc:
            print("YES")
        else:
            print("No")
    else:
        print("NO")