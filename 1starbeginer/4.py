# https://www.codechef.com/problems/PRACTICEPERF

problem_s = input().split()

p1,p2,p3,p4 = int(problem_s[0]), int(problem_s[1]), int(problem_s[2]), int(problem_s[3])
list1 = [p1,p2,p3,p4]

if (p1 and p2 and p3 and p4) >=1 and (p1 and p2 and p3 and p4) <= 100:
    count = 0
    
    for i in list1:
        if i>=10:
            count+=1
            
    print(count)