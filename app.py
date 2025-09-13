import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Math Tutor Chatbot",
    page_icon="🧮",
    layout="wide"
)

# App title
st.title("🧮 Math Tutor Chatbot")
st.markdown("Ask me any math question and I'll provide step-by-step solutions!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ask a math question..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        # Placeholder response - this is where LLM integration will go
        response = f"I received your math question: '{prompt}'\n\nThis is a placeholder response. In the full implementation, I would provide a step-by-step solution to your math problem using an LLM backend."
        st.markdown(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar with app info
with st.sidebar:
    st.header("About")
    st.markdown("""
    This is a math tutor chatbot that helps you solve math problems step by step.
    
    **Features:**
    - Interactive chat interface
    - Step-by-step problem solving
    - Support for various math topics
    
    **How to use:**
    1. Type your math question in the chat input
    2. Press Enter or click send
    3. Get detailed step-by-step solutions
    """)
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
