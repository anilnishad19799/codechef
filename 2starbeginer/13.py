
# test_cases = int(input())
# for _ in range(test_cases):
#     N,K,L = input().split()
#     N,K,L = int(N), int(K), int(L)
    
#     A = list(map(int, input().split()))
    
    
#     if N == 1:
#         print("Yes")
#     else:
#         friend = A[-1]
#         del A[-1]
#         mx = max(A)

#         if friend > mx:
#             print("Yes")
#         elif (K<0 and mx>=friend):
#             print("No")
#         else:
#             friend += (L-1) * K
#             if friend > mx:
#                 print("Yes")
#             else:
#                 print("No")