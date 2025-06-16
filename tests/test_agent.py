import pytest

from agent.main import create_agent

@pytest.fixture
def agent():
    return create_agent()

def test_agent_has_run_method(agent):
    # Agent should have a callable run method
    assert hasattr(agent, 'run')
    assert callable(agent.run)

def test_agent_run_returns_dict(agent):
    # Running with a prompt returns a dict of tool results
    prompt = "TestPrompt"
    output = agent.run(prompt)
    assert isinstance(output, dict)
    # Expect one entry per generator tool
    expected_tools = {
        'generate_functional_requirements',
        'generate_technical_requirements',
        'generate_architecture_design',
        'generate_detailed_design',
        'generate_task_breakdown',
    }
    assert set(output.keys()) == expected_tools
    # Each value should be a string incorporating the prompt
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
    # Test that each tool returns the correctly formatted string
    output = agent.run(prompt)
    assert output[tool_name] == expected_substr