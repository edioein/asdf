import streamlit as st
import time

# 초기 변수 설정
if '잔여시간' not in st.session_state:
    st.session_state['잔여시간'] = 0
if 'cnt' not in st.session_state:
    st.session_state['cnt'] = 0
if 'running' not in st.session_state:
    st.session_state['running'] = False

# 타이머 시작 함수
def start_timer():
    st.session_state['잔여시간'] = 5  # 5초로 설정
    st.session_state['cnt'] = 0
    st.session_state['running'] = True
    update_timer()

# 타이머 업데이트 함수
def update_timer():
    if st.session_state['잔여시간'] > 0:
        st.session_state['잔여시간'] -= 1
        st.text(f"Time left: {st.session_state['잔여시간']} seconds")
        time.sleep(1)  # 1초 대기 후 타이머 갱신
        update_timer()  # 재귀적으로 타이머 업데이트
    else:
        st.session_state['running'] = False
        st.text(f"최종횟수: {st.session_state['cnt']}")
        st.text("TIME OVER")

# 클릭 함수
def click():
    if st.session_state['running']:
        st.session_state['cnt'] += 1
        st.text(f"현재 횟수: {st.session_state['cnt']}")

# 리셋 함수
def reset():
    st.session_state['cnt'] = 0
    st.session_state['잔여시간'] = 0
    st.session_state['running'] = False
    st.text(f"현재 횟수: {st.session_state['cnt']}")

# Streamlit 인터페이스 설정
st.title('주어진 시간동안 최대한 많이 클릭하세요!')

# 현재 클릭 횟수와 남은 시간 표시
st.text(f"현재 횟수: {st.session_state['cnt']}")

# 타이머 시작 버튼
if st.button('Start Timer'):
    start_timer()

# 클릭 버튼
if st.button('Button') and st.session_state['running']:
    click()

# 리셋 버튼
if st.button('Reset'):
    reset()

# 타이머 상태에 따라 UI 업데이트
if st.session_state['running']:
    st.text(f"Time left: {st.session_state['잔여시간']} seconds")
else:
