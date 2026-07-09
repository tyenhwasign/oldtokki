import streamlit as size_px
from pathlib import Path
import streamlit.components.v1 as components

# 1. 페이지 설정
size_px.set_page_config(
    page_title="3칸 슬롯머신 웹앱",
    page_icon="🎰",
    layout="wide"
)

# 2. 제목 및 소개 문구
size_px.title("🎰 3칸 슬롯머신 시뮬레이터")
size_px.markdown("""
과일과 숫자 7로 이루어진 3칸 슬롯머신 웹앱입니다. 
아래에서 슬롯머신을 돌려 행운을 시험해보세요!
""")

# 3. htmls/index.html 파일 경로 설정
html_path = Path(__file__).resolve().parent / "htmls" / "index.html"

# 4. 파일 존재 여부 확인 및 렌더링
if html_path.exists():
    try:
        # 파일 읽기
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Streamlit 컴포넌트를 통해 HTML 렌더링 (높이는 필요에 따라 조절 가능)
        components.html(html_content, height=800, scrolling=True)
        
    except Exception as e:
        size_px.error(f"⚠️ 파일을 읽는 중 오류가 발생했습니다: {e}")
else:
    # 파일이 없을 때 친절한 한국어 안내 메시지 표시
    size_px.error("⚠️ `htmls/index.html` 파일을 찾을 수 없습니다.")
    size_px.info("""
    **해당 문제를 해결하려면 다음을 확인해주세요:**
    1. 프로젝트 폴더 내에 `htmls` 라는 이름의 폴더가 있는지 확인하세요.
    2. `htmls` 폴더 안에 `index.html` 파일이 정확히 위치해 있는지 확인하세요.
    3. 현재 폴더 구조가 아래와 같은지 확인해 보세요.
    
    ```text
    내-웹앱/
    ├── app.py
    ├── requirements.txt
    └── htmls/
        └── index.htmlimport streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

# 1. 페이지 설정 (웹 브라우저 탭에 표시될 정보)
st.set_page_config(
    page_title="3칸 슬롯머신 웹앱",
    page_icon="🎰",
    layout="wide"
)

# 2. 페이지 제목 및 소개 문구 (한국어 안내)
st.title("🎰 3칸 슬롯머신 시뮬레이터")
st.markdown("""
과일(레몬, 수박, 키위, 바나나, 코코넛, 사과)과 **숫자 7**로 이루어진 3칸 슬롯머신 웹앱입니다.
숫자 7이 3칸 모두에 뜰 확률은 **1%** 이며, 나머지는 무작위로 배열됩니다. 
아래 화면에서 실행 버튼을 눌러 행운을 시험해보세요!
""")

# 3. htmls/index.html 파일의 상대 경로 설정
html_path = Path(__file__).resolve().parent / "htmls" / "index.html"

# 4. HTML 파일 존재 여부 확인 및 Streamlit에 렌더링
if html_path.exists():
    try:
        # 인코딩을 utf-8로 지정하여 HTML 파일 읽기
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # HTML 내용을 전체 화면에 임베드 (높이가 부족할 경우 height 값을 조절하세요)
        components.html(html_content, height=850, scrolling=True)
        
    except Exception as e:
        st.error(f"⚠️ HTML 파일을 읽는 중 오류가 발생했습니다: {e}")
else:
    # 파일이 없을 경우 출력할 친절한 한국어 안내 메시지
    st.error("⚠️ `htmls/index.html` 파일을 찾을 수 없습니다.")
    st.info("""
    **슬롯머신 화면을 띄우기 위해 아래 사항을 확인해 주세요:**
    
    1. 현재 `app.py`가 있는 폴더 안에 **`htmls`**라는 이름의 폴더가 있는지 확인하세요.
    2. 그 `htmls` 폴더 안에 **`index.html`** 파일이 올바르게 들어가 있는지 확인하세요.
    
    **정상적인 프로젝트 구조 예시:**
    ```text
    내-웹앱/
    ├── app.py
    ├── requirements.txt
    └── htmls/
        └── index.html
    ```
    """)
    ```
    """)
