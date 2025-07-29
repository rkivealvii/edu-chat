import streamlit as st
import openai

# --- CONFIGURE OPENAI API ---
openai.api_key = "YOUR_OPENAI_API_KEY"  # <-- Replace with your key

# --- APP TITLE ---
st.set_page_config(page_title="EduChat", page_icon="🎓")
st.title("🎓 EduChat")
st.write("Your friendly school assistant! Ask me anything about school events, tests, or portions.")

# --- CHAT HISTORY ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- USER INPUT ---
user_input = st.text_input("👩‍👩‍👦 Parent:", placeholder="Type your question here...")

# --- BOT RESPONSE ---
if user_input:
    st.session_state.chat_history.append(f"👩‍👩‍👦 Parent: {user_input}")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are EduChat, a polite teacher assistant who helps parents with school-related questions."},
            {"role": "user", "content": user_input}
        ]
    )

    bot_reply = response["choices"][0]["message"]["content"]
    st.session_state.chat_history.append(f"🎓 EduChat: {bot_reply}")

# --- DISPLAY CHAT ---
for chat in st.session_state.chat_history:
    st.write(chat)
