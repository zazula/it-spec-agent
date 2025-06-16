PROMPT = """
You are a technical project manager. Break the following Detailed Technical Design into executable engineering tasks. Output a task list as:

- [ ] Task Name (Component)
  - Description
  - Dependencies (if any)
  - Estimated Effort (Low/Med/High)

Group tasks by component or sprint. Output in Markdown.
"""