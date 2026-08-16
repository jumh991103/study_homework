#print.py 역할 -> 출력 담당 — 결과를 화면에 어떻게 보여줄지

def print_game_result(result:str, user_input:str = None, computer_value:str = None):
    if user_input and computer_value:
        print(f"사용자 : {user_input}, 컴퓨터 : {computer_value}")

    print(f"사용자가 {result}했습니다.") #if 문밖에 빼놓은 이유가 뭐지? 컴퓨터,사용자값이 입력되어서 그값이 프린트되고나서 결과가 나오는게 맞는거 아냐?

def print_game_result_rspmo(result:str, user_input:list = None, computer_value:str = None, user_final_input:str = None, computer_final_value:str = None):
    if user_input and computer_value and user_final_input and computer_final_value:

        print(f"사용자의 첫 두개: {user_input}, 컴퓨터의 첫 두개 : {computer_value}")
        print(f"사용자의 최종 선택 : {user_final_input}, 컴퓨터의 최종 선택 : {computer_final_value}")

    print(f"사용자가 {result}했습니다.")

def print_game_result_mjp(result:str):
    print(f"사용자가 {result}했습니다.")