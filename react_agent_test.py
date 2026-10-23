from openai_function import generate_text_basic

from prompts import react_system_prompt

prompt = f"""
Should i take an umbrella while going out today in California?
"""


response = generate_text_basic(prompt,system_prompt=react_system_prompt)

print(response)