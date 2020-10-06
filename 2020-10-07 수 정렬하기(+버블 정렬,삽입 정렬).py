"""
1. N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다.
수는 중복되지 않는다.
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
"""
# 1. 내가 사랑하는 sort() 정렬
N = int(input())
list_box=[]
for i in range(0,N):
    list_box.append(int(input()))
list_box.sort()
for i in range(0,len(list_box)):
	print(list_box[i])

# 이제 백준이 설명한 버블 정렬, 삽입 정렬에 대해 알아보자..

# 2. 버블 정렬이란걸 해보자 - 뒤에 꺼랑 계속해서 비교해가면서 위치 바꾸기
N=int(input())
list_box=[]
for i in range(0,N):
    list_box.append(int(input()))
for j in range(0,N):
    for k in range(0,N-(j+1)):
        if list_box[k] >= list_box[k+1]:
            list_box[k+1], list_box[k] = list_box[k], list_box[k+1]
print(list_box)

# 3. 삽입 정렬이란걸 해보자 - 최소값을 계속 구해가면서 그 값을 입력시키기
N=int(input())
list_box=[]
for i in range(N):
    list_box.append(int(input()))
for j in range(len(list_box)-1):
    minn = min(list_box[j:]) #j 부터 끝까지의 최소값 구하기
    index = list_box.index(minn) #그거의 인덱스
    list_box[index] = list_box[j]
    list_box[j] = minn
print(list_box)

# 아 참고로 부등호를 반대로해보니 내림차순으로 정렬이 되더라.
