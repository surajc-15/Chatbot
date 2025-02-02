# import streamlit as st
# import os
# import uuid
# from groq import Groq
# from dotenv import load_dotenv
# from datetime import datetime

# # Load environment variables
# load_dotenv()

# # Retrieve API key
# api_key = os.getenv("GROQ_API_KEY")
# if not api_key:
#     st.error("GROQ_API_KEY is not set in environment variables. Please check your .env file.")
#     st.stop()

# # Initialize Groq API client
# client = Groq(api_key=api_key)

# # Initialize session state
# if "session_id" not in st.session_state:
#     st.session_state.session_id = str(uuid.uuid4())

# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# # Set layout
# st.set_page_config(page_title="AI Chatbot", page_icon="💬", layout="wide")

# # Sidebar - Chat History & Summary Button
# with st.sidebar:
#     st.title("📝 Chat History")

#     if st.session_state.chat_history:
#         for i, chat in enumerate(reversed(st.session_state.chat_history)):
#             if st.button(f"Chat {len(st.session_state.chat_history) - i}"):
#                 st.session_state.selected_chat = chat
#     else:
#         st.write("No chat history yet.")

#     # Clear Chat Button
#     if st.button("🗑️ Clear Chat"):
#         st.session_state.chat_history = []

#     # Summarize All Chats Button
#     if st.button("📌 Summarize Session"):
#         if st.session_state.chat_history:
#             all_chats_text = "\n".join(
#                 [f"User: {chat['user']}\nBot: {' '.join(chat['bot'])}" for chat in st.session_state.chat_history]
#             )
            
#             try:
#                 summary_response = client.chat.completions.create(
#                     messages=[
#                         {"role": "user", "content": f"Summarize this chat session:\n{all_chats_text}"}
#                     ],
#                     model="llama-3.3-70b-versatile",
#                 )

#                 if summary_response and summary_response.choices:
#                     st.session_state.session_summary = summary_response.choices[0].message.content
#                     st.success("Session summary generated!")

#             except Exception as e:
#                 st.error(f"An error occurred while summarizing: {e}")

# # Main Chat Window
# st.title("💬 AI Chatbot")
# st.write(f"Session ID: `{st.session_state.session_id}` (Active until refresh)")

# # Display Session Summary
# if "session_summary" in st.session_state and st.session_state.session_summary:
#     st.subheader("📌 Session Summary")
#     st.write(st.session_state.session_summary)

# # Display selected chat if exists
# if "selected_chat" in st.session_state and st.session_state.selected_chat:
#     chat = st.session_state.selected_chat
#     st.subheader("Previous Conversation")
#     st.write(f"**You:** {chat['user']}")
#     st.write("**Bot:**")
#     for line in chat['bot']:
#         st.markdown(f"- {line}")

# # Chat UI
# st.markdown("---")
# st.write("### 💬 Chat with AI")

# # Chat Message Container
# chat_container = st.container()

# # Display chat messages in a nice format
# for chat in st.session_state.chat_history:
#     with chat_container:
#         st.write(f"**🧑 You:** {chat['user']}")
#         st.write("**🤖 AI:**")
#         for line in chat['bot']:
#             st.markdown(f"- {line}")  # Proper bullet point formatting

# # Chat Input with Enter to Send & Loading Spinner
# def process_input():
#     user_input = st.session_state.chat_input.strip()
    
#     if user_input:
#         with st.spinner("🤖 Analyzing... Please wait..."):  # Show loading indicator
#             try:
#                 chat_completion = client.chat.completions.create(
#                     messages=[
#                         {"role": "user", "content": f"You are a helpful assistant. {user_input} Give a short, bullet-pointed response."}
#                     ],
#                     model="llama-3.3-70b-versatile",
#                 )

#                 current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#                 if chat_completion and chat_completion.choices:
#                     response_content = chat_completion.choices[0].message.content
#                     response_list = [line.strip() for line in response_content.split("\n") if line.strip()]

#                     new_chat = {"date": current_date, "user": user_input, "bot": response_list}
#                     st.session_state.chat_history.append(new_chat)
#                     st.session_state.selected_chat = new_chat

#                     st.session_state.chat_input = ""  # Clear input after sending

