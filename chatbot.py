import streamlit as st
import ollama
from datetime import datetime

st.title("Llama 2 Chatbot")
st.write("Welcome! I'm here to assist you with your questions and tasks.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "personality" not in st.session_state:
    st.session_state.personality = "Friendly"

if "user_input" not in st.session_state:
    st.session_state.user_input = ""


with st.sidebar:
    st.header("Settings")
    personality_options = ["Friendly", "Professional", "Humorous"]
    st.selectbox("Select personality:", options=personality_options, key="personality")
    clear = st.button("Clear Chat History")

def get_llama_response(message):
    try:
        response = ollama.chat(model="llama2", messages=[
            {"role": "user", "content": f"[{st.session_state.personality}] {message}"}
        ])
        return response['message']['content'] if 'message' in response else "Error: No response from LLaMA."
    except Exception as e:
        return f"Error: {e}"

user_input = st.text_input("You:", placeholder="Type your message here...", key="usr_inp")

if user_input:
    with st.spinner("LLaMA is typing..."):
        timestamp = datetime.now().strftime("%H:%M")
        st.session_state.chat_history.insert(0, {"user": user_input, "time":timestamp})
        response = get_llama_response(user_input)
        st.session_state.chat_history.insert(1, {"llama": response, "time":timestamp})
        user_input = ""

for chat in st.session_state.chat_history:
    if "user" in chat:
        st.write(f"**You [{chat['time']}]:** {chat['user']}")
    elif "llama" in chat:
        st.write(f"**LLaMA {chat['time']}:** {chat['llama']}")

if clear:
    st.session_state.chat_history.clear()
    st.success("Chat history cleared!")
