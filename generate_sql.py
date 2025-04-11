from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider


class ResponseModel(BaseModel):
    query: str

PROMPT = """
    Convert the user's question into a SQL query using the following schema:

    Tables:
    - members(member_id, full_name, national_id, house_number, membership_status)
    - villages(village_id, village_name, sub_district, district, province)
    - savings(saving_id, member_id, deposit_amount, deposit_date, account_type)
    - loans(loan_id, member_id, loan_amount, interest_rate, status)
    - projects(project_id, project_name, budget, responsible_parties, progress_percentage, impact_summary)
    """
    
vllm_model = OpenAIModel(
    model_name="deepseek-ai/deepseek-coder-1.3b-base",  
    provider=OpenAIProvider(base_url="http://localhost:8000/v1"),  
)

agent = Agent(
    model=vllm_model,
    result_type=ResponseModel,
    system_prompt=PROMPT,
)

if __name__ == "__main__":
    result = agent.run_sync("List all members who have a loan amount greater than 30000 THB")
    print(result.data.model_dump())

