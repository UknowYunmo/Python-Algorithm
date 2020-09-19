"""
1. N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다.
둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

N=int(input())
num_list=list(map(int,input().split()))
num_list.sort()
print(str(num_list[0])+" "+str(num_list[N-1]))

2. 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
예를 들어, 서로 다른 9개의 자연수
3, 29, 38, 12, 57, 74, 40, 85, 61
이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

num_list=[]
count=1
best=0
for i in range(0,9):
    num_list.append(int(input()))
    if num_list[i]>best:
        best=num_list[i]
        count=i+1
print(best)
print(count)

3. 세 개의 자연수 A, B, C가 주어질 때 A×B×C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
예를 들어 A = 150, B = 266, C = 427 이라면
A × B × C = 150 × 266 × 427 = 17037300 이 되고,
계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.
"""
A=int(input())
B=int(input())
C=int(input())
result=str(A*B*C)
result_box=[]
count_box=[]
count=0
for i in range(0,10):
    for j in range(0,len(result)):
        if int(result[j])==i:
            count+=1
    count_box.append(count)
print(count_box[0])
for i in range(1,10):
    print(int(count_box[i])-int(count_box[i-1]))

