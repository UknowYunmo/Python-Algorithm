"""
1.
어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다.
어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다.
예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다.
물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.
자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.
"""

N=input()
sum=0
for i in range(0,len(N)):
    sum+=int(N[i])
N=int(N)
answer=0
for i in range(1,(N-sum)+1):
    str_i=str(i)
    len_i=len(str_i)
    sum2=0
    for j in range(0,len_i):
        sum2+=int(str_i[j])
    if (i+sum2)==N:
        answer=i
        break
print(answer)

# 이상하게 답은 나오는데 잘 올라가다가 틀린다고 나온다..

N=int(input())
answer=0
for i in range(1,N+1):
    str_i=str(i)
    len_i=len(str_i)
    sum2=0
    for j in range(0,len_i):
        sum2+=int(str_i[j])
    if (i+sum2)==N:
        answer=i
        break
print(answer)

# 시간초 맞추려고 좁혔던 sum을 빼는 과정을 빼니까 정답이 떴다.
# 적어도 216이면 합이 9니까 216까지가 아니고 207까지만 돌리게 했었는데 아무래도 209에서 210으로 넘어가는 그런 특별한 케이스에
# 식별자가 걸러지는 경우가 있는 것 같다..