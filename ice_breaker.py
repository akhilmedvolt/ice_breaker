from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from third_parties.linkedin import scrape_linkedin_profile
from langchain.chains import LLMChain

load_dotenv()

if __name__ == "__main__":
    summary_template = """
    geiven the information {information} about a person from i want you to create:
    1. a short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_value=["information"], template=summary_template
    )
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    linkedin_data = scrape_linkedin_profile()
    chain = summary_prompt_template | llm
    # chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    res = chain.invoke(input={"information": linkedin_data})

    print(res)
