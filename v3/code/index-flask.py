from flask import Flask
from flask import request
import agents
import chains
import json

from langchain import PromptTemplate
from logging.config import dictConfig
app = Flask(__name__)

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'DEBUG',
        'handlers': ['wsgi']
    }
})

@app.route('/demo/google-search', methods=['get'])
def google_search():
    query=request.args.get("q")
    prompt = PromptTemplate(
        input_variables=["question"],
        template="""
        I'm a professional amazon seller, answer the following question in json format:
        {question}
        """,
    )
    result = agents.google_agent.run(prompt.format(question=query))
    return result

@app.route('/demo/call-api', methods=['get'])
def call_api():
    result=chains.api_chain.run('what is the name of the user with id 88765?')
    return result


@app.route('/internal/user-api', methods=['get'])
def internal_api():
    user_id=request.args.get("user_id")
    print(user_id)
    if int(user_id)==88765:
        return json.dumps({
            'id':88765,
            'user_name':'john'
        })
    elif int(user_id)==6666:
        return json.dumps({
            'id':6666,
            'user_name':'jackson'
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
