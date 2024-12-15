import streamlit as st
from streamlit.components.v1 import html


def init_session_state():
    if 'character' not in st.session_state:
        st.session_state.character = None

def main():
    st.markdown(
        """
        <style>
        /* 메인 영역 스타일 */
        .stApp {
            background-color: black; /* 배경 흰색 */
            color: white !important; /* 텍스트 검은색 */
        }

        /* 버튼 스타일 */
        .stButton > button {
            color: white;
            background-color: transparent;
            border: 1px solid white;
        }
        .stButton > button:hover {
            color: black;
            background-color: white;
        }
        
        /* 제목 스타일 */
        h1, h2, h3, h4, h5, h6 {
            color: white !important; /* 모든 제목을 검은색으로 설정 */
        }
        style>
        """,
        unsafe_allow_html=True
    )
    


    
    init_session_state()
    
    # 첫 페이지
    if st.session_state.character is None:
        st.image('6.25 인생게임 프로토타입.png', use_container_width=True)
        st.write('6.25 전쟁상황으로 당신을 초대합니다.')
        st.write('▽ 아래 버튼을 클릭하세요.')
        st.markdown(
            """
            <script>
            document.addEventListener('keydown', function(event) {
                if (event.key) {
                    document.querySelector('button[aria-label="캐릭터 선택"]').click();
                }
            });
            </script>
            """,
            unsafe_allow_html=True
        )
        st.session_state.character = ''

        if st.button('캐릭터 선택'):
            pass
        st.session_state.character     
  
    # 캐릭터 선택 화면
    else:
        
        st.markdown("<h2 style='color: white;'>등장인물을 선택하세요</h2>", unsafe_allow_html=True)
        character_options = ['','피난민', '국군']
        character = st.selectbox('',character_options)


        
        if character == '피난민':
            st.image('refugees.png', use_container_width=True)        
        elif character == '국군':
            st.image('s_soldier.png', use_container_width=True)


        # 버튼들을 위한 컬럼 생성
        col1, col2 = st.columns([4,1])
        
        # 선택 완료 버튼은 왼쪽 컬럼에
        with col1:
            if st.button('선택 완료'):
                st.session_state.character = character
                if character == '피난민':
                   # JavaScript를 사용하여 새 탭에서 URL 열기
                    html("""
                    <script type="text/javascript">
                    window.open("https://625refugee.streamlit.app/", "_blank").focus();
                    </script>
                    """)
                elif character == '국군':
                    html("""
                    <script type="text/javascript">
                    window.open("https://625soldier.streamlit.app/", "_blank").focus();
                    </script>
                    """)
           
        
        # 처음으로 버튼은 오른쪽 컬럼에
        with col2:
            if st.button('← 처음으로 \n\n (두번클릭)'):
                st.session_state.character = None
                st.session_state.page_refresh = not st.session_state.get('page_refresh', False)


if __name__ == '__main__':
    main()


