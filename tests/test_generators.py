import pytest

from tools.generators import (
    generate_functional_requirements,
    generate_technical_requirements,
    generate_architecture_design,
    generate_detailed_design,
    generate_task_breakdown,
)

@pytest.mark.parametrize(
    "func, prompt, expected_prefix",
    [
        (generate_functional_requirements, "Login module", "Functional requirements for: Login module"),
        (generate_technical_requirements, "Database schema", "Technical requirements for: Database schema"),
        (generate_architecture_design, "Microservices", "Architecture design for: Microservices"),
        (generate_detailed_design, "API endpoints", "Detailed design for: API endpoints"),
        (generate_task_breakdown, "Deployment", "Task breakdown for: Deployment"),
    ]
)
def test_generator_functions(func, prompt, expected_prefix):
    # Each generator should return the expected formatted string
    result = func(prompt)
    assert isinstance(result, str)
    assert result == expected_prefix