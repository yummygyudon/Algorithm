import sys
T = int(sys.stdin.readline())
for _ in range(T) :
    n = int(sys.stdin.readline())
    real = set(sorted(list(map(int, sys.stdin.readline().split()))))
    # 굳이 sorted(list(... 안해도될듯
    # real = set(map(int, sys.stdin.readline().split())) 로 하니까  500ms 가까이 줄어듦.
    print(real)
    m = int(sys.stdin.readline())
    hear = list(map(int, sys.stdin.readline().split()))
    same = real & set(hear.copy()) # 본래 위치를 유지한 hear리스트는 1,0 출력할 때 필요
    # copy해서 중복값만 찾기
    print(same)

    for num in hear :
        if num in same :
            print(1)
        else:
            print(0)

