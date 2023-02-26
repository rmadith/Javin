from neo4j import GraphDatabase
import openai
import graph
import json
import re
import search
import requests 

# Set your OpenAI API key
openai.api_key = "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"

# Set your Neo4j database credentials
uri = "bolt://localhost:7687"
user = "neo4j"
password = "password"
driver = GraphDatabase.driver(uri, auth=(user, password))

# Create a session with the database
session = driver.session()

def getkeywords_final(description):
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

# Open repos.json file
with open('repos.json') as f:
    data = json.load(f)

def get_tags(link):
    link = "https://api.github.com/repos/" + link 
    headers = {'Authorization': 'token ' + "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"}
    # link is a github link
    response = requests.get(link, headers=headers)
    # get the tags from the github link
    tags = response.json()
    # return the tags
    return tags


# Loop through each project and create a node for it
lists = []
def create_graph():
   counter = 0
   for language in data:
      for project in data[language]:
         # Parse Project name - [awesome-ios](https://github.com/vsouza/awesome-ios) => vsouza/awesome-ios
         project_name = re.sub(r'\[.*\]\((.*)\)', r'\1', project["Project Name"])
         print(project_name)
         # Create a project node
         graph.create_project(session, project_name)

         # Get star count
         stars = int(project["Stars"])

         # Get forks count
         forks = int(project["Forks"])

         # Get Ranking 
         ranking = int(project["Ranking"])

         weight = (stars + forks) / ranking

         # Get the description of the project
         description = project["Description"]
         # Get the keywords from the description
         keywords = getkeywords(description)
         # Split the keywords into a list
         keywords = keywords.split(",")
         print(keywords)
         for keyword in keywords:
            # Create a keyword node
            graph.create_keyword(session, keyword)
            # Create a relationship between the project and the keyword
            graph.create_relationship(session, project_name, keyword, weight)

        #create a list with all the values
         lists.append([project_name, stars, forks, ranking, weight, keywords])
         counter += 1
         print(counter)

def create_graph_final():
    counter = 0
    counter_id = 0
    for language in data:
        for project in data[language]:
            # Parse Project name - [awesome-ios](https://github.com/vsouza/awesome-ios) => vsouza/awesome-ios
            project_name_link = re.sub(r'\[.*\]\((.*)\)', r'\1', project["Project Name"])
            project_name = project_name_link.split("/")[3] + "/" + project_name_link.split("/")[4]

            
            git_json = get_tags(project_name)
            
            
            # Create Graph
            if graph.create_project( session, counter, project_name, project["Description"], git_json["stargazers_count"], git_json["forks_count"], project["Ranking"], project_name_link, git_json["size"], git_json["language"] ):
                counter += 1
            else:
                continue

            
            for keyword in git_json["topics"]:
                if graph.create_keyword(session, keyword, counter_id):
                    counter_id += 1
                graph.create_relationship(session, project_name, keyword, 1)

            print(counter)

            # Export to CSV
            with open('data_repo.csv', 'a') as f:
                try:
                   f.write(str(counter) + "," + project_name + "," + project["Description"] + "," + str(git_json["stargazers_count"]) + "," + str(git_json["forks_count"]) + "," + project["Ranking"] + "," + project_name_link + "," + str(git_json["size"]) + "," + git_json["language"] + "," + str(git_json["topics"]) + "\n")
                except:
                    continue
                        


def get_shortest(array):
    nodes_list = []
    nodes = search.find_all_shortest(session, array)
    for i in nodes:
        node = search.getinformations(session, i)
        nodes_list.append(node)
    nodes = json.dumps(nodes)
    return nodes_list

