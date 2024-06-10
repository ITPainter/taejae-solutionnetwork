import streamlit as st

# Utterances 스크립트 코드
utterances_code = """
<div id="utterances"></div>
<script src="https://utteranc.es/client.js"
        repo="yochoiDavid/taejae-solutionnetwork"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
"""

st.title("Utterances Comments")
st.markdown(
    """
    This is a simple Streamlit app that includes Utterances for comments.
    """, unsafe_allow_html=True)

# Utterances 코드 삽입
st.markdown(utterances_code, unsafe_allow_html=True)
