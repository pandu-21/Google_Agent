from dotenv import load_dotenv
load_dotenv()
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
llm=ChatGroq(model="openai/gpt-oss-20b")
search=GoogleSerperAPIWrapper()
agent=create_agent(llm, tools=[search.run], 
system_prompt="you are agent and you can search for any question on google",
checkpointer=MemorySaver())

while True:
    query=input("User:")
    if query.lower() in ["exit","quit"]:
        print("Exiting...")
        break
    res=agent.invoke({"messages":[{"role":"user","content":query}]},
    {"configurable":{"thread_id":"1"}})
    print("AI:",res["messages"][-1].content)