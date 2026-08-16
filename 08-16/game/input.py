#input.py 역할 -> 입력 담당 — 사용자로부터 값을 받고 검증 

from .constants import RSP

def get_user_input() -> RSP :  # 왜 리턴값이 RSP클래스임?
    user_input = input("rock,scissor,paper 중에 하나 입력해주세요.").strip()

    #검증로직 추가
    if user_input not in RSP.__members__: # enum클래스.__members__ => 그 클래스 안에 소속된 모든 멤버를 조회할수있게함(읽기전용(수정안됨.) 딕셔너리 형식으로)
        print("다시 입력해주세요 제발...")
        return get_user_input()       #재귀 호출(자기자신을 다시 실행시킴)

    return RSP[user_input] #이 함수를 누가쓸지 호출한 파일,함수에서 어떤 값형태가 사용하기 편한지를 생각해서 리턴값의 형식을 선택해야함... 모듈화 어렵네...


def get_user_two_input() -> str :
    user_input_1 = input("rock,scissor,paper 중에 한개 입력해주세요.").strip()
    user_input_2 = input("rock,scissor,paper 중에 한개 더 입력해주세요.").strip()

    if user_input_1 not in RSP.__members__ or user_input_2 not in RSP.__members__:
        print("다시 입력해주세요.")
        return get_user_two_input()

    return [user_input_1, user_input_2]

def final_pick(choices:list) ->RSP : 

    user_final_pick = input("먼저 입력한 두가지 중 하나를 입력해주세요.").strip()

    if user_final_pick not in choices:
        print("다시 골라주세요.이전에 고르신 두개중에 하나를 입력해주세요")
        return final_pick(choices) #재귀호출에서도 반드시 필수 파라미터는 넘겨줘야함. final_pick() 불가능

    return RSP[user_final_pick]







    
if __name__ == "__main__":    #이 파일을 단독실행해서 잘 작동하는지 체크하기위해 넣었음 만약 이거안넣고 그냥 print~~~했으면 나중에 main 실행했는데 print~~~가 실행됨.
    print(get_user_input())   #주피터 노트북에선 한섹션씩 실행시키면서 작동확인했으면 됐는데 .py파일은 그게 안되니까