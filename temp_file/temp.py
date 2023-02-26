vowel = ['a', 'e', 'i', 'o', 'u']
n = int(input())
if n <= 100 and n>=1:
    for i in range(n):
        b = int(input())
        if b>1 and b<=100:
            a = input().lower()
            easy_flag = True
            count = 0
            for i in a:
                print("i",i)
                if i.lower() not in vowel:
                    count+=1
                else:
                    count=0

                if count==4:
                    easy_flag = False
                    break
            if easy_flag:
                print("YES")
            else:
                print("NO")