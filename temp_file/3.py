n = int(input())
N, K, V = input().split()
N = int(N)
K = int(K)
V = int(V)

input_v = input().split()
out = map(int, input_v)

# for i in range(N+K):
i=0

val = 0
for k in out:
    val+=k

flag = False
temp = 0
while True:
    if len(input_v)!=N:
        break

    if temp <= (N+K)*(V):
    # if finalout <= V:
        i=i+1
        val  = val + K*(i)
        temp = val
        finalout = val / (N + K)
        if isinstance(finalout, int):
            if finalout==V:
                flag = True
                break
        val  = val - K*(i)
    else:
        break


if flag:
    print(i)
else:
    print(-1)


        

    