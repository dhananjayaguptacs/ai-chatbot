import streamlit as st
from langchain_community.llms import Ollama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Set Streamlit page configuration
st.set_page_config(layout="wide")
st.title("LangChain Chatbot with Gemma3:1b")

# Initialize LangChain components in session state
if 'conversation' not in st.session_state:
    llm = Ollama(model="gemma3:1b", temperature=0.7)
    st.session_state.conversation = ConversationChain(
        llm=llm,
        memory=ConversationBufferMemory(),
        verbose=False
    )
    # Add system prompt
    st.session_state.conversation.memory.save_context(
        {"input": "System: You are a helpful assistant powered by Gemma3:1b."},
        {"output": "Understood! I'm ready to assist."}
    )

# Display initial message
with st.chat_message("assistant"):
    st.write("Hello! I'm your LangChain-powered chatbot with Gemma3:1b. Ask me anything!")

# Chat input
prompt = st.chat_input("Ask a question")
if prompt:
    with st.spinner('Thinking...'):
        try:
            # Get response from LangChain conversation chain
            response = st.session_state.conversation.predict(input=prompt)
            # Display conversation history
            for message in st.session_state.conversation.memory.chat_memory.messages:
                role = "user" if message.type == "human" else "assistant"
                with st.chat_message(role):
                    st.write(message.content)
        except Exception as e:
            st.error(f"Error: {str(e)}")