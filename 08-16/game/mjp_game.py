from .input import get_user_input
import random
from .constants import RSP
from .constants import GameResult

def do_mjp_game() -> dict:
    while True:
        # 유저와 컴퓨터가 각각 하나씩 가위바위보 중에 고른다.
        user_input = get_user_input()
        computer_value = random.choice(list(RSP.__members__))

        result = user_input.is_win(RSP[computer_value])

        #이긴사람이 공격권을 갖게 되고 다시한번 인풋을 받는다. 비기면 위로 올라가 가위바위보를 다시 한다.

        
        if result == "tie":
            print("무승부! 다시한번 입력하세요")
            continue

        attacker = "user" if result == "win" else "computer"
        print(f"공격자는 {attacker}!")
        break

    while True:
        if attacker == "user":
            print("공격자 입니다. 한번 더 입력하시오")
            user_two_input = get_user_input()
            computer_two_value = random.choice(list(RSP.__members__))

        else :
            print("수비자 입니다. 한번 더 입력하시오")

            user_two_input = get_user_input()
            computer_two_value = random.choice(list(RSP.__members__))
        print(f"user : {user_two_input.name}, computer : {computer_two_value}")
        result = user_two_input.is_win(RSP[computer_two_value])

        if result =="tie" :
            winner = attacker
            print(f"공격자({'user' if winner == 'user' else 'computer'})가 승리했습니다!")
            break
        else:
            new_attacker = "user" if result == "win" else "computer"
            if new_attacker != attacker:
                print(f"공격권이 넘어갑니다!!")
            attacker = new_attacker

    return {"game_result": "win" if winner == "user" else "lose"}


#묵찌빠에서 tie가 나와서 승패가 결정되기 전까지 사용자와 컴퓨터가 무엇을 냈는지를 프린트하고 싶은데 어떻게 해야할지 모르겠다... 
#모듈화를 하기위해 최대한 print는 print.py에서 하려했지만 묵찌빠는 그래되면 매우 이상해짐... 아닌가 방법이 있나.. 