"""
2048 게임은 4×4 크기의 보드에서 혼자 즐기는 재미있는 게임이다. 이 링크를 누르면 게임을 해볼 수 있다. (https://play2048.co/)
이 게임에서 한 번의 이동은 보드 위에 있는 전체 블록을 상하좌우 네 방향 중 하나로 이동시키는 것이다.
이때, 같은 값을 갖는 두 블록이 충돌하면 두 블록은 하나로 합쳐지게 된다.
한 번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없다.
(실제 게임에서는 이동을 한 번 할 때마다 블록이 추가되지만, 이 문제에서 블록이 추가되는 경우는 없다)
첫째 줄에 보드의 크기 N (1 ≤ N ≤ 20)이 주어진다.
둘째 줄부터 N개의 줄에는 게임판의 초기 상태가 주어진다.
0은 빈 칸을 나타내며, 이외의 값은 모두 블록을 나타낸다.
블록에 쓰여 있는 수는 2보다 크거나 같고, 1024보다 작거나 같은 2의 제곱꼴이다.
블록은 적어도 하나 주어진다.
이 문제에서 다루는 2048 게임은 보드의 크기가 N×N 이다.
보드의 크기와 보드판의 블록 상태가 주어졌을 때, 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하는 프로그램을 작성하시오.
최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출력한다.
"""
N=int(input())
game=[]
for i in range(N):
    game.append(list(map(int,input().split())))
game2=game[:]

def right():
    global game
    for i in range(N):
        for j in range(N-2,-1,-1):
            for k in range(j,N-1):
                if game[i][k+1]==game[i][k]:
                    game[i][k+1]=str(game[i][k+1]*2)
                    game[i][k]=0
                    break
                elif game[i][k+1]==0 or game[i][k+1]=='0':
                    game[i][k+1]=game[i][k]
                    game[i][k]=0
                else:
                    break
    for i in range(N):
        for j in range(N):
            game[i][j]=int(game[i][j])
    return

def left():
    global game
    for i in range(N):
        for j in range(1,N):
            for k in range(j,0,-1):
                if game[i][k-1]==game[i][k]:
                    game[i][k-1]=str(game[i][k-1]*2)
                    game[i][k]=0
                    break
                elif game[i][k-1]==0 or game[i][k-1]=='0':
                    game[i][k-1]=game[i][k]
                    game[i][k]=0
                else:
                    break
    for i in range(N):
        for j in range(N):
            game[i][j]=int(game[i][j])
def up():
    global game
    for i in range(N):
        for j in range(1,N):
            for k in range(j,0,-1):
                if game[k-1][i]==game[k][i]:
                    game[k-1][i]=str(game[k-1][i]*2)
                    game[k][i]=0
                    break
                elif game[k-1][i]==0 or game[k-1][i]=='0':
                    game[k-1][i]=game[k][i]
                    game[k][i]=0
                else:
                    break
    for i in range(N):
        for j in range(N):
            game[i][j]=int(game[i][j])
def down():
    global game
    for i in range(N):
        for j in range(N-1,-1,-1):
            for k in range(j,N-1):
                if game[k+1][i]==game[k][i]:
                    game[k+1][i]=str(game[k+1][i]*2)
                    game[k][i]=0
                    break
                elif game[k+1][i]==0 or game[k+1][i]=='0':
                    game[k+1][i]=game[k][i]
                    game[k][i]=0
                else:
                    break
    for i in range(N):
        for j in range(N):
            game[i][j]=int(game[i][j])
    return
"""
up()
for i in range(N):
    print(game[i])
"""
player=[]
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                for e in range(4):
                    player.append([a,b,c,d,e])
score_list=[]
def play():
    global N
    global game
    global game2
    global score_list
    for i in range(4*4*4*4*4):
        game = game2[:]
        for j in range(5):
            if player[i][j]==0:
                down()
            if player[i][j]==1:
                up()
            if player[i][j]==2:
                right()
            if player[i][j]==3:
                left()
        for z in range(N):
            score_list.append(max(game[z]))
    return
play()
print(max(score_list))

"""
저번에 풀었던 다른 문제처럼 up() down() left() right()를 만들었다.
그 이유는 끝에서 첫번째 자리는 1번만 실행하지만 중간에 0이 여러번 있는 경우 0을 계속 통과하고 끝까지 가야되기 때문에
j 안에 k라는 for문을 또 만들었다.
그리고 4 4 4 4 같은 경우 뭉치면 8 8 0 0 이 되어야하는데 일반적으로 하면 8과 8이 만나 한 번에 16 0 0 0 이 되는 현상이 생겨서
4와 4가 처음 for문으로 합쳐졌을때 int 8이 아닌 str 8로 바꿔 저장되게 해서, 다음 for문에서 8과 만나더라도 8과 str(8)이 다르기 때문에
같다고 인식하지 않고 부딪히도록 만들었다.
그리고 딱 5번만 이동하고, up down left right 4개 중에 하나를 하기 때문에
저번과 동일한 방법으로 for문을 5번 돌리고 1,2,3,4를 갖도록 했다.
대신 이번엔 up up 처럼 두 번해도 다른 결과가 나올 수 있기 때문에 총 경우의 수를 4*4*4*4*4로 했다.
그렇게 5번 이동해서 game이 끝나면, for문으로 훑어서 행 별로 최대 숫자를 뽑아서 score_list에 저장시켰다.
그리고 초기화 되도록 저번처럼 game2를 만들어서 game2[:]를 이용했다.
또 테스트 케이스는 다 되는데 채점하면 실패가 뜬다 ㅎ
테스트 케이스가 1*1, 2*2, 20*20 인 경우도 정상적으로 되는 건 확인했다. 
"""
