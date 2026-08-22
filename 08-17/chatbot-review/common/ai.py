import streamlit as st
from groq import Groq
from dotenv import load_dotenv

from .constants import ROLE #groq에서도 user, assistance를 그대로 씀.

#client는 인터넷 통신할때 사용하는 용어
@st.cache_resource# 스트림릿에서 Singleton 디자인 패턴 저용
def get_client():
    load_dotenv() #.env 파일에 등록된 데이터 환경변수에 저장하는 함수
    return Groq()

def get_msg_of_ai(
    user_input:str, model_name:str="openai/gpt-oss-120b")->str: #기존코드에 input만 입력받도록해놨는데 moedl_name의 기본값을 저장해뒀으므로 코드 안바꿔도 오류안나.

    #과거의 대화했던 내용을 가지고 있어야 ai가 문맥에 맞게 대답할거잖아. history에 있음 대화내용
    
    #이력데이터 추가
    messages = [
        {
            #grok에서는 키값이 role은 맞는데, msg가 아님 그래서 바꿔줄거야
            "role":history['role'].name, #grok은 우리가 만든 객체를 모를거아냐. 그러니까 str을 전달해야함. 그래서 뒤에.name이라고 붙여야하는거임.그럼 str이 리턴되는데 어떤 str? 바로 constants.py에서 user가 이름이고 enum.auto()가 value잖아 그러므로 user가 전달됨.
            "content":history['msg']
        } for history in st.session_state.history
    ]

    #현재메시지 추가 msg
    messages.append({
        "role":ROLE.user.name, #얘또한 바꿔줘야하지 history['role']이 아니라 ㅇㅇ 그리고 얘는 history['role].name이랑 정확히 똑같은 거임.
        "content": user_input
    })

    #ai 호출
    client = get_client()
    response = client.chat.completions.create(
        messages=messages,
        model=model_name
    )

    return response.choices[0].message.content