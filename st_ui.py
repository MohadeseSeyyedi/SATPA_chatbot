import streamlit as st

# Page config
st.set_page_config(page_title="Chat Page", page_icon="💬", layout="wide")
st.title("💬 Simple Chat with Streamlit Chat API")

# Initialize messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display all previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["user"]):
        st.markdown(msg["text"])

# Chat input (submission handled by return value)
user_input = st.chat_input("Type your message here:")

if user_input:
    # Add user message
    st.session_state.messages.append({"user": "user", "text": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Dummy bot response
    bot_reply = f"Bot received: {user_input}"
    st.session_state.messages.append({"user": "assistant", "text": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)