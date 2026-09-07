import os
import asyncio
from dotenv import load_dotenv
from openai import OpenAI, AsyncOpenAI

from app.database import prompts_collection, history_collection

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

client = OpenAI(api_key=OPENAI_API_KEY)
async_client = AsyncOpenAI(api_key=OPENAI_API_KEY)


def get_prompt():
    prompt = prompts_collection.find_one(
        {"_id": "Education_Prompt"}
    )

    if not prompt:
        # Create the required prompt automatically
        prompt = {
            "_id": "Education_Prompt",
            "template": (
                "You are an expert in education domain. "
                "Answer the following: {{userInput}}"
            )
        }

        prompts_collection.insert_one(prompt)

    return prompt["template"]


def create_prompt(user_input):
    template = get_prompt()

    return template.replace(
        "{{userInput}}",
        user_input
    )


def call_openai(prompt):
    if os.getenv("MOCK_MODE", "false").lower() == "true":
        return f"Demo response for: {prompt}"

    response = client.responses.create(
        model=OPENAI_MODEL,
        input=prompt
    )

    return response.output_text


def save_history(user_input, response):
    history_collection.insert_one({
        "userInput": user_input,
        "response": response
    })


def process_request(user_input):
    prompt = create_prompt(user_input)

    response = call_openai(prompt)

    save_history(user_input, response)

    return response


async def call_openai_async(prompt):
    if os.getenv("MOCK_MODE", "false").lower() == "true":
        await asyncio.sleep(0.1)
        return f"Demo response for: {prompt}"

    response = await async_client.responses.create(
        model=OPENAI_MODEL,
        input=prompt
    )

    return response.output_text


async def process_multiple_requests(user_inputs):

    prompts = [
        create_prompt(user_input)
        for user_input in user_inputs
    ]

    tasks = [
        call_openai_async(prompt)
        for prompt in prompts
    ]

    responses = await asyncio.gather(*tasks)

    for user_input, response in zip(user_inputs, responses):
        save_history(user_input, response)

    return responses