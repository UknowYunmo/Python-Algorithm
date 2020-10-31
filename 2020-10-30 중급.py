"""
옛날 옛적에 수학이 항상 큰 골칫거리였던 나라가 있었다.
이 나라의 국왕 김지민은 다음과 같은 문제를 내고 큰 상금을 걸었다.
길이가 N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S를 정의하자.
S = A[0]*B[0] + ... + A[N-1]*B[N-1]
S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자.
단, B에 있는 수는 재배열하면 안 된다.
S의 최솟값을 출력하는 프로그램을 작성하시오.
"""
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=B[:]
C.sort()
A.sort()
sum=0
for i in range(N):
    sum+=A[i]*C[-(i+1)]
print(sum)

"""
양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다.
어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오
첫째 줄에 N의 진짜 약수의 개수가 주어진다.
이 개수는 50보다 작거나 같은 자연수이다.
둘째 줄에는 N의 진짜 약수가 주어진다.
1,000,000보다 작거나 같고, 2보다 크거나 같은 자연수이고, 중복되지 않는다.
"""
N=int(input())
list=list(map(int,input().split()))
list.sort()
if N==1:
    print(list[0]*list[0])
else:
    print(list[0]*list[-1])

"""
체스판은 8*8크기이고, 검정 칸과 하얀 칸이 번갈아가면서 색칠되어 있다.
가장 왼쪽 위칸 (0,0)은 하얀색이다.
체스판의 상태가 주어졌을 때, 하얀 칸 위에 말이 몇 개 있는지 출력하는 프로그램을 작성하시오.
첫째 줄부터 8개의 줄에 체스판의 상태가 주어진다. ‘.’은 빈 칸이고, ‘F’는 위에 말이 있는 칸이다.
첫째 줄에 문제의 정답을 출력한다.
"""
list=[]
for i in range(8):
    list.append(input())
count=0
line=1
for i in range(8):
    if line%2==1:
        for j in range(0,8,2):
            if list[i][j]=="F":
                count+=1
        line+=1
    else:
        for j in range(1,8,2):
            if list[i][j]=="F":
                count+=1
        line+=1
print(count)
"""
국가대표팀의 감독이 된 이후에 상근이는 매우 게을러졌다.
그는 선수의 이름을 기억하지 못하고, 각 선수의 능력도 알지 못한다.
따라서, 누가 선발인지 기억하기 쉽게 하기 위해 성의 첫 글자가 같은 선수 5명을 선발하려고 한다
만약, 성의 첫 글자가 같은 선수가 5명보다 적다면, 상근이는 내일 있을 친선 경기를 기권하려고 한다.
상근이는 내일 경기를 위해 뽑을 수 있는 성의 첫 글자를 모두 구해보려고 한다.
첫째 줄에 선수의 수 N (1 ≤ N ≤ 150)이 주어진다. 다음 N개 줄에는 각 선수의 성이 주어진다.
(성은 알파벳 소문자로만 이루어져 있고, 최대 30글자이다)
상근이가 선수 다섯 명을 선발할 수 없는 경우에는 "PREDAJA" (따옴표 없이)를 출력한다.
PREDAJA는 크로아티아어로 항복을 의미한다. 선발할 수 있는 경우에는 가능한 성의 첫 글자를 사전순으로 공백없이 모두 출력한다.
"""
N=int(input())
list=[]
for i in range(N):
    list.append(input().split()[0][0])
flag=False
for i in range(97,123):
    count=0
    for j in list:
        if chr(i)==j:
            count+=1
    if count>=5:
        flag=True
        print(chr(i), end="")
if flag==False:
    print("PREDAJA")
