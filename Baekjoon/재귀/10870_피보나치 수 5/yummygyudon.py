def Fibonacci(n) :
    if n <= 1 : # n단계만큼 내려간다음 상향식 분석
        # (Fibonacci((n-1)-1)&Fibonacci((n-1)) 이 0(0번째) & 1(1번째) 가 될때
        return n
    n -= 1 # if조건문에 해당할 때까지 단계가 내려가게끔
    return Fibonacci(n) + Fibonacci(n-1) # (n-1번째 + n-2번째) 가 n번째 피보나치 수
# F(5) = F(4) + F(3)
#      =(F(3) + F(2))  +  (F(2) + F(1))
#      =((F(2) + F(1)) + (F(1) + F(0)))  +  ((F(1) + F(0)) + F(1))
#      =(((F(1) + F(0)) + F(1)) + (F(1) + F(0)))  +  ((F(1) + F(0)) + F(1))
#      = (((1 + 0)) + 1) + (1 + 0))  +  ((1 + 0) + 1)
#      = ((1 + 1) + 1)  +  (1 + 1)
#      = (2 + 1)  +  (2)
#      = (3) + (2)
#      = 5
num = int(input())
print(Fibonacci(num))

# 시간 = 76ms / 메모리 = 30864KB