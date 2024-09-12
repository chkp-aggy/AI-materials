# GPT-based 'app'

## /app/
This directory is a minimal GPT-based app.
It consists of the following files:
* `.env`: A file with Environment variables. You need to add your API key to this file (Locally. Don't commit it.)
* `env.py`: A module designed to read the Environment variables
* `openai_tool.py`: A module with helper functions for working with Azure OpenAI
* `gpt_query.py`: A module that utilized all the above mentioned components to query GPT print its response

## Running the mock app
1. Get your [API key](https://wiki.checkpoint.com/confluence/pages/viewpage.action?pageId=554281566#CloudSecurityR&DAIHackathon-AI_ENVIRONMENT)
2. Insert it to the `.env` file
3. Create a virtualenvironment (optional but recommended)
4. Install dependencies with `pip install -r requirements.txt`
5. Run `gpt_query.py` script (the 'main' script in this app)
6. Verify you get a response from GPT
