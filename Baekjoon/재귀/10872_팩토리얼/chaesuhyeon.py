def fac(N):
    if N == 0:
        return 1
    return N * fac(N-1)

N = int(input())
print(fac(N))