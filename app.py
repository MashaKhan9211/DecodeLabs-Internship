import streamlit as st
from datetime import datetime

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------
# CUSTOM CSS
# ---------------------------
st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.chat-header {
    text-align: center;
    padding: 10px;
    margin-bottom: 20px;
}

.chat-header h1 {
    color: #4CAF50;
}

.timestamp {
    font-size: 12px;
    color: gray;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# HEADER
# ---------------------------
st.markdown("""
<div class="chat-header">
    <h1>🤖 AI Assistant</h1>
    <p>Rule-Based AI Chatbot | DecodeLabs Internship Project 1</p>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# SIDEBAR
# ---------------------------
with st.sidebar:

    st.title("🤖 AI Assistant")

    st.markdown("---")

    st.subheader("About")
    st.write("""
This chatbot is built using:

- Python
- Streamlit
- Rule-Based AI Logic
- Session State
    """)

    st.markdown("---")

    st.subheader("Available Commands")

    st.code("""
hi
hello
hey
how are you
your name
time
date
help
bye
exit
""")

    st.markdown("---")

    if st.button("🗑 Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# ---------------------------
# SESSION STATE
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------
# CHATBOT FUNCTION
# ---------------------------
def get_bot_response(user_message):

    msg = user_message.lower().strip()

    if msg in ["hi", "hello", "hey"]:
        return "Hello! 👋 How can I help you today?"

    elif msg == "how are you":
        return "I'm doing great! Thanks for asking 😊"

    elif msg == "your name":
        return "I'm AI Assistant 🤖"

    elif msg == "time":
        return f"Current Time: {datetime.now().strftime('%I:%M:%S %p')}"

    elif msg == "date":
        return f"Today's Date: {datetime.now().strftime('%d-%m-%Y')}"

    elif msg == "help":
        return """
Available Commands:

• hi
• hello
• hey
• how are you
• your name
• time
• date
• help
• bye
• exit
"""

    elif msg in ["bye", "exit"]:
        return "Goodbye! 👋 Have a great day."

    else:
        return (
            "Sorry, I don't understand that command.\n\n"
            "Type **help** to see available commands."
        )

# ---------------------------
# DISPLAY OLD CHAT
# ---------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"], avatar=message["avatar"]):

        st.write(message["content"])

        st.caption(message["time"])

# ---------------------------
# CHAT INPUT
# ---------------------------
user_input = st.chat_input("Type your message here...")

if user_input:

    current_time = datetime.now().strftime("%I:%M %p")

    # USER MESSAGE
    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
        "avatar": "🧑",
        "time": current_time
    })

    # BOT RESPONSE
    response = get_bot_response(user_input)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response,
        "avatar": "🤖",
        "time": current_time
    })

    st.rerun()

# ---------------------------
# FOOTER
# ---------------------------
st.markdown("---")

st.caption(
    "Built with ❤️ using Streamlit | Artificial Intelligence Internship Project 1"
)