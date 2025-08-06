import os
import json
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.utilities import SQLDatabase

# Import Custom Module
import ivt_bdg as ivb

# Load the JSON
with open('ref_examples.json', 'r') as f:
    examples = json.load(f)

# Connect to Database
def handle_db():
    db_user = os.environ.get['DB_USER']
    db_password = os.environ.get['DB_PASSWORD']
    db_host = os.environ.get['DB_HOST']
    db_name = os.environ.get['DB_NAME']

    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}", sample_rows_in_table_info=3)
    return db

# Create the Store
def handle_store():
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    to_vectorize = [" ".join(example.values()) for example in examples]
    vectorstore = Chroma.from_texts(to_vectorize, embeddings, metadatas=examples)
    return vectorstore

# Handle Custom Prompt
def handle_prompt():
    vs = handle_store()
    return ivb.handle_few_shot_prompt(vs)