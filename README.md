# Math Tutor Chatbot 🧮

A Streamlit-based chatbot application that demonstrates using **Pydantic for structured LLM outputs**. This project shows how to force language models to return well-structured, type-safe responses for math problem solving.

## 🎯 Learning Objective

This project is an **exercise in using Pydantic to enforce structured outputs from Large Language Models (LLMs)**. It demonstrates how to:

- Define structured data models using Pydantic
- Force LLMs to return JSON responses that conform to specific schemas
- Parse and validate LLM outputs with type safety
- Handle errors gracefully when LLM responses don't match expected structure

## Features

- 💬 Interactive chat interface powered by GPT-4o-mini
- 🔢 Math problem validation and solving
- 📝 Structured step-by-step explanations using Pydantic models
- 🗂️ Chat history management
- 🎨 Clean and intuitive UI
- ✅ Type-safe LLM response handling

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd practice-llm-structured-outputs
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
```

3. Activate the virtual environment:
```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Set up your OpenAI API key:
```bash
# Copy the example environment file
copy .env.example .env

# Edit .env and add your OpenAI API key:
# OPENAI_API_KEY=sk-your-actual-api-key-here
```

### Running the Application

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically `http://localhost:8501`)

## Usage

1. Type your math question in the chat input at the bottom
2. Press Enter or click the send button
3. The chatbot will:
   - Validate if your query is an appropriate math question
   - If valid, solve it step-by-step using structured Pydantic models
   - Display formatted solutions with explanations and mathematical outputs
   - If invalid, provide helpful guidance on asking math questions

## Project Structure

```
practice-llm-structured-outputs/
├── app.py              # Main Streamlit application
├── prompting.py        # Pydantic models and OpenAI integration
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
├── README.md          # This file
└── .gitignore         # Git ignore rules
```

## 🔧 Pydantic Models

The project uses three main Pydantic models to structure LLM outputs:

### `Step`
```python
class Step(BaseModel):
    explanation: str  # Reasoning for this step
    output: str      # Mathematical result after this step
```

### `MathResponse`
```python
class MathResponse(BaseModel):
    steps: list[Step]     # List of solution steps
    final_answer: str     # Final solution
```

### `ValidationResponse`
```python
class ValidationResponse(BaseModel):
    is_math_question: bool  # Whether query is valid math
    reason: str            # Explanation of validation result
```

## 🚀 Key Learning Points

1. **Structured Output Enforcement**: Using `response_format={"type": "json_object"}` with detailed JSON schema instructions
2. **Type Safety**: Pydantic automatically validates and converts LLM JSON responses to typed Python objects
3. **Error Handling**: Graceful fallbacks when LLM responses don't match expected structure
4. **Validation Logic**: Two-step process (validate question → solve problem) using structured responses

## Future Enhancements

- [ ] Add support for mathematical notation rendering (LaTeX)
- [ ] Implement problem categorization (algebra, calculus, geometry)
- [ ] Add export functionality for solutions
- [ ] Include interactive math visualizations
- [ ] Support for multi-step problem chains

## Contributing

This project serves as a learning example for Pydantic + LLM integration. Feel free to:
- Extend the Pydantic models for more complex math problems
- Add additional validation layers
- Experiment with different LLM prompting strategies
- Improve error handling and edge cases

## License

This project is open source and available under the [MIT License](LICENSE).
