"""
Module for demonstrating basic usage of GPT via API
"""

from openai_tools import openai_client
from env import AZURE_OPENAI_API_MODEL

import logging


def query_gpt(query):
    logging.info(f"Querying GPT for: {query}")
    res = openai_client.chat.completions.create(
        model=AZURE_OPENAI_API_MODEL, messages=[{"role": "user", "content": query}]
    )

    return res


def parse_gpt_response(res):
    parsed_res = res.choices[0].message.content
    logging.info(f"Response parsed: {parsed_res}")
    return parsed_res


def query_and_parse(query):
    res = query_gpt(query)
    return parse_gpt_response(res)


def demo():
    query = "What is 10 times 10"
    parsed_res = query_and_parse(query)
    print(f"Parsed response: {parsed_res}")


if __name__ == "__main__":
    demo()

