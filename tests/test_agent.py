import pytest
from unittest.mock import MagicMock
from agent.main import create_agent

# --- Fixture to auto-mock OpenAI completions ---
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

@pytest.fixture
def agent():
    return create_agent()

def test_agent_has_run_method(agent):
    assert hasattr(agent, 'run')
    assert callable(agent.run)

def test_agent_run_returns_dict(agent):
    prompt = "TestPrompt"
    output = agent.run(prompt)
    assert isinstance(output, dict)
    expected_tools = {
        'generate_functional_requirements',
        'generate_technical_requirements',
        'generate_architecture_design',
        'generate_detailed_design',
        'generate_task_breakdown',
    }
    assert set(output.keys()) == expected_tools
    for key, value in output.items():
        assert isinstance(value, str)
        assert prompt in value

@pytest.mark.parametrize(
    "tool_name, prompt, expected_substr",
    [
        ('generate_functional_requirements', 'Login', 'Functional requirements for: Login'),
        ('generate_technical_requirements', 'DB', 'Technical requirements for: DB'),
        ('generate_architecture_design', 'Svc', 'Architecture design for: Svc'),
        ('generate_detailed_design', 'API', 'Detailed design for: API'),
        ('generate_task_breakdown', 'Deploy', 'Task breakdown for: Deploy'),
    ]
)
def test_individual_tool_output(agent, tool_name, prompt, expected_substr):
    output = agent.run(prompt)
    assert output[tool_name] == expected_substr
