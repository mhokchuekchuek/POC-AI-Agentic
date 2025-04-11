import pytesseract
from PIL import Image
from pydantic import BaseModel, Field
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider


def extract_text_from_image(image_path: str) -> str:
    return pytesseract.image_to_string(Image.open(image_path), lang="eng+tha")

class LoanInfo(BaseModel):
    name: str = Field(description="Full name of the borrower")
    national_id: str = Field(description="National ID number")
    loan_amount: float = Field(description="Loan amount in THB")
    interest_rate: float = Field(description="Interest rate in percent")
    status: str = Field(description="Loan status, e.g., On-time, Overdue, Paid in Full")

PROMPT = """
You are an AI assistant that extracts structured loan information from messy OCR output text.

Please extract the following fields from the OCR text and return them in JSON:
- name
- national_id
- loan_amount (THB)
- interest_rate (%)
- status (e.g., On-time, Overdue, Paid in Full)
If any fields are missing, return null for that field.
"""

vllm_model = OpenAIModel(
    model_name="deepseek-ai/deepseek-coder-1.3b-base",
    provider=OpenAIProvider(base_url="http://localhost:8000/v1"),
)

agent = Agent(
    model=vllm_model,
    result_type=LoanInfo,
    system_prompt=PROMPT,
)

if __name__ == "__main__":

    ocr_text = extract_text_from_image("assets/sample_loan_form.jpg")


    result = agent.run_sync(ocr_text)

    print(result.data.model_dump())
