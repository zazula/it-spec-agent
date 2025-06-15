from openai import AssistantBuilder

def setup_agent(tools):
    return AssistantBuilder(
        name="IT Spec Agent",
        instructions="You are a systems analyst AI agent that helps generate IT system documentation from natural language.",
        tools=tools,
        model="gpt-4o"
    ).build()
