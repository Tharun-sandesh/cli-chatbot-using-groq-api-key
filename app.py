import streamlit as st
from config import get_groq_client

# Sets the browser tab title and icon
st.set_page_config(page_title="My AI Chatbot", page_icon="🤖")
st.title("🤖 My AI Chatbot")

# Get a ready-to-use connection to Groq (key handled inside config.py)
client = get_groq_client()

# st.session_state keeps data alive between interactions on the page.
# Without this, the chat history would vanish every time you send a message.
if "messages" not in st.session_state:
    st.session_state.messages = []

# Re-draw every past message on screen (so history stays visible)
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Shows a chat-style input box pinned at the bottom of the page
user_input = st.chat_input("Ask me anything...")

if user_input:
    # Save and display the user's message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Send it to the AI model
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": user_input}]
    )
    answer = response.choices[0].message.content

    # Save and display the AI's reply
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.write(answer)

# --- Footer with trademark / copyright ---
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        text-align: center;
        color: gray;
        font-size: 0.8rem;
        padding: 8px 0;
        background-color: rgba(255, 255, 255, 0.9);
    }
    </style>
    <div class="footer">
        © 2026 Tharun Sandesh. All rights reserved.
    </div>
    """,
    unsafe_allow_html=True
)