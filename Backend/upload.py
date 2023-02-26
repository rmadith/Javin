from flask import (Blueprint, request, json)

bp = Blueprint('upload', __name__, url_prefix='/upload')


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
  "keywords": ["best", "project", "james"],
  "hits": [
    {
      "name": "Best project",
      "description": "This is a description",
      "link": "https://github.com/james-gavin/",
      "stars": 1
    },
    {
      "name": "I hate my life",
      "description": "I just want to die",
      "link": "https://github.com/james-gavin/",
      "stars": 5
    },
    {
      "name": "What has the world come to",
      "description": "i just made some eggs",
      "link": "https://github.com/james-gavin/",
      "stars": 69
    },
    {
      "name": "What has the world come to",
      "description": "i just made some eggs",
      "link": "https://github.com/james-gavin/",
      "stars": 69
    },
    {
      "name": "What has the world come to",
      "description": "i just made some eggs",
      "link": "https://github.com/james-gavin/",
      "stars": 69
    },
    {
      "name": "What has the world come to",
      "description": "i just made some eggs",
      "link": "https://github.com/james-gavin/",
      "stars": 69
    },
    {
      "name": "What has the world come to",
      "description": "i just made some eggs",
      "link": "https://github.com/james-gavin/",
      "stars": 69
    },
    {
      "name": "What has the world come to",
      "description": "i just made some eggs",
      "link": "https://github.com/james-gavin/",
      "stars": 69
    },
    {
      "name": "What has the world come to",
      "description": "i just made some eggs",
      "link": "https://github.com/james-gavin/",
      "stars": 69
    },
    {
      "name": "What has the world come to",
      "description": "i just made some eggs",
      "link": "https://github.com/james-gavin/",
      "stars": 69
    },
    {
      "name": "What has the world come to",
      "description": "i just made some eggs",
      "link": "https://github.com/james-gavin/",
      "stars": 69
    },
    {
      "name": "What has the world come to",
      "description": "i just made some eggs",
      "link": "https://github.com/james-gavin/",
      "stars": 69
    },
    {
      "name": "What has the world come to",
      "description": "i just made some eggs",
      "link": "https://github.com/james-gavin/",
      "stars": 69
    },
    {
      "name": "What has the world come to",
      "description": "i just made some eggs",
      "link": "https://github.com/james-gavin/",
      "stars": 69
    }
  ]
}


def call_gpt3(query):
    # call gpt3 with our query parameters
    return "finish me"

def call_neo4js(keywords):
    # query neo4js with our keywords
    return "finish me"
