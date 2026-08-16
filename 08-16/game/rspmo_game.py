from .input import get_user_two_input
from .input import final_pick
from .constants import RSP
import random

def do_rspmo_game() -> dict:
    user_input = get_user_two_input()
    computer_value = random.choices(list(RSP.__members__),k = 2)  #RSP.__members__는 딕셔너리랑 비슷한 형식의 mappingproxy라서 인덱스 접근이 안되기때문에 list로 바꿔준것

    user_final_input = final_pick(user_input)
    computer_final_value = random.choice(computer_value)

    result = user_final_input.is_win(RSP[computer_final_value])

    
    if result != "tie" :
        return{
            "사용자의 초기 입력값" : user_input,
            "컴퓨터의 초기 입력값" : computer_value,
            "game_result" : result, #user_input은 get_user_input()함수의 리턴값을 저장했는데, 그 리턴값이 RSP 인스턴스였음. 그래서 is_win메소드 사용가능한것
            "사용자의 최종 입력값" : user_final_input.name,
            "컴퓨터의 최종 입력값" : computer_final_value
        }
    else:
        print("무승부입니다.재승부하세요")
        return do_rspmo_game()  #재귀 호출