import streamlit as st
import openai
import GlobalConstants

from vectorstores import VectorDB

st.set_page_config(page_title="AI Assistant Builder", page_icon="🤖", layout="centered", initial_sidebar_state="auto", menu_items=None)
openai.api_key = GlobalConstants.OPENAI_KEY
st.title(f"Chat with an AI {GlobalConstants.ASSISTANT} 🤖")
st.info("Check out more information on our [Github Repository](https://github.com/hasnain3142/AI-Assistant-Builder)", icon="📃")
         
if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": f"Ask me a question about {GlobalConstants.CATEGORY}..."}
    ]

@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Loading and indexing the Data hang tight! This should take 1-2 minutes."):
        db = VectorDB()
        db.create_index(collection_name=GlobalConstants.CATEGORY)
        print(f"Index created for {GlobalConstants.CATEGORY}!")
        return db.index

index = load_data()

if "chat_engine" not in st.session_state.keys(): # Initialize the chat engine
        st.session_state.chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) # Add response to message history