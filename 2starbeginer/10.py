# https://www.codechef.com/problems/REMOVEBAD?tab=statement
import statistics
for _ in range(int(input())):
    N = int(input())

    list1 = list(map(int, input().split()))

    max_element = statistics.mode(list1)

    # max_element = max(list1, key = list1.count)
    final_out = len(list(filter(lambda x : max_element != x, list1)))
    print(final_out)