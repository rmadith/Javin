
# Javin (An Aspiring AI)

Repository for a web app that recommends repositories for new code development

Requires - Neo4J, Next.Js and Python (Flask) to functions

Link to [deployment](https://javin.vercel.app/)



## Installation
Look down this section to set up your own installation of Javin!

## Frontend Dev Environment
To run a development version of the frontend. Use this - 

```bash
npm run dev
# or
yarn dev
# or
npm dev
```

Note - Before you run the code against your neo4j installation, be sure to change the IP fetches to 'localhost'

## Database Dev Environment

To run a development version of the database, we have set up a docker zip for you to use. The Docker file runs on an ArmV8 architecure. For all other architecures you will need to use -

```
docker buildx 
```

If you have arm, you will need to - 

```
ddocker run \
    --name testneo4j \
    -p7474:7474 -p7687:7687 \
    -d \
    -v $HOME/neo4j/data:/data \
    -v $HOME/neo4j/logs:/logs \
    -v $HOME/neo4j/import:/var/lib/neo4j/import \
    -v $HOME/neo4j/plugins:/plugins \
    --env NEO4J_AUTH=neo4j/password \
    neo4j-hackathon:latest
```



 
## Authors

- [Muthu Adithya Ramnarayanan](https://www.github.com/rmadith)
- [Shlok Desai](https://github.com/ShlokDesai33)
- [James Gavin](https://github.com/james-gavin)
- [Julia Paciorek](https://github.com/JuliaPaciorek)

