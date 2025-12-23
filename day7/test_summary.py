from ai.llm_client import generate_summary

text = """
Artificial Intelligence is a branch of computer science that focuses on
building machines capable of learning from data, reasoning, and making decisions.
It is widely used in healthcare, finance, and automation.
"""

result = generate_summary(text)
print(result)
