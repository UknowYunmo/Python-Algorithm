N,M=map(int,input().split())
game=[]
where_R=[0,0]
where_B=[0,0]
for i in range(0,N):
    game.append(input())
def find():
    for i in range(0,N):
        for j in range(0,M):
            if game[i][j]=='R':
                where_R[0]=i
                where_R[1]=j
    for i in range(0,N):
        for j in range(0,M):
            if game[i][j]=='B':
                where_B[0]=i
                where_B[1]=j
    return
def down():
    find()
    a=where_R[0]
    b=where_R[1]
    c=where_B[0]
    d=where_B[1]
    for i in range(a+1,N):
        if game[a+1][b]=="#" or game[a+1][b]=="B":
            break
        if game[i][b]=="O":
            print("---게임 종료!!---")
            break
        if game[i][b]=="#" or game[i][b]=="B":
            game[a]=game[a][0:b]+"."+game[a][b+1:]
            game[i-1]=game[i-1][0:b]+"R"+game[i-1][b+1:]
            break
    for i in range(c+1,N):
        if game[c+1][d]=="#" or game[c+1][d]=="R":
            break
        if game[i][d]=="O":
            print("---패배---")
            break
        if game[i][d]=="#" or game[i][d]=="R":
            game[c]=game[c][0:d]+"."+game[c][d+1:]
            game[i-1]=game[i-1][0:d]+"B"+game[i-1][d+1:]
            break
    return
def right():
    find()
    a=where_R[0]
    b=where_R[1]
    c=where_B[0]
    d=where_B[1]
    for i in range(b+1,M):
        if game[a][b+1]=="#" or game[a][b+1]=="B":
            break
        if game[a][i]=="O":
            print("---게임종료!!---")
            break
        if game[a][i]=="#" or game[a][i]=="B":
            game[a]=game[a][0:b]+"."+game[a][b+1:i-1]+"R"+game[a][i:]
            break
    for i in range(d+1,M):
        if game[c][d+1]=="#" or game[c][d+1]=="R":
            break
        if game[c][i]=="O":
            print("---패배---")
            break
        if game[c][i]=="#" or game[c][i]=="R":
            game[c]=game[c][0:d]+"."+game[c][d+1:i-1]+"B"+game[c][i:]
            break
    return

def left():
    find()
    a=where_R[0]
    b=where_R[1]
    c=where_B[0]
    d=where_B[1]
    for i in range(b-1,-1,-1):
        if game[a][b-1]=="#" or game[a][b-1]=="B":
            break
        if game[a][i]=="O":
            print("---게임 종료!!---")
            break
        if game[a][i]=="#" or game[a][i]=="B":
            game[a]=game[a][0:i+1]+"R"+game[a][i+2:b]+"."+game[a][b+1:]
            break
    for i in range(d-1,-1,-1):
        if game[c][d-1]=="#" or game[c][d-1]=="R":
            break
        if game[c][i]=="O":
            print("---패배---")
            break
        if game[c][i]=="#" or game[c][i]=="R":
            game[c]=game[c][0:i+1]+"B"+game[c][i+2:d]+"."+game[c][d+1:]
            break
    return
def up():
    find()
    a=where_R[0]
    b=where_R[1]
    c=where_B[0]
    d=where_B[1]
    for i in range(a-1,-1,-1):
        if game[a-1][b]=="#" or game[a-1][b]=="R":
            break
        if game[i][b]=="O":
            print("---게임 종료!!---")
            break
        if game[i][b]=="#" or game[i][b]=="B":
            game[a]=game[a][0:b]+"."+game[a][b+1:]
            game[i+1]=game[i+1][0:b]+"R"+game[i+1][b+1:]
            break
    for i in range(a-1,-1,-1):
        if game[c-1][d]=="#" or game[c-1][d]=="B":
            break
        if game[i][d]=="O":
            print("---패배---")
            break
        if game[i][d]=="#" or game[i][d]=="R":
            game[c]=game[c][0:d]+"."+game[c][d+1:]
            game[i+1]=game[i+1][0:d]+"B"+game[i+1][d+1:]
            break
    return
down()
down()
print("------내려--------")
for i in range(0,N):
    print(game[i])
print("------오른쪽--------")
right()
right()
for i in range(0,N):
    print(game[i])
print("------왼쪽--------")
left()
left()
for i in range(0,N):
    print(game[i])
print("------올려--------")
up()
up()
for i in range(0,N):
    print(game[i])

"""
R 또는 B 구슬이 # 뿐만 아니라 다른 구슬을 만들 떄 멈추도록 수정했고
다음 #을 만나기 전 O(구멍)을 만날 경우 게임 종료 또는 게임 패배를 출력하도록 만들었다
기능은 다 만들었는데 이제 문제는 내가 직접 결정하는 것이 아니라
모든 경우의 수를 해서 최적의 수를 찾아야하기 때문에 모든 함수를 써보고
cnt를 1씩 더하게 해서? 해야하나.. 그 방법을 좀 생각해 봐야될 것 같다.
"""