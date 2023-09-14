from config import SECRETS
# Import the required modules
from langchain.llms import Clarifai
from langchain import PromptTemplate, LLMChain

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

clarifai_llm = Clarifai( pat=SECRETS.get("PAT"), user_id=SECRETS.get("USER_ID"), app_id=SECRETS.get("APP_ID"), model_id=SECRETS.get("MODEL_ID"))


# Create LLM chain
llm_chain = LLMChain(prompt=prompt, llm=clarifai_llm)
question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

print(llm_chain.run(question))
