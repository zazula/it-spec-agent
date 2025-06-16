
"""
This module defines generator tools for the IT Spec Agent.
Each function is registered as an OpenAI tool via @tool decorator using a phase-specific system prompt and user input.
"""

try:
    import openai
    from openai import tool
    _has_openai = True
except ImportError:
    _has_openai = False
    def tool(f=None, *, name=None, description=None):
        def decorator(func):
            return func
        if f:
            return decorator(f)
        return decorator

from agent.prompts.functional import PROMPT as FUNCTIONAL_PROMPT
from agent.prompts.technical import PROMPT as TECHNICAL_PROMPT
from agent.prompts.architecture import PROMPT as ARCHITECTURE_PROMPT
from agent.prompts.design import PROMPT as DESIGN_PROMPT
from agent.prompts.tasks import PROMPT as TASKS_PROMPT

def _raise_no_openai():
    raise ImportError("openai Python package is required to use these functions. Please install openai.")

def _chat_completion(system_prompt, user_prompt):
    if not _has_openai:
        _raise_no_openai()
    client = openai.OpenAI()
    result = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2
    )
    return result.choices[0].message.content

@tool
def generate_functional_requirements(prompt: str) -> str:
    """Generate functional requirements based on a prompt."""
    return _chat_completion(FUNCTIONAL_PROMPT, prompt)

@tool
def generate_technical_requirements(prompt: str) -> str:
    """Generate technical requirements based on a prompt."""
    return _chat_completion(TECHNICAL_PROMPT, prompt)

@tool
def generate_architecture_design(prompt: str) -> str:
    """Generate architecture design based on a prompt."""
    return _chat_completion(ARCHITECTURE_PROMPT, prompt)

@tool
def generate_detailed_design(prompt: str) -> str:
    """Generate detailed design based on a prompt."""
    return _chat_completion(DESIGN_PROMPT, prompt)

@tool
def generate_task_breakdown(prompt: str) -> str:
    """Generate task breakdown based on a prompt."""
    return _chat_completion(TASKS_PROMPT, prompt)