import streamlit as st
import time

# 세션 상태 초기화
if '잔여시간' not in st.session_state:
    st.session_state['잔여시간'] = 0
if 'cnt' not in st.session_state:
    st.session_state['cnt'] = 0
if 'running' not in st.session_state:
    st.session_state['running'] = False
if 'last_update' not in st.session_state:
    st.session_state['last_update'] = time.time()

# 타이머 로직: 매 초 자동으로 감소
if st.session_state['running']:
    now = time.time()
    elapsed = now - st.session_state['last_update']
    if elapsed >= 1:
        st.session_state['잔여시간'] -= int(elapsed)
        st.session_state['last_update'] = now
        if st.session_state['잔여시간'] <= 0:
            st.session_state['running'] = False
            st.session_state['잔여시간'] = 0
        st.rerun()

# 타이머 시작 함수
def start_timer():
    st.session_state['잔여시간'] = 5  # 예: 5초
    st.session_state['cnt'] = 0
    st.session_state['running'] = True
    st.session_state['last_update'] = time.time()

# 클릭 함수
def click():
    if st.session_state['running']:
        st.session_state['cnt'] += 1

# 리셋 함수
def reset():
    st.session_state['cnt'] = 0
    st.session_state['잔여시간'] = 0
    st.session_state['running'] = False

# ---------------------
# UI 영역
st.title('주어진 시간 동안 최대한 많이 클릭하세요!')

st.write(f"⏳ 남은 시간: {st.session_state['잔여시간']}초")
st.write(f"👆 클릭 횟수: {st.session_state['cnt']}")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button('Start Timer'):
        start_timer()

with col2:
    if st.button('Click') and st.session_state['running']:
        click()

with col3:
    if st.button('Reset'):
        reset()

# 종료 메시지
if not st.session_state['running'] and st.session_state['잔여시간'] == 0 and st.session_state['cnt'] > 0:
    st.success(f"⏰ 시간 종료! 최종 클릭 수: {st.session_state['cnt']}회")

