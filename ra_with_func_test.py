from openai_function import generate_text_basic
from sample_func import get_weather
from prompts import react_system_prompt
from json_helper import extract_json

available_actions = {
"get_weather": get_weather
}

prompt = f"""
Should i take an umbrella while going out today in California?
"""


response = generate_text_basic(prompt,system_prompt=react_system_prompt)

json_function = extract_json(response)

#print(response)

# print(type(json_function))
# print(json_function[0]['function_name'])

if json_function:
    function_name = json_function[0]['function_name']
    function_parms = json_function[0]['function_parms']
    if function_name not in available_actions:
        raise Exception(f"Unknown action: {function_name}: {function_parms}")
    print(f" -- running {function_name} {function_parms}")
    action_function = available_actions[function_name]
    #call the function
    result = action_function(**function_parms)
    function_result_message = f"Action_Response: {result}"
    print(function_result_message)