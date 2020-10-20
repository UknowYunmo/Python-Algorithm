N, M = map(int, input().split())
game = []
where_R = [0, 0]
where_B = [0, 0]
game_end = False
game_over = False
for i in range(0, N):
    game.append(input())
game2=game[:]

def find():
    for i in range(0, N):
        for j in range(0, M):
            if game[i][j] == 'R':
                where_R[0] = i
                where_R[1] = j
    for i in range(0, N):
        for j in range(0, M):
            if game[i][j] == 'B':
                where_B[0] = i
                where_B[1] = j
    return


def down():
    global game_end
    global game_over
    find()
    a = where_R[0]
    b = where_R[1]
    c = where_B[0]
    d = where_B[1]
    for i in range(a + 1, N):
        if game[a + 1][b] == "#" or game[a + 1][b] == "B":
            break
        if game[i][b] == "#" or game[i][b] == "B":
            game[a] = game[a][0:b] + "." + game[a][b + 1:]
            game[i - 1] = game[i - 1][0:b] + "R" + game[i - 1][b + 1:]
            break
        if game[i][b] == "O":
            game[a]= game[a][0:b]+"."+game[a][b+1:]
            game_end = True
            break
    for i in range(c + 1, N):
        if game[c + 1][d] == "#" or game[c + 1][d] == "R":
            break
        if game[i][d] == "#" or game[i][d] == "R":
            game[c] = game[c][0:d] + "." + game[c][d + 1:]
            game[i - 1] = game[i - 1][0:d] + "B" + game[i - 1][d + 1:]
            break
        if game[i][d] == "O":
            game_over = True
            break
    return


def right():
    global game_end
    global game_over
    find()
    a = where_R[0]
    b = where_R[1]
    c = where_B[0]
    d = where_B[1]
    for i in range(b + 1, M):
        if game[a][b + 1] == "#" or game[a][b + 1] == "B":
            break
        if game[a][i] == "#" or game[a][i] == "B":
            game[a] = game[a][0:b] + "." + game[a][b + 1:i - 1] + "R" + game[a][i:]
            break
        if game[a][i] == "O":
            game[a]= game[a][0:b]+"."+game[a][b+1:]
            game_end = True
            break
    for i in range(d + 1, M):
        if game[c][d + 1] == "#" or game[c][d + 1] == "R":
            break
        if game[c][i] == "#" or game[c][i] == "R":
            game[c] = game[c][0:d] + "." + game[c][d + 1:i - 1] + "B" + game[c][i:]
            break
        if game[c][i] == "O":
            game_over = True
            break
    return


def left():
    global game_end
    global game_over
    find()
    a = where_R[0]
    b = where_R[1]
    c = where_B[0]
    d = where_B[1]
    for i in range(b - 1, -1, -1):
        if game[a][b - 1] == "#" or game[a][b - 1] == "B":
            break
        if game[a][i] == "#" or game[a][i] == "B":
            game[a] = game[a][0:i + 1] + "R" + game[a][i + 2:b] + "." + game[a][b + 1:]
            break
        if game[a][i] == "O":
            game[a]= game[a][0:b]+"."+game[a][b+1:]
            game_end = True
            break
    for i in range(d - 1, -1, -1):
        if game[c][d - 1] == "#" or game[c][d - 1] == "R":
            break
        if game[c][i] == "#" or game[c][i] == "R":
            game[c] = game[c][0:i + 1] + "B" + game[c][i + 2:d] + "." + game[c][d + 1:]
            break
        if game[c][i] == "O":
            game_over = True
            break
    return


def up():
    global game_end
    global game_over
    find()
    a = where_R[0]
    b = where_R[1]
    c = where_B[0]
    d = where_B[1]
    for i in range(a - 1, -1, -1):
        if game[a - 1][b] == "#" or game[a - 1][b] == "R":
            break
        if game[i][b] == "#" or game[i][b] == "B":
            game[a] = game[a][0:b] + "." + game[a][b + 1:]
            game[i + 1] = game[i + 1][0:b] + "R" + game[i + 1][b + 1:]
            break
        if game[i][b] == "O":
            game[a]= game[a][0:b]+"."+game[a][b+1:]
            game_end = True
            break
    for i in range(a - 1, -1, -1):
        if game[c - 1][d] == "#" or game[c - 1][d] == "B":
            break
        if game[i][d] == "#" or game[i][d] == "R":
            game[c] = game[c][0:d] + "." + game[c][d + 1:]
            game[i + 1] = game[i + 1][0:d] + "B" + game[i + 1][d + 1:]
            break
        if game[i][d] == "O":
            game_over = True
            break
    return

special_list = []


def play():
    global game
    global game2
    global game_over
    global game_end
    for i in range(2048):
        game=game2[:]
        cnt = 0
        game_over = False
        game_end = False
        for j in range(10):
            cnt += 1
            if player[i][j] == 1:
                down()
            elif player[i][j] == 2:
                up()
            elif player[i][j] == 7:
                right()
            elif player[i][j] == 8:
                left()
            if game_over == True:
                break
            if game_end == True:
                special_list.append(cnt)
                break
    return


