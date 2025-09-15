import streamlit as st
from prompting import solve_math_problem

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
        # Get structured math solution
        math_result = solve_math_problem(prompt)
        
        if math_result is None:
            response = "I can only help with specific math problems that have calculable answers. Please ask a math question like 'solve 2x + 5 = 15' or 'find the derivative of x²'."
        else:
            # Format the structured response
            response = "## Step-by-Step Solution\n\n"
            
            for i, step in enumerate(math_result.steps, 1):
                response += f"**Step {i}:** {step.explanation}\n\n"
                response += f"```\n{step.output}\n```\n\n"
            
            response += f"## Final Answer\n\n**{math_result.final_answer}**"
        
        st.markdown(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar with app info
with st.sidebar:
    st.header("About")
    st.markdown("""
    This is a math tutor chatbot that helps you solve math problems step by step.
    
    **Features:**
    - Interactive chat interface powered by GPT-4o-mini
    - Step-by-step problem solving with detailed explanations
    - Support for algebra, calculus, geometry, and arithmetic
    - Validates math questions automatically
    
    **How to use:**
    1. Type your math question in the chat input
    2. Press Enter or click send
    3. Get detailed step-by-step solutions
    """)
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
