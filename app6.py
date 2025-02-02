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
#             start_time = chat["date"]
#             user_input_snippet = chat["user"][:20]  # Show first 20 characters as the label
#             if st.button(f"Chat started at {start_time}\n...{user_input_snippet}"):
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
#                         {"role": "user", "content": f"Summarize this chat session with key points:\n{all_chats_text}"}
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
#     summary = st.session_state.session_summary
#     # Highlight keywords in the summary
#     highlighted_summary = summary.replace("key points", "**key points**").replace("summary", "**summary**")
#     st.markdown(highlighted_summary)

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

# # Custom CSS to increase font size and add background color
# st.markdown("""
#     <style>
#         .user-message {
#             background-color: #DCF8C6; /* Light Green */
#             border-radius: 8px;
#             padding: 10px;
#             font-size: 18px;
#             width: fit-content;
#             margin: 10px 0;
#             margin-left: auto;
#             color: black;
#         }
#         .bot-message {
#             background-color: lightblue; /* Light Gray */
#             border-radius: 8px;
#             padding: 10px;
#             font-size: 18px;
#             width: fit-content;
#             margin: 10px 0;
#             margin-right: auto;
#             color: black;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Chat Message Container
# chat_container = st.container()

# # Display chat messages with timestamp (User's message right-aligned, Bot's left-aligned)
# for chat in st.session_state.chat_history:
#     with chat_container:
#         # Display user's message with timestamp and background, aligned right
#         st.markdown(f"<div class='user-message'><b>You ({chat['date']}):</b> {chat['user']}</div>", unsafe_allow_html=True)
#         # Display bot's message with timestamp and background, aligned left
#         st.markdown(f"<div class='bot-message'><b>Bot ({chat['date']}):</b> {'<br>'.join(chat['bot'])}</div>", unsafe_allow_html=True)

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

if "session_history" not in st.session_state:
    st.session_state.session_history = {}

# Set layout
st.set_page_config(page_title="AI Chatbot", page_icon="💬", layout="wide")

# Sidebar - Chat History & Summary Button
with st.sidebar:
    st.title("📝 Chat History")

    # Display history of different chat sessions
    for session_key, session_data in st.session_state.session_history.items():
        session_label = f"Chat Session {session_key}"
        if st.button(session_label):
            st.session_state.chat_history = session_data['history']
            st.session_state.selected_session = session_key
            st.session_state.session_summary = session_data.get('summary', None)

    # New Chat Button (clears the current chat history and starts a new one)
    if st.button("🆕 New Chat"):
        new_session_id = str(uuid.uuid4())
        st.session_state.chat_history = []
        st.session_state.session_id = new_session_id
        st.session_state.selected_session = None
        st.session_state.session_summary = None

    # Clear All Chats Button
    if st.button("🗑️ Clear All Chats"):
        st.session_state.session_history = {}

    # Summarize All Chats Button
    if st.button("📌 Summarize Session"):
        if st.session_state.chat_history:
            all_chats_text = "\n".join(
                [f"User: {chat['user']}\nBot: {' '.join(chat['bot'])}" for chat in st.session_state.chat_history]
            )
            
            try:
                summary_response = client.chat.completions.create(
                    messages=[
                        {"role": "user", "content": f"Summarize this chat session with key points:\n{all_chats_text}"}
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
    summary = st.session_state.session_summary
    # Highlight keywords in the summary
    highlighted_summary = summary.replace("key points", "**key points**").replace("summary", "**summary**")
    st.markdown(highlighted_summary)

# Display selected chat if exists
if "selected_session" in st.session_state and st.session_state.selected_session:
    selected_session = st.session_state.selected_session
    if selected_session in st.session_state.session_history:
        chat_history = st.session_state.session_history[selected_session]['history']
        st.subheader("Previous Conversation")
        for chat in chat_history:
            st.write(f"**You:** {chat['user']}")
            st.write(f"**Bot:** {' '.join(chat['bot'])}")

# Chat UI
st.markdown("---")
st.write("### 💬 Chat with AI")

# Custom CSS to increase font size and add background color
st.markdown("""
    <style>
        .user-message {
            background-color: #DCF8C6; /* Light Green */
            border-radius: 8px;
            padding: 10px;
            font-size: 18px;
            width: fit-content;
            margin: 10px 0;
            margin-left: auto;
            color: black;
        }
        .bot-message {
            background-color: lightblue; /* Light Gray */
            border-radius: 8px;
            padding: 10px;
            font-size: 18px;
            width: fit-content;
            margin: 10px 0;
            margin-right: auto;
            color: black;
        }
    </style>
""", unsafe_allow_html=True)

# Chat Message Container
chat_container = st.container()

# Display chat messages with custom CSS (User's message right-aligned, Bot's left-aligned)
for chat in st.session_state.chat_history:
    with chat_container:
        # Display user's message with a background and aligned right
        st.markdown(f"<div class='user-message'><b>You:</b> {chat['user']}</div>", unsafe_allow_html=True)
        # Display bot's message with a background and aligned left
        st.markdown(f"<div class='bot-message'><b>Bot:</b> {'<br>'.join(chat['bot'])}</div>", unsafe_allow_html=True)

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

                    # Store the chat history in the session's history
                    if st.session_state.session_id not in st.session_state.session_history:
                        st.session_state.session_history[st.session_state.session_id] = {'history': [], 'summary': None}
                    st.session_state.session_history[st.session_state.session_id]['history'].append(new_chat)

                    st.session_state.selected_session = st.session_state.session_id  # Set active session
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