player = []
for a in range(1, 3):
    for b in range(7, 9):
        for c in range(1, 3):
            for d in range(7, 9):
                for e in range(1, 3):
                    for f in range(7, 9):
                        for g in range(1, 3):
                            for h in range(7, 9):
                                for i in range(1, 3):
                                    for j in range(7, 9):
                                        player.append([a, b, c, d, e, f, g, h, i, j])
for a in range(7, 9):
    for b in range(1, 3):
        for c in range(7, 9):
            for d in range(1, 3):
                for e in range(7, 9):
                    for f in range(1, 3):
                        for g in range(7, 9):
                            for h in range(1, 3):
                                for i in range(7, 9):
                                    for j in range(1, 3):
                                        player.append([a, b, c, d, e, f, g, h, i, j])
play()
if not special_list:
    print("-1")
else:
    print(min(special_list))

"""
수없이 많은 시행착오를 겪으면서 만든 구슬 탈출 게임
추가한 내용에 대해 설명하자면
오른쪽 왼쪽 위쪽 아래쪽으로 이동하는 경우의 수를 모두 구하기 위해서 1과 2, 그리고 7과 8로 이루어진 2048개의 경우의 수를 뽑았다.
각각 이동 형태는 숫자로 표현했고 10자리 수를 for문 돌려서 숫자에 따라 이동하도록 만들었다.
1과 2 그리고 7,8로 나눈 이유는
예를 들어 처음 아래쪽으로 이동한 경우, 위쪽으로 다시 되돌아가면 의미가 없고, 다시 한 번 아래쪽으로 이동하면 이동하지 않으니 의미가 없으니
왼쪽과 오른쪽 중 골라야 한다. 마찬가지로 그렇게 이동하면 다시 왼쪽과 오른쪽 중에 골라야한다.
그래서 두 가지 중 하나를 선택하는 걸 10번 하는 수열을 만들었다.
10자리로 만든 이유는 10번까지 이동시키고 그 횟수를 넘으면 실패로 치기 때문.
최소 회수를 구하는 방법은 먼저 down() up() left() right() 함수에 R이 O를 만나면
game_end 라는 변수를 True로 만들고 B가 O를 만나면 game_over 라는 변수를 True라 만들게 해놓고
for문에 cnt를 선언해서 위치를 옮기는 함수를 쓸 때마다 1씩 더하게 했고
game_end 또는 game_over가 True가 되는지 확인해서 game_over가 True면 그대로 다음 수열로, 그리고
game_end가 True라면 cnt를 반환하여 special_list에 저장시켰다.
special_list는 10번 이내에 게임이 성공한 경우에 함수를 실행시킨 횟수를 의미하고, special_list의 최소값은
모든 10번 내에 성공한 경우의 수 중 최소 횟수 즉 정답을 의미한다.
또 처음 입력받은 게임 상태를 2048번 반복할 동안 게임을 제자리로 돌려놓는 방법에서 막혔었는데,
이게 뭐가 문제였냐면 list의 원상태를 저장하기 위해 list2를 선언하고 list2=list를 했을때
list가 바뀌면 list2도 같이 바뀌는 상황이 생겨서 막혔었다.
이 때 list2=list[:]를 하면 list의 값만 따오기 때문에 list2는 list의 원형을 유지했고, for문 처음에 list2를 계속 list에 참조시켜서
초기화시켰다.
또 R과 B가 같이 들어가는데 옆에 붙어있을 경우 B도 들어가서 실패가 떠야하는데 옆에 R이 있다고 B가 이동하지 않아서 성공해버리는 케이스도 있어서
그 경우 R을 먼저 이동시키고 R이 성공하면 원래 R의 위치를 .으로 바꾼 뒤 B를 이동시키는 작업을 해줬다.
B는 들어가자마자 실패기 때문에 굳이 이 작업은 하지 않아도 괜찮았다.

...주저리주저리 썼지만 최종 코드 제출 결과 잘 올라가다가 실패가 뜬다.
문제의 테스트 케이스 7개도 다 정답이 나오고, 내가 직접 아무렇게나 막 바꿔서 입력시켜봐도 정답이 나오는데,
애석하게도 실패라고 나온다.
뭐..솔직히 문제를 풀기라도 한 게 뿌듯하기도 하지만, 아무리 그래도 억울하다 적어도 어느 케이스에 틀리는지는 알았으면 좋겠는데 ㅠ
구글로 다른 분들의 문제 풀이들도 찾아봤다.
다들 간략하고 처음 보는 함수로 잘 푸셨는데, 내 잘못된 부분은 알 수 없었다.
그냥 뭐..여기까지 왔는데 포기하긴 아쉬운데 방법이 없어서 주저리주저리 써본다 ㅠㅠ 실력 더 키워서 나중에 다시 풀어야겠다  
"""