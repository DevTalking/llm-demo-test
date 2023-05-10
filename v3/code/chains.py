from langchain.llms import OpenAI
import os
from langchain.chains import APIChain
llm = OpenAI(temperature=0, openai_api_key=os.environ['OPENAI_API_KEY'])
api_chain = APIChain.from_llm_and_api_docs(llm, """
the api return user information include two fields: 
user_name: text
id: integer
api endpoint: http://localhost:9000/internal/user-api
api parameters:
user_id: specify the user id to retrieve information of a specific user

""", verbose=True)