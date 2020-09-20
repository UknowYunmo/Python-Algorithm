"""
1. 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다.
수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

mylist=[]
minus=0
for i in range(0,10):
    a=int(input())
    if a>=42:
        a=a%42
    mylist.append(a)
mylist.sort()
for i in range(1,10):
    if mylist[i]==mylist[i-1]:
        minus+=1
print(10-minus)

2. 세준이는 기말고사를 망쳤다. 세준이는 점수를 조작해서 집에 가져가기로 했다. 일단 세준이는 자기 점수 중에 최댓값을 골랐다.
이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.
예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.
세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.

N=int(input())
mylist=list(map(int,input().split()))
mylist2=[]
sum=0
M=mylist[0]
for i in range(0,N):
    if mylist[i]>M:
        M=mylist[i]
for i in range(0,N):
    mylist2.append(int(mylist[i])/M*100)
for i in range(0,N):
    sum+=mylist2[i]
avg=sum/N
print(avg)

3. "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다.
문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

N=int(input())
case_list=[]
for i in range(0,N):
    case_list.append(input())
for i in range(0,N):
    score=0
    sum=0
    for j in range(0,len(case_list[i])):
        if case_list[i][j]=='O':
            score+=1
            sum+=score
        if case_list[i][j]=='X':
            score=0
    print(sum)

4. 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다.
점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
"""

C=int(input())
mylist=[]
avglist=[]
for i in range(0,C):
    mylist.append(list(map(int,input().split())))
for i in range(0,C):
    sum=0
    avg=0
    for j in range(0,mylist[i][0]):
        sum+=mylist[i][j+1]
    avg=sum/mylist[i][0]
    avglist.append(avg)
for i in range(0,C):
    count=0
    for j in range(0,mylist[i][0]):
        if mylist[i][j+1]>avglist[i]:
            count+=1
    student=count/mylist[i][0]*100
    print('%.3f'% student,end="%\n")
    """
    이렇게 하면 무조건 3자리수까지 나옴
    그래서 40.000%라고 나올때도 있는데 만약 이렇게 3자리 이하도 가능할 경우에는 2자리 이하로 나오게 하고 싶을때는
    print(round(count/mylist[i][0]*100,3),end="%\n")로
    round 함수를 이용하면 가능하다
    그리고 리스트에 내용을 넣을 때 무조건 append()를 써야된다.
    list[X]=N 이런식으로 입력이 가능할 때는 수정할 때만 되는거 같다.
    """
    #print(round(count/mylist[i][0]*100,3),end="%\n")