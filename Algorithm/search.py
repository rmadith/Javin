###
# Author: Muthu Adithya Ramnarayanan
# This file contains all the functions that are used to search the graph database
# It uses the Neo4j API to search the graph
# They are quick functions to call Neo4j Queries
###

# Given multiple keywords, find projects that match all of them
def find_projects(tx, keywords):
    # Create a list of projects that match all keywords
    projects = []
    # Loop through each keyword
    for keyword in keywords:
        # Find projects that match the keyword
        projects.append(tx.run("MATCH (a:Keyword {name: $keyword})-[:HAS_KEYWORD]->(b:Project) RETURN b.name", keyword=keyword).values())
    # Find projects that match all keywords
    return projects

# Between two keywords, find shortest path
def find_shortest_path(tx, keyword1, keyword2):
    # Find shortest path between two keywords
    path = tx.run("MATCH p=shortestPath((a:Keyword {name: $keyword1})-[:IS_A_KEYWORD_OF*]-(b:Keyword {name: $keyword2})) RETURN nodes(p)", keyword1=keyword1, keyword2=keyword2).values()
    return path

def find_all_shortest(tx, array):
    paths = []
    for i in range(len(array)):
        if i == len(array) - 1:
            break
        # Check if Keyword exists 
        if tx.run("MATCH (a:Keyword {name: $keyword1}) RETURN a", keyword1=array[i]).single() is None:
            continue
        if tx.run("MATCH (a:Keyword {name: $keyword2}) RETURN a", keyword2=array[i+1]).single() is None:
            continue
        path  = tx.run("MATCH p=shortestPath((a:Keyword {name: $keyword1})-[:IS_A_KEYWORD_OF*]-(b:Keyword {name: $keyword2})) RETURN p", keyword1=array[i], keyword2=array[i+1])
        path = path.single()[0]
        #<Node element_id='4:b538ac41-bdf5-499a-ba4c-652883196492:7450' labels=frozenset({'Project'}) properties={'forks': 19297, 'size': 34550, 'link': 'https://github.com/keras-team/keras', 'name': 'keras-team/keras', 'description': 'Deep Learning for humans', 'ranking': '97', 'language': 'Python', 'stars': 57409, 'id': 2496}>
        for nodes in path.nodes:
            if nodes.get('id') != None:
                paths.append(nodes.get('id'))
    return paths


def getinformations(tx, id):
    # Get informations about a project
    info = {}
    informations = tx.run("MATCH (a:Project {id: $id}) RETURN a", id=id).values()
    print(informations)
    info["id"] = informations[0][0].get('name')
    info["name"] = informations[0][0].get('name')
    info["description"] = informations[0][0].get('description')
    info["stars"] = informations[0][0].get('stars')
    info["forks"] = informations[0][0].get('forks')
    info["ranking"] = informations[0][0].get('ranking')
    info["link"] = informations[0][0].get('link')
    info["size"] = informations[0][0].get('size')
    info["language"] = informations[0][0].get('language')
    return info
