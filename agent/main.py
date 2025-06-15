from agent.config import setup_agent
from tools.generators import (
    generate_functional_requirements,
    generate_technical_requirements,
    generate_architecture_design,
    generate_detailed_design,
    generate_task_breakdown
)

def create_agent():
    return setup_agent([
        generate_functional_requirements,
        generate_technical_requirements,
        generate_architecture_design,
        generate_detailed_design,
        generate_task_breakdown,
    ])
