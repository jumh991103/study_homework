#rsp_game.py 역할 -> 게임 로직(오케스트레이션) — 입력 받고, 계산하고, 결과를 조립

from .input import get_user_input
from .constants import RSP
import random

def do_game() -> dict:
    user_input = get_user_input()
    computer_value = random.choice(list(RSP.__members__))  #RSP.__members__는 딕셔너리랑 비슷한 형식의 mappingproxy라서 인덱스 접근이 안되기때문에 list로 바꿔준것
    result = user_input.is_win(RSP[computer_value])
    
    if result != "tie" :
        return{
            "game_result" : result, #user_input은 get_user_input()함수의 리턴값을 저장했는데, 그 리턴값이 RSP 인스턴스였음. 그래서 is_win메소드 사용가능한것
            "사용자의 입력값" : user_input.name,
            "컴퓨터의 입력값" : computer_value
        }
    else:
        print("무승부입니다.재승부하세요")
        return do_game()  #재귀 호출