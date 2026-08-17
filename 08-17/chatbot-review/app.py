import streamlit as st

from common.show import show_msg #보라색은 함수
from common.constants import ROLE #초로색은 상수
from common.history import init_history
from common.ai import get_msg_of_ai


st.title("ChatBot Service") #서비스 제목

init_history()


#사용자 답변
user_input = st.chat_input("매시지를 입력해주세요.") #chat_input은 사용자의 답변을 str로 리턴해줌

if user_input: #user_input이 있다면
    #사용자
    show_msg(**
            {
            "role":ROLE.user,
            "msg":user_input
    })

    #AI
    show_msg(**
        {
            "role":ROLE.assistant,
            "msg":get_msg_of_ai(user_input)
        })