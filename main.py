import streamlit as st

# Custom CSS for pink background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: pink;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Session state for tracking button clicks
if "page" not in st.session_state:
    st.session_state.page = 0


# Function to show "I Love You" page
def show_love_page():
    st.title("I Love You! 💖")
    st.write("### You are loved! 😍💑")
    st.write("👩‍❤️‍👨👨‍❤️‍👨👩‍❤️‍👩")  # Couple emojis
# If page is 0, show propose form
if st.session_state.page == 0:
    st.title("💖💖💖 WILL YOU BE MY GF 💖💖💖")

    # Two buttons
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Yes 💖"):
            st.session_state.page = 1  # Change to new page

    with col2:
        if st.button("Of Course, Yes 💘"):
            st.session_state.page = 1  # Change to new page

# If page is 1, show the love page
if st.session_state.page == 1:
    show_love_page()
