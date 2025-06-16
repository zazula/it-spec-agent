"""
Configuration for the IT Spec Agent.
If OpenAI's AssistantBuilder is available, use it; otherwise provide a stub.
"""
try:
    from openai import AssistantBuilder
except ImportError:
    class AssistantBuilder:
        def __init__(self, *, name, instructions, tools, model):
            self.name = name
            self.instructions = instructions
            self.tools = tools
            self.model = model
        def build(self):
            # Create a simple Agent stub
            class Agent:
                def __init__(self, tools):
                    self.tools = tools
                def run(self, prompt: str = "prompt"):
                    # Invoke each tool with the given prompt and return results
                    return {tool.__name__: tool(prompt) for tool in self.tools}
            return Agent(self.tools)

def setup_agent(tools):
    """Build and return the AI agent object."""
    return AssistantBuilder(
        name="IT Spec Agent",
        instructions="You are a systems analyst AI agent that helps generate IT system documentation from natural language.",
        tools=tools,
        model="gpt-4o"
    ).build()
