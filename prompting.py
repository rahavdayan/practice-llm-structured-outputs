import os
from typing import Optional
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Step(BaseModel):
    explanation: str
    output: str

class MathResponse(BaseModel):
    steps: list[Step]
    final_answer: str

class ValidationResponse(BaseModel):
    is_math_question: bool
    reason: str

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def is_appropriate_math_question(query: str) -> ValidationResponse:
    """
    Validates if the user query is an appropriate math question with a specific answer.
    """
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a math tutor validator. Determine if the user's query is an appropriate math question that has a specific, calculable answer. Math questions include algebra, calculus, geometry, arithmetic, etc. Exclude vague questions like 'help me with math' or non-math questions. Respond with JSON format: {\"is_math_question\": boolean, \"reason\": string}"
                },
                {
                    "role": "user",
                    "content": f"Is this an appropriate math question with a specific answer? Query: {query}"
                }
            ],
            response_format={"type": "json_object"}
        )
        import json
        result = json.loads(completion.choices[0].message.content)
        return ValidationResponse(**result)
    except Exception as e:
        return ValidationResponse(
            is_math_question=False,
            reason=f"Error validating question: {str(e)}"
        )

def solve_math_problem(query: str) -> Optional[MathResponse]:
    """
    Solves a math problem and returns structured step-by-step solution.
    First validates if it's an appropriate math question.
    """
    # First validate the question
    validation = is_appropriate_math_question(query)
    
    if not validation.is_math_question:
        return None
    
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert math tutor. Solve the given math problem step by step. For each step, provide a clear explanation of your reasoning and show the mathematical output after applying that step. Be precise and show all work. Respond with JSON format: {\"steps\": [{\"explanation\": string, \"output\": string}], \"final_answer\": string}"
                },
                {
                    "role": "user",
                    "content": f"Solve this math problem step by step: {query}"
                }
            ],
            response_format={"type": "json_object"}
        )
        import json
        result = json.loads(completion.choices[0].message.content)
        return MathResponse(**result)
    except Exception as e:
        # Return error as a single step
        return MathResponse(
            steps=[
                Step(
                    explanation=f"Error occurred while solving: {str(e)}",
                    output="Unable to solve due to error"
                )
            ],
            final_answer="Error: Could not solve problem"
        )

# Test function - uncomment to test
# print(solve_math_problem("can you solve the equation 4x + 16 = 20"))