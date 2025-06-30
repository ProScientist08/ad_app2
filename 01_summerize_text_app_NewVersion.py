# 가상환경 생성
# python -m venv myenv
# 가상환경 활성화
# Windows: myenv\Scripts\activate
# MacOS/Linux: source venv/bin/activate
# 패키지 설치
# pip install streamlit 
# pip install openai  


##### 기본 정보 불러오기 ####
# Streamlit 패키지 추가
import streamlit as st
# OpenAI 패키기 추가
import openai

##### 기능 구현 함수 #####
def askGpt(prompt,apikey):
    client = openai.OpenAI(api_key = apikey)
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}])
    gptResponse = response.choices[0].message.content
    return gptResponse

##### 메인 함수 #####
def main():
    st.set_page_config(page_title="요약 프로그램")
    # session state 초기화
    # st.session_state: Streamlit이 사용자의 세션(웹앱에 접속해있는 동안의 상태)을 저장하는 공간입니다. 
    # 여기에 저장된 값은 페이지가 새로고침 되어도 유지됩니다. 
    # "OPENAI_API"라는 키가 세션 상태에 없으면 빈 문자열로 초기화합니다.
    # 이는 사용자가 OpenAI API 키를 입력할 때 사용할 것입니다.
    if "OPENAI_API" not in st.session_state:
        st.session_state["OPENAI_API"] = ""

    # 사이드바
    with st.sidebar:
        # Open AI API 키 입력받기
        open_apikey = st.text_input(label='OPENAI API 키', placeholder='Enter Your API Key', value='',type='password')    
        # 입력받은 API 키 표시
        if open_apikey:
            st.session_state["OPENAI_API"] = open_apikey
        st.markdown('---')

    st.header("📃요약 프로그램")
    st.markdown('---')
    
    text = st.text_area("요약 할 글을 입력하세요")
    if st.button("요약"): 
        # '''...'''는 멀티라인 문자열을 정의하는 방법입니다.
        # f-strings는 문자열 내에 변수를 삽입할 수 있는 방법입니다.
        # 여기서 text 변수에 저장된 내용을 prompt 문자열에 삽입합니다.
        prompt = f'''
        **Instructions** :
    - You are an expert assistant that summarizes text into **Korean language**.
    - Your task is to summarize the **text** sentences in **Korean language**.
    - Your summaries should include the following :
        - Omit duplicate content, but increase the summary weight of duplicate content.
        - Summarize by emphasizing concepts and arguments rather than case evidence.
        - Summarize in 3 lines.
        - Use the format of a bullet point.
    -text : {text}
    '''
        st.info(askGpt(prompt,st.session_state["OPENAI_API"]))

# Main 함수 실행
# 이 부분은 스크립트가 직접 실행될 때만 main() 함수를 호출
# 즉, 다른 모듈에서 import될 때는 실행되지 않습니다.
# 이는 일반적으로 스크립트의 진입점을 정의하는 관례입니다.
# 이렇게 함으로써, 이 스크립트가 다른 곳에서 재사용될 때
# main() 함수가 자동으로 실행되지 않도록 합니다.
# 따라서 이 코드를 다른 모듈에서 import할 때는 main() 함수가 실행되지 않습니다.
# 대신, 이 모듈을 직접 실행할 때만 main() 함수가 실행됩니다.
if __name__=="__main__":
    main()


# 가상환경에 설치된 패키지 목록 확인
# pip freeze > requirements.txt
# requirements.txt 파일을 통해 가상환경에 설치된 패키지 목록을 확인할