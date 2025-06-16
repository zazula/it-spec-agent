import pytest
from unittest.mock import MagicMock
from tools.generators import (
    generate_functional_requirements,
    generate_technical_requirements,
    generate_architecture_design,
    generate_detailed_design,
    generate_task_breakdown,
)

@pytest.fixture(autouse=True)
def mock_openai_chat(monkeypatch):
    class DummyChoice:
        def __init__(self, content):
            self.message = MagicMock(content=content)
    class DummyResult:
        def __init__(self, content):
            self.choices = [DummyChoice(content)]
    def fake_create(model, messages, temperature):
        role_to_prefix = {
            'You are a systems analyst': 'Functional requirements for: ',
            'You are a technical analyst': 'Technical requirements for: ',
            'You are a software architect': 'Architecture design for: ',
            'You are a senior engineer': 'Detailed design for: ',
            'You are a project manager': 'Task breakdown for: ',
        }
        sys_msg = messages[0]['content']
        user_msg = messages[1]['content']
        prefix = next((v for k, v in role_to_prefix.items() if sys_msg.startswith(k)), 'Result: ')
        return DummyResult(prefix + user_msg)
    monkeypatch.setattr(
        'openai.OpenAI',
        lambda *a, **k: type('MockClient', (), {"chat": type('Obj', (), {"completions": type('Obj', (), {"create": staticmethod(fake_create)})})})(),
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
    result = func(prompt)
    assert isinstance(result, str)
    assert result == expected_prefix
