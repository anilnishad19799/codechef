## elvstr

test_cases = int(input())

for _ in range(test_cases):
    N, sv, ev = input().split()
    N = int(N)
    sv = int(sv) 
    ev =int(ev)

    sd = N * 1.41421356237
    ed = N * 2

    st = sd / sv
    et = ed / ev

    if st < et:
        print("Stairs")
    else:
        print("Elevator")



