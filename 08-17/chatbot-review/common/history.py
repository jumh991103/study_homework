import streamlit as st
from common.show import show_msg

#여기서는 함수, 클래스 뭐써야함?
#함수!! 왜 ? 기억해야하는거아님? no
# 이미 session_state요놈이 서버에 저장하고있음.


def init_history()->None:
    if "history" not in st.session_state:

        st.session_state.history = [ #history는 리스트가 가장좋음. set은 중복답변 지워ㅓ릴수있으니 안되고, dict는 키를 계속 생성해줘야하니깐 굳이임. 튜플은 추가(수정)이 안됨. 바로 오류남. 그래서 리스트 써야함.
            
        ]


    for h in st.session_state.history:
        show_msg(**h, is_history=True)

        #is_history=True -> 너 트루야? 라고 얘기해줘야 show에서 함수돌릴때
        #맨아래 함수를  history가 안씀