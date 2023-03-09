# https://www.codechef.com/problems/LADDU
for _ in range(int(input())):
    sum = 0
    rank = 10000
    bug_val = 100000
    Act, origin = input().split()   
    Act = int(Act)
    
    for i in range(Act):
        activity = input()
        
        if 'CONTEST_WON' in activity:
            rank =int(activity.split()[1]) 
            if rank<=20:
                sum= sum + (300+(20-rank))
            else:
                sum+=300
                
        elif 'TOP_CONTRIBUTOR' in activity:
            sum+=300
            
        elif 'BUG_FOUND ' in activity:
            bug_val = int(activity.split()[1])
            sum+=bug_val
            
        elif 'CONTEST_HOSTED' in activity:
            sum+=50
        
    if origin == 'INDIAN':
        output = sum // 200
    else:
        output = sum // 400
    
    print(output)
    
            
        
    