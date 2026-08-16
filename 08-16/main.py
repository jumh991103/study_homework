#main.py 역할 -> 진입점(entry point) — 프로그램을 실제로 실행시키는 곳
from game.constants import GameType
from game.print import print_game_result
from game.print import print_game_result_rspmo
from game.print import print_game_result_mjp
from game.rsp_game import do_game
from game.rspmo_game import do_rspmo_game
from game.mjp_game import do_mjp_game


def game_run(game_type:GameType = GameType.rsp):  #각각의 게임들의 규칙이나 실행 로직은 각각의 파일을 따로 만들어서 저장해두었음.

    game_result = do_game() if game_type == GameType.rsp else None#만약 묵찌빠, 하나빼기 게임 파일들을 만들게 되면 그 안에서도 함수들 이름은 다 do_game이어야하는건가?
    if game_result:
        print_game_result(
            result = game_result['game_result'], 
            user_input = game_result['사용자의 입력값'],
            computer_value = game_result['컴퓨터의 입력값'] 
        )

def game_rspmo_run(game_type:GameType = GameType.rspmo):  #각각의 게임들의 규칙이나 실행 로직은 각각의 파일을 따로 만들어서 저장해두었음.

    game_result = do_rspmo_game() if game_type == GameType.rspmo else None #만약 묵찌빠, 하나빼기 게임 파일들을 만들게 되면 그 안에서도 함수들 이름은 다 do_game이어야하는건가?
    if game_result:
        print_game_result_rspmo(
            result = game_result['game_result'], 
            user_input = game_result['사용자의 초기 입력값'],
            computer_value = game_result['컴퓨터의 초기 입력값'],
            user_final_input =  game_result["사용자의 최종 입력값"],
            computer_final_value = game_result["컴퓨터의 최종 입력값"]
        )

def game_mjp_run(game_type:GameType = GameType.mjp):

    game_result = do_mjp_game() if game_type == GameType.mjp else None
    if game_result:
        print_game_result_mjp(result = game_result['game_result']
        )

if __name__ =="__main__":
    while True:
        game_choice = input("게임 종류를 선택하시오(rsp, rspmo, mjp):").strip()
        if game_choice not in GameType.__members__:
            print("게임 종류 다시입력해주세요")
            continue

        else:
            if game_choice == "rsp":
                game_run()

            elif game_choice == "rspmo":
                game_rspmo_run()

            else:
                game_mjp_run()

        break