#             except Exception as e:
#                 st.error(f"An error occurred: {e}")

# # Chat Input
# user_input = st.text_input(
#     "Type a message...",
#     key="chat_input",
#     placeholder="Ask me anything...",
#     on_change=process_input  # Calls the function when Enter is pressed
# )


import streamlit as st
import os
import uuid
from groq import Groq
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# Retrieve API key
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("GROQ_API_KEY is not set in environment variables. Please check your .env file.")
    st.stop()

# Initialize Groq API client
client = Groq(api_key=api_key)

# Initialize session state
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Set layout
st.set_page_config(page_title="AI Chatbot", page_icon="💬", layout="wide")

# Sidebar - Chat History & Summary Button
with st.sidebar:
    st.title("📝 Chat History")

    if st.session_state.chat_history:
        for i, chat in enumerate(reversed(st.session_state.chat_history)):
            if st.button(f"Chat {len(st.session_state.chat_history) - i}"):
                st.session_state.selected_chat = chat
    else:
        st.write("No chat history yet.")

    # Clear Chat Button
    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []

    # Summarize All Chats Button
    if st.button("📌 Summarize Session"):
        if st.session_state.chat_history:
            all_chats_text = "\n".join(
                [f"User: {chat['user']}\nBot: {' '.join(chat['bot'])}" for chat in st.session_state.chat_history]
            )
            
            try:
                summary_response = client.chat.completions.create(
                    messages=[
                        {"role": "user", "content": f"Summarize this chat session:\n{all_chats_text}"}
                    ],
                    model="llama-3.3-70b-versatile",
                )

                if summary_response and summary_response.choices:
                    st.session_state.session_summary = summary_response.choices[0].message.content
                    st.success("Session summary generated!")

            except Exception as e:
                st.error(f"An error occurred while summarizing: {e}")

# Main Chat Window
st.title("💬 AI Chatbot")
st.write(f"Session ID: `{st.session_state.session_id}` (Active until refresh)")

# Display Session Summary
if "session_summary" in st.session_state and st.session_state.session_summary:
    st.subheader("📌 Session Summary")
    st.write(st.session_state.session_summary)

# Display selected chat if exists
if "selected_chat" in st.session_state and st.session_state.selected_chat:
    chat = st.session_state.selected_chat
    st.subheader("Previous Conversation")
    st.write(f"**You:** {chat['user']}")
    st.write("**Bot:**")
    for line in chat['bot']:
        st.markdown(f"- {line}")

# Chat UI
st.markdown("---")
st.write("### 💬 Chat with AI")

# Chat Message Container
chat_container = st.container()

# Display chat messages in a nice format (User's message right-aligned, Bot's left-aligned)
for chat in st.session_state.chat_history:
    with chat_container:
        # Display user's message aligned to the right
        st.markdown(f"<div style='text-align: right;'><b>You:</b> {chat['user']}</div>", unsafe_allow_html=True)
        # Display bot's message aligned to the left
        st.markdown(f"<div><b>Bot:</b> {'<br>'.join(chat['bot'])}</div>", unsafe_allow_html=True)

# Chat Input with Enter to Send & Loading Spinner
def process_input():
    user_input = st.session_state.chat_input.strip()
    
    if user_input:
        with st.spinner("🤖 Analyzing... Please wait..."):  # Show loading indicator
            try:
                chat_completion = client.chat.completions.create(
                    messages=[
                        {"role": "user", "content": f"You are a helpful assistant. {user_input} Give a short, bullet-pointed response."}
                    ],
                    model="llama-3.3-70b-versatile",
                )

                current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                if chat_completion and chat_completion.choices:
                    response_content = chat_completion.choices[0].message.content
                    response_list = [line.strip() for line in response_content.split("\n") if line.strip()]

                    new_chat = {"date": current_date, "user": user_input, "bot": response_list}
                    st.session_state.chat_history.append(new_chat)
                    st.session_state.selected_chat = new_chat

                    st.session_state.chat_input = ""  # Clear input after sending

            except Exception as e:
                st.error(f"An error occurred: {e}")

# Chat Input
user_input = st.text_input(
    "Type a message...",
    key="chat_input",
    placeholder="Ask me anything...",
    on_change=process_input  # Calls the function when Enter is pressed
)
