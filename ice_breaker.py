from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

information = """
Elon Reeve Musk is a businessman and investor known for his key roles in space company SpaceX and automotive company Tesla, Inc. Other involvements include ownership of X Corp., formerly Twitter, and his role in the founding of The Boring Company, xAI, Neuralink and OpenAI."""
summary_template = """
geiven the information {information} about a person from i want you to create:
1. a short summary
2. two interesting facts about them
"""

summary_prompt_template = PromptTemplate(
    input_value=["information"], template=summary_template
)
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
chain = summary_prompt_template | llm
res = chain.invoke(input={"information": information})

print(res)
