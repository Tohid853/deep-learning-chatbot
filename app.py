
import streamlit as st
from predict import chatbot_response

st.set_page_config(
    page_title="Deep Learning Chatbot",
    page_icon="🤖"
)

st.title("🤖 Deep Learning Chatbot")
st.caption("Powered by TensorFlow")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Display old messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:

    # Display user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Get chatbot response
    response = chatbot_response(user_input)

    # Save bot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    st.rerun()

