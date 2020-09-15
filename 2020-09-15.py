"""# 1. N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.
# 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.

a = int(input())
for i in range(1,10):
    print(str(a)+" * " + str(i) +" = " + str(a*i))

# 2. 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

T = int(input())
for i in range(1,T+1):
    a,b = input().split()
    print(int(a)+int(b))

# 3. n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
# 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

a = int(input())
sum=0
for i in range (1,a+1):
    sum+=i
print(sum)

# 4. 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
# 첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.

N = int(input())
for i in range (1,N+1):
    print(i)

# 5.자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
# 첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.

N = int(input())
for i in range (1,N+1):
    print(N+1-i)

# 6. 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

T = int(input())
for i in range(1,T+1):
    a,b=input().split()
    print("Case #"+str(i)+": " + str(int(a)+int(b)))

7. 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.

T = int(input())
for i in range(1,T+1):
    a,b=input().split()
    print("Case #"+str(i)+": " +str(a)+ " + " + str(b)+ " = " +str(int(a)+int(b)))
"""
