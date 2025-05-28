import streamlit as st
import random

st.set_page_config(
    page_title="고민자판기",
    page_icon="🎰",
    layout="centered"
)


# 고민 종류와 응답 정의
concern_categories = ["연애", "직장", "학교", "가족", "진로", "자존감", "우울", "불안", "외로움", "인간관계"]

responses = {
    "연애": ["사랑은 때로 아프지만, 당신은 소중한 사람입니다.", "상대의 마음도 중요하지만, 당신 마음도 잊지 마세요."],
    "직장": ["일이 힘들 땐 잠깐 쉬어가는 것도 용기예요.", "작은 성공도 큰 의미가 있어요."],
    "학교": ["성적보다 중요한 건 당신의 마음입니다.", "꾸준함이 결국 성과로 이어져요."],
    "가족": ["가족과의 대화는 천천히 시작해도 좋아요.", "당신의 노력은 분명히 의미 있어요."],
    "진로": ["정답은 없어요. 다양한 길이 열려 있어요.", "조급해하지 말고 천천히 걸어가세요."],
    "자존감": ["당신은 존재만으로도 충분히 소중해요.", "스스로에게 친절해지려 노력해보세요."],
    "우울": ["지금은 많이 힘들겠지만, 이 감정은 지나갈 수 있어요.", "작은 변화부터 천천히 시도해보세요."],
    "불안": ["불안은 자연스러운 감정임을 기억하세요.", "현재에 집중하는 연습을 해보세요."],
    "외로움": ["외로움은 누구에게나 찾아오는 감정이에요.", "지금 이 글을 읽는 동안만큼은 당신이 혼자가 아니에요."],
    "인간관계": ["모든 사람과 잘 지낼 필요는 없어요.", "솔직한 대화가 관계를 더욱 깊게 만듭니다."]
}

# 세션 상태 초기화
if "page" not in st.session_state:
    st.session_state.page = "select"

# 고민 선택 페이지
if st.session_state.page == "select":
    st.title("🎰 고민자판기")
    st.write("고민 종류를 선택한 후, 버튼을 눌러 상담 메시지를 받아보세요.")

    selected = st.radio("고민 종류를 선택하세요", concern_categories)

    if st.button("👉 다음"):
        st.session_state.selected_concern = selected
        st.session_state.page = "result"
        st.rerun()

# 상담 메시지 페이지
elif st.session_state.page == "result":
    concern = st.session_state.selected_concern
    st.title("🧾 상담 메시지")
    st.markdown(f"**고민 종류**: {concern}")
    message = random.choice(responses[concern])
    st.success(message)

    if st.button("🔁 처음으로"):
        st.session_state.page = "select"
        st.rerun()
