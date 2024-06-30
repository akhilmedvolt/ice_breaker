from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from tools.tools import get_profile_url_tavily


def lookup(name: str):
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """
        given the full name {name_of_person}. I want you to get it me a link to their linkedin
        profile page. Your answer should contain only a URL
        """
    prompt_template = PromptTemplate(
        input_variables=["name_of_person"], template=template
    )
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 Linkedin profile page",
            func=get_profile_url_tavily,
            description="useful for when you need to get the linkedin Page URL",
        )
    ]
    print("Pulling ReACT from hub")
    react_prompt = hub.pull("hwchase17/react")
    print("Creating Agent")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)
    print("Invoking Agent")
    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linkedin_profile_url = result["output"]
    return linkedin_profile_url


if __name__ == "__main__":
    linkedin_url = lookup(name="Akhil Sanker")
    print(linkedin_url)
