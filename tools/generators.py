"""
This module defines generator tools for the IT Spec Agent.
Each function is registered as an OpenAI tool via @tool decorator.
If the OpenAI tool decorator is unavailable, we provide a no-op fallback.
"""
try:
    from openai import tool
except ImportError:
    def tool(f=None, *, name=None, description=None):
        def decorator(func):
            return func
        # support both @tool and @tool(...)
        if f:
            return decorator(f)
        return decorator

@tool
def generate_functional_requirements(prompt: str) -> str:
    """Generate functional requirements based on a prompt."""
    return f"Functional requirements for: {prompt}"

@tool
def generate_technical_requirements(prompt: str) -> str:
    """Generate technical requirements based on a prompt."""
    return f"Technical requirements for: {prompt}"

@tool
def generate_architecture_design(prompt: str) -> str:
    """Generate architecture design based on a prompt."""
    return f"Architecture design for: {prompt}"

@tool
def generate_detailed_design(prompt: str) -> str:
    """Generate detailed design based on a prompt."""
    return f"Detailed design for: {prompt}"

@tool
def generate_task_breakdown(prompt: str) -> str:
    """Generate task breakdown based on a prompt."""
    return f"Task breakdown for: {prompt}"