"""
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M*N 크기의 보드를 찾았다.
어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다.
지민이는 이 보드를 잘라서 8*8 크기의 체스판으로 만들려고 한다.
체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다.
구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다.
따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다.
하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8*8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다.
당연히 8*8 크기는 아무데서나 골라도 된다.
지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
"""
X,Y=map(int,input().split())
chess=[]
for i in range(0,X):
    chess.append(input())

# 검정, 하얀색일때 고쳐야하는 경우의 수를 세야하므로 그걸 체크해주는 함수 만들어서 아닐때 1을 반환해서 그 1을 더해서 비교하려는 설계를 함
def check_B(N):
    if N=="B":
        return 0
    else:
        return 1
def check_W(N):
    if N=="W":
        return 0
    else:
        return 1

sum_1=0 # 첫째줄이 검정으로 시작해서 검하검하검하가 되는게 더 바람직한 경우 고쳐야 되는 체스판 수의 합
sum_2=0 # 첫째줄이 하향으로 시작해서 하검하검하검이 되는게 더 바람직한 경우 고쳐야 되는 체스판 수의 합
for j in range(0,X):
    if j%2==0: # 체스판은 줄이 계속 바뀌기 때문에 줄이 홀수 줄인지, 짝수 줄인지 체크해서 번갈아가며 확인하기 위해 (이 경우 홀수 줄)
        for i in range(0,Y):
            if i%2==0:
                sum_1+=check_B(chess[j][i])
                sum_2+=check_W(chess[j][i])
            else:
                sum_1+=check_W(chess[j][i])
                sum_2+=check_B(chess[j][i])
    else: # 짝수 줄일때
        for i in range(0,Y):
            if i%2==0:
                sum_1+=check_W(chess[j][i])
                sum_2+=check_B(chess[j][i])
            else:
                sum_1+=check_B(chess[j][i])
                sum_2+=check_W(chess[j][i])
print(sum_1)
print(sum_2)

# 여기까지 해서 겨우 끝하고 답안 제출하려는데?? 알고보니까 문제를 잘못 이해했었음
# 예를 들어 10*13 체스판인 경우 그냥 전체 체스판을 다시 칠하는줄 알고 풀었는데, 알고 보니
# 이 10*13 체스판을 8*8 사이즈로 잘랐을때 가장 칠할 개수가 적을 때 자르고, 또 그 다시 칠하는 개수를 구하는거였음
# 그래도 생각해보니까 내가 이미 만들었던거에 범위를 (8,8)로 고정시키고 8을 초과한 경우에 8을 빼면서 for문을 돌리면 되겠다고 생각함
sum_1=0
sum_2=0
cnt_list=[]
for k in range(0,X-7): #처음엔 8을 빼면 된다고 생각했는데, 돌려보니까 8*8 사이즈의 경우 아예 for문이 안 돌아가버려서 7을 빼는게 맞았음
    for p in range(0,Y-7):
        for j in range(0,8): #여기가 내가 아까 만들었던 for문..4중 for문이 되버렸지만 일종의 함수라고 생각하면 사실상 2중 for문처럼 느껴졌음
            if j%2==0:
                for i in range(0,8):
                    if i%2==0:
                        sum_1+=check_B(chess[j+k][i+p])
                        sum_2+=check_W(chess[j+k][i+p])
                    else:
                        sum_1+=check_W(chess[j+k][i+p])
                        sum_2+=check_B(chess[j+k][i+p])
            else:
                for i in range(0,8):
                    if i%2==0:
                        sum_1+=check_W(chess[j+k][i+p])
                        sum_2+=check_B(chess[j+k][i+p])
                    else:
                        sum_1+=check_B(chess[j+k][i+p])
                        sum_2+=check_W(chess[j+k][i+p])
        cnt_list.append(sum_1)
        cnt_list.append(sum_2)
        sum_1=0
        sum_2=0
print(min(cnt_list))
# 시간 초과 뜨더라도 정답만 구하면 여한이 없겠다 생각했는데, 시간 초과도 안 떴음!!

