"""
1. 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다.
다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
"""
N=int(input())
cnt=0
Num_list=list(map(int,input().split()))
for i in range(0,N):
    num=Num_list[i]
    sosu_x=0
    if num==1:
        sosu_x=1
    else:
        for j in range(2,num):
            if num%j==0:
                sosu_x=1
    if sosu_x==0:
        cnt+=1
print(cnt)
"""
2. 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로,
이들 소수의 합은 620이고, 최솟값은 61이 된다.
"""
M=int(input())
N=int(input())
sosu_list=[]
for i in range(M,N+1):
    sosu_x=0
    if i==1:
        sosu_x=1
    else:
        for j in range(2,i):
            if i%j==0:
                sosu_x=1
                break
    if sosu_x==0:
        sosu_list.append(i)
if len(sosu_list)==0:
    print(-1)
else:
    cnt=0
    for i in range(0,len(sosu_list)):
        cnt+=sosu_list[i]
    print(cnt)
    print(sosu_list[0])
#시간 초과가 계속 걸려서 어디가 잘못됐나했더니 break를 안해줬던게 원인
#뭔가 다중 조건 걸려있을 때 쫄려서 break를 잘 안쓰는 경향이 있었는데 정확히 알고 써야겠다
"""
3. M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다.
(1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
"""
M,N=map(int,input().split())
for i in range(M,N+1):
    sosu_x=0
    if i==1:
        sosu_x=1
    else:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                sosu_x=1
                break
    if sosu_x==0:
        print(i)
# 아무리해도 시간초과가 뜨기에 구글링을 했더니 2부터 i까지 검사하는게 아니라 2부터 i의 제곱근까지만 해도 소수를 충분히 찾을 수 있다고 한다.

