from openai_function import generate_text_basic

from sample_func import get_weather

curr_weather = get_weather("California")

prompt = f"""
Should i take an umbrella while going out today in 
California based on following weather condition: {curr_weather}?
"""

response = generate_text_basic(prompt)

print(response)
