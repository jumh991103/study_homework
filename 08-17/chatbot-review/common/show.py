import streamlit as st
from .constants import  ROLE

#함수로 만들지 클래스로 만들지 여기서 결정해야함.
#둘의 차이는 함수는 함수안의 변수가 사라짐.. 함수안의 변수를 누군가가 기억했으면 좋겠다면
#클래스를 써야함.(기억할건 생성함수에 쓰면됨.)

#여기선 코딩좋아를 기억할필요없으니까 함수쓰면됨.

def show_msg(role:ROLE, msg:str, is_history=False)->None: 
    #검증로직

    assert isinstance(role, ROLE), "정상적인 코드가 아닙니다."

    with st.chat_message(role.name):
        st.markdown(msg)

    if not is_history:
        #사용자
        st.session_state.history.append(
                {
                    "role":role,  #객체가 저장된것
                    "msg":msg      #문자열이 저장된것
                }
            )

    #history가 부를떄랑 app이 부를떄랑 로직이 달라야겠지? 안그럼 두번 저장하게되니까.
