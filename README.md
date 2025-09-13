# Math Tutor Chatbot 🧮

A simple Streamlit-based chatbot application designed to help students with math problems by providing step-by-step solutions.

## Features

- 💬 Interactive chat interface
- 🔢 Math problem solving assistance
- 📝 Step-by-step explanations (placeholder for now)
- 🗂️ Chat history management
- 🎨 Clean and intuitive UI

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

### Running the Application

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically `http://localhost:8501`)

## Usage

1. Type your math question in the chat input at the bottom
2. Press Enter or click the send button
3. The chatbot will respond with a step-by-step solution (currently shows placeholder responses)

## Project Structure

```
practice-llm-structured-outputs/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── .gitignore         # Git ignore rules
```

## Future Enhancements

- [ ] Integrate with an LLM API for actual math problem solving
- [ ] Add support for mathematical notation rendering
- [ ] Implement problem categorization
- [ ] Add export functionality for solutions
- [ ] Include interactive math visualizations

## Contributing

This is a basic scaffold for a math tutor chatbot. Feel free to extend and improve the functionality!

## License

This project is open source and available under the [MIT License](LICENSE).
