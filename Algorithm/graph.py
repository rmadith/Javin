###
# Author: Muthu Adithya Ramnarayanan
# This file contains all the functions that are used to create the graph database
# It uses the Neo4j API to create the graph
# They are quick functions to call Neo4j Queries
###

from neo4j import GraphDatabase

# Create a Project Node and unique information about it
def create_project(tx, identity, name, description, stars, forks, ranking, link, size, language):
    # Check if any parameter is empty or NoneType
    if name is None or name == "" and description is None or description == "" and stars is None or stars == "" and forks is None or forks == "" and ranking is None or ranking == "" and link is None or link == "" and size is None or size == "" and language is None or language == "":
        return False;
    else:
        tx.run("CREATE (a:Project {id: $identity, name: $name, language: $language, description: $description, stars: $stars, forks: $forks, ranking: $ranking, link: $link, size: $size })", identity = identity, name=name, description=description, stars=stars, forks=forks, ranking=ranking, link=link, size = size, language = language)
        return True

# Create a keyword Node 
def create_keyword(tx, name, identity):
    # Check if keyword already exists
    if tx.run("MATCH (a:Keyword {name: $name}) RETURN a", name=name).single() is None:
        tx.run("CREATE (a:Keyword {name: $name, identity : $identity})", name=name, identity = identity)
        return True
    else:
        return False

# Create a relationship between a project and a keyword with weights associated
def create_relationship(tx, project, keyword, weight):
    tx.run("MATCH (a:Project {name: $project}) "
           "MATCH (b:Keyword {name: $keyword}) "
           "MERGE (a)-[r:IS_A_PROJECT_OF]->(b) "
           "SET r.weight = $weight", project=project, keyword=keyword, weight=weight)
    tx.run("MATCH (a:Project {name: $project}) "
           "MATCH (b:Keyword {name: $keyword}) "
           "MERGE (b)-[r:IS_A_KEYWORD_OF]->(a) "
           "SET r.weight = $weight", project=project, keyword=keyword, weight=weight)


# List all keywords in the database
def list_keywords(tx):
    return tx.run("MATCH (a:Keyword) RETURN a.name").values()

    
