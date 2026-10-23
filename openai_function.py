# from openai import OpenAI

# import os
# from dotenv import load_dotenv
# load_dotenv()

# openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def generate_text_basic(prompt: str, model = "gpt-5.6-luna", system_prompt: str = "You are a helpfull ai assistant"):
#     response = openai_client.chat.completions.create(
#         model=model,
#         messages=[
#             {"role": "system", "content": system_prompt},
#             {"role": "user", "content": prompt}
#             ]
#         )
#     return response.choices[0].message.content




# import os
# from dotenv import load_dotenv
# from google import genai

# load_dotenv()

# gemini_client = genai.Client(
#     api_key=os.getenv("GEMINI_API_KEY")
# )


# def generate_text_basic(
#     prompt: str,
#     model: str = "gemini-3.8-flash",
#     system_prompt: str = "You are a helpful AI assistant"
# ):
#     response = gemini_client.models.generate_content(
#         model=model,
#         contents=prompt,
#         config={"system_instruction": system_prompt}
#     )

#     return response.text



import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

groq_client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_text_basic(
    prompt: str,
    model: str = "openai/gpt-oss-120b",
    system_prompt: str = "You are a helpful AI assistant"
):
    response = groq_client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_completion_tokens=200
    )

    return response.choices[0].message.content

def generate_text_with_conversation(messages,model = "openai/gpt-oss-120b"):
    response = groq_client.chat.completions.create(
        model=model,
        messages=messages
        )
    return response.choices[0].message.content