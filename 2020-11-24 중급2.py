"""
A*B를 계산하다 지겨워진 형택이는 A*B를 새로운 방법으로 정의하려고 한다.

A에서 한 자리를 뽑고 * B에서 임의로 한 자리를 뽑아 곱한다.

의 가능한 모든 조합 (A가 n자리, B가 m자리 수라면 총 가능한 조합은 n*m개)을 더한 수로 정의하려고 한다.

예를 들어 121*34는

1*3 + 1*4 + 2*3 + 2*4 + 1*3 + 1*4 = 28

이 된다. 이러한 형택이의 곱셈 결과를 구하는 프로그램을 작성하시오.

첫째 줄에 A와 B가 주어진다. 주어지는 두 수는 모두 10,000자리를 넘지 않는다.

첫째 줄에 형택이의 곱셈 결과를 출력한다.

"""
#%%
a,b=input().split()
sum=0
for i in range(len(a)):
    for j in range(len(b)):
        sum+=int(a[i])*int(b[j])
print(sum)

# 시간 초과
#%%


a,b=input().split()
Asum = 0
Bsum = 0
for i in range(len(a)):
    Asum+=int(a[i])
for j in range(len(b)):
    Bsum+=int(B[j])
print(Asum*Bsum)

# 어차피 하나씩 뽑아서 전부 곱한걸 합치는 것과 각자 합친걸 곱하는거랑 결과값이 같아서
#  이렇게 하는게 더 빠르다
"""

동호는 내년에 초등학교를 입학한다. 그래서 동호 어머니는 수학 선행 학습을 위해 쉽게 푸는 문제를 동호에게 주었다.

이 문제는 다음과 같다. 1을 한 번, 2를 두 번, 3을 세 번, 이런 식으로 1 2 2 3 3 3 4 4 4 4 5 .. 이러한 수열을 만들고

어느 일정한 구간을 주면 그 구간의 합을 구하는 것이다.

첫째 줄에 구간의 시작과 끝을 나타내는 정수 A, B(1≤A≤B≤1,000)가 주어진다.

즉, 수열에서 A번째 숫자부터 B번째 숫자까지 합을 구하면 된다.

첫 줄에 구간에 속하는 숫자의 합을 출력한다.
"""
#%%
a,b=map(int,input().split())
list=[]

def koo(x):
    global list
    for i in range(x):
        list.append(x)
    return

for i in range(b+1):
    koo(i)

sum=0
for i in range(a,b+1):
    sum+=list[i-1]
    
print(sum)

"""

어떤 수 X가 주어졌을 때, X의 모든 자리수가 역순이 된 수를 얻을 수 있다. Rev(X)를 X의 모든 자리수를 역순으로 만드는 함수라고 하자.

예를 들어, X=123일 때, Rev(X) = 321이다. 그리고, X=100일 때, Rev(X) = 1이다.

두 양의 정수 X와 Y가 주어졌을 때, Rev(Rev(X) + Rev(Y))를 구하는 프로그램을 작성하시오

첫째 줄에 수 X와 Y가 주어진다. X와 Y는 1,000보다 작거나 같은 자연수이다.

첫째 줄에 문제의 정답을 출력한다.

"""
    
#%%
a,b=input().split()

def Rev(x):
    str(x)
    temp_list=[]
    changed_x=0
    flag=0
    exp=1
    for i in range(len(x)-1,-1,-1):
        if flag==0 and x[i]=='0':
            continue
        temp_list.append(x[i])
        flag+=1
    for i in range(len(temp_list)-1,-1,-1):
        changed_x+=int(temp_list[i])*exp
        exp*=10
    return(changed_x)

print(Rev(str(Rev(a)+Rev(b))))

# 리스트를 뒤집는 reverse 함수도 있던데 어차피 연산하려면 또 숫자로 풀어야되서 그냥 직접 만들었다.
