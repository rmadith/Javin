from flask import (Blueprint, request, json)

from neo4j import GraphDatabase
import openai
from Algorithm import graph, search
import json
import re
import requests 

bp = Blueprint('upload', __name__, url_prefix='/upload')

session = driver.session()


@bp.route('/', methods=['POST'])
def upload():

    # get the query from the request
    # example: {"query": "what is the best project james has done?"}
    data = json.loads(request.data)

    query = data['query']

    # call gpt3 with our query parameters
    gpt3_response = call_gpt3(query)

    # after calling gpt3 we have to call neo4js with the keywords to return our "hits"
    neo4js_response = call_neo4js(gpt3_response)

    response = {}

    # put them in a response object
    response['keywords'] = gpt3_response
    response['hits'] = neo4js_response

    # get the keywords from gpt3 query
    # then add them to a key of the keywords into the response
    # example: {"keywords": ["best", "project", "james"]}

    # next we have to query neo4js with our keywords
    # add to the response the hits from neo4js

    # this is an example result

#    {
#        "keywords": ["best", "project", "james"],
#        "hits": [
#            {
#                "name": "Best project",
#                "description": "This is a description",
#                "link": "https://github.com/james-gavin/",
#                "stars": 1
#            }
#        ]
#    }

    return {
  "keywords": gpt3_response,
  "hits": neo4js_response
}


def call_gpt3(query):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Use Github Topics to create a list of 6 topics for the prompt (Seperate by commas)- \n" + description + "\nGithub Topics:",
    temperature=0.2,
    max_tokens=265,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )
  text = response["choices"][0]["text"].strip().split(",")
  return text

def call_neo4js(session, array):
    nodes_list = []
    nodes = search.find_all_shortest(session, array)
    for i in nodes:
        node = search.getinformations(session, i)
        nodes_list.append(node)
    nodes = json.dumps(nodes)
    return nodes_list
