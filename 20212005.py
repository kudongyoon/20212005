import random
import math

def play():
    # 사용자로부터 선택을 입력받습니다. ('r'은 바위, 'p'는 보, 's'는 가위, 'q'는 게임 종료)
    user = input("당신의 선택은 무엇인가요? 'r'은 바위, 'p'는 보, 's'는 가위, 'q'는 게임 종료\n")
    user = user.lower()

    # 사용자가 'q'를 입력하면 게임 종료
    if user == 'q':
        return ('q', user, None)

    # 컴퓨터의 선택을 무작위로 결정합니다.
    computer = random.choice(['r', 'p', 's'])

    # 사용자와 컴퓨터가 동일한 선택을 했으면 비깁니다.
    if user == computer:
        return (0, user, computer)

    # 바위 > 가위, 가위 > 보, 보 > 바위입니다.
    if is_win(user, computer):
        return (1, user, computer)

    # 사용자가 졌을 경우입니다.
    return (-1, user, computer)

def is_win(player, opponent):
    # 플레이어가 상대를 이겼는지 확인하는 함수입니다.
    # 이기는 조건은 바위 > 가위, 가위 > 보, 보 > 바위입니다.
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

def play_best_of(n):
    # 컴퓨터와 최종적으로 n판 중 다수결로 승패를 결정하는 게임입니다.
    # 이기려면 ceil(n/2)번을 이겨야 합니다. (예: 2/3, 3/5, 4/7)
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    
    # 플레이어와 컴퓨터가 각각 wins_necessary번 이상 이길 때까지 게임을 반복합니다.
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()
        
        # 게임 종료 시
        if result == 'q':
            print("게임이 종료되었습니다. 수고하셨습니다!")
            break
        
        # 비겼을 경우입니다.
        if result == 0:
            print('비겼습니다. 당신과 컴퓨터가 모두 {}를 선택했습니다. \n'.format(user))
        # 사용자가 이겼을 경우입니다.
        elif result == 1:
            player_wins += 1
            print('당신은 {}를 선택했고, 컴퓨터는 {}를 선택했습니다. 당신이 이겼습니다!\n'.format(user, computer))
        else:
            computer_wins += 1
            print('당신은 {}를 선택했고, 컴퓨터는 {}를 선택했습니다. 당신은 졌습니다 :(\n'.format(user, computer))

    # 최종 승패 출력값입니다.
    if result != 'q':  # 게임이 종료되지 않았다면
        if player_wins > computer_wins:
            print('당신이 {}판 중 {}판을 이겼습니다! 멋진 승리입니다 :D'.format(n, player_wins))
        else:
            print('안타깝게도 컴퓨터가 {}판 중 {}판을 이겼습니다. 다음에는 더 잘할 수 있을 거예요!'.format(n, computer_wins))


# 3판 2선승제입니다.
if __name__ == '__main__':
    play_best_of(3)
