#constats.py 역할 -> 개념/데이터 정의 — 이 프로그램에서 다루는 값들이 뭔지(가위바위보, 승패, 게임종류)

from __future__ import annotations #??
import enum

class RSP(enum.Enum):  # rsp사용할때 인스턴스 따로 안만들고 rsp.rock이런식으로 써도 되는거임? 왜??
    rock = 0
    scissor = 1
    paper = 2

    def is_win(self, computer:RSP) ->str:
        result = (self.value - computer.value)%3
        return GameResult(result).name  #GameResult[result].value 이런식으로 쓰면 tie,win이런걸 얻어낼수있음.

class GameResult(enum.Enum):
    tie = 0
    lose = 1
    win = 2


class GameType(enum.Enum):
    rsp = enum.auto()
    rspmo = enum.auto()
    mjp = enum.auto()  #enum..auto()  -> rsp클래스에서 처럼 각 값들 자체는 별 의미가 없을때 enum.auto로 무작위숫자를 배정해 구분만 할떄 사용

if __name__ == "__main__":  #지금 내가 직접실행된거야 아님 누가 import해서 쓴거야를 컴퓨터가 직접 판단하는데에 쓰임.
    user = RSP.scissor #user에 RSP클래스의 scissor라는 인스트스를 대입
    computer = RSP.rock #computer에 RSP클래스의 rock이라는 인스턴스를 대입
    print(user.is_win(computer))  # scissor인스턴스의 is_win 메소드를 사용(입력값으로 rock 인스턴스)


