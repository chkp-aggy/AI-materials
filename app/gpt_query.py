"""
Module for demonstrating basic usage of GPT via API
"""

import logging

from openai.types.chat.chat_completion import ChatCompletion  # Just for typing

from openai_tools import openai_client
from env import AZURE_OPENAI_API_MODEL


def query_gpt(query: str, model=AZURE_OPENAI_API_MODEL) -> ChatCompletion:
    """Send a query to OpenAI and return the response"""
    logging.info(f"Querying GPT for: {query}")
    res = openai_client.chat.completions.create(
        model=model, messages=[{"role": "user", "content": query}]
    )
    return res


def parse_gpt_response(res: ChatCompletion) -> str:
    """Parse a ChatCompletion response from OpenAI"""
    parsed_res = res.choices[0].message.content
    logging.info(f"Response parsed: {parsed_res}")
    return parsed_res


def query_and_parse(query: str) -> str:
    """Query GPT and parse the response"""
    res = query_gpt(query)
    return parse_gpt_response(res)


def demo() -> None:
    """Demonstrate invocation of `query_and_parse`"""
    query = "What is 10 times 10"
    parsed_res = query_and_parse(query)
    print(f"Parsed response: {parsed_res}")


if __name__ == "__main__":
    demo()
