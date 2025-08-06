import os
import getpass
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.sql import SQLDatabaseChain

# Import Custom Module
import ivt_util as ivu

# Handle Environment Variables
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google API key: ")
if "MODEL_NAME" not in os.environ:
    os.environ["MODEL_NAME"] = getpass.getpass("Enter your Model Name: ")

# Define the Model
llm = ChatGoogleGenerativeAI(
    model = os.environ.get("MODEL_NAME"),
    temperature=0.6,
    max_retries=2
)

# Create the Chain
db = ivu.handle_db()
prompt = ivu.handle_prompt()
ivt_chain = SQLDatabaseChain.from_llm(llm, db, verbose = True, prompt = prompt)
