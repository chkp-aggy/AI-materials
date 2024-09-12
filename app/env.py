"""
Module for loading sensitive information from Environment Variables
"""

from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Retrieve the API key and endpoint from environment variables
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
AZURE_OPENAI_API_MODEL = os.getenv("AZURE_OPENAI_API_MODEL")

if not AZURE_OPENAI_API_KEY or not AZURE_OPENAI_ENDPOINT or not AZURE_OPENAI_API_VERSION:
    raise ValueError("Azure API key, endpoint or version not found in environment variables.")

if not AZURE_OPENAI_API_MODEL:
    raise ValueError("GPT model not found in environment variables.")
