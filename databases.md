NETWORK THEORY : Network theory is the study of how things are connected and how they interact with each other.
                 It uses nodes (points) and edges (lines) to represent a network.
Edge (or Link): A connection between two nodes.

example : Electric Circuit
Nodes = Components (bulbs, batteries)

Edges = Wires
Example: A simple light bulb circuit is a small electrical network.

GRAPH THEORY : Graph theory is a branch of mathematics that studies graphs — which are made of dots (called nodes or vertices) and lines (called edges) that connect them.

example: Flight Network
Airports = vertices
Flights = edges
Helps airlines plan routes and schedules.

TRADITIONAL DATABASE : A traditional database is a system used to store, organize, and manage data in tables (rows and columns), usually using Structured Query Language (SQL).
example: Hospital Management
Tables for patients, doctors, appointments, medicines.
common Traditional Databases:
MySQL
Oracle Database
Microsoft SQL Server
PostgreSQL
IBM DB2

GRAPH DATABASE : A graph database is a type of database that stores data as a network of connections — using nodes and edges instead of tables.
Social Networks
Facebook, LinkedIn use graph databases to manage connections
example: 

Popular Graph Databases:
Neo4j
Amazon Neptune
ArangoDB
OrientDB

CENTRALITY : Centrality is a way to measure how important a node (point) is in a network or graph.
It tells us which people, places, or things are the most influential or central in a network.

example:  Social Media

Degree Centrality
Example: A celebrity like Cristiano Ronaldo has millions of followers.
Meaning: High degree centrality — many direct connections (followers).

Betweenness Centrality
Example: A journalist who connects two different communities (e.g., tech & politics).
Meaning: They bridge two groups, spreading info across otherwise unconnected areas.

Closeness Centrality
Example: An influencer who can quickly reach any user through a few reshares.
Meaning: They are close to everyone in the network — ideal for fast info spread.

Eigenvector Centrality
Example: Someone followed by other top influencers.
Meaning: Even if their follower count is small, the quality of their connections is high.



Degree centrality : it counts how many direct connections a node has.
                    more connections = more central
example : Popular kid at school with lots of connections

Betweenness centrality : counts how many shortest paths go through each node.Control over shortest paths.
example : Middleman passing messages between groups.

closeness centrality : Measures how close a node is all to others. Average distance to all others.
                       lower total distance = more central.
example : Central warehouse for fast deliveries.

eigenvector centrality : importance based on connections to important nodes.

                          Ax = lamda x 
example  : A - B - D
               |                         
               D

A is only connected to B

B is connected to A, C, D

C and D are only connected to B

Here, B has the highest eigenvector centrality because:

It connects with many nodes, and

Those nodes (C, D) don’t connect with anyone else → B’s influence is greater.


Social network : A social network is a structure made up of individuals or entities (called nodes) that are connected by one or more types of relationships (called edges or links).

A graph is used to model a social network.

example:
Nodes = People

Edges = Relationships

Edges can be:

Undirected (e.g., Facebook friends: mutual)

Directed (e.g., Twitter follows: one-way)

Key Concepts in Social Network Analysis (SNA):


Degree – Number of connections a node has

Centrality – Importance of a node (like eigenvector centrality)

Clustering – Tendency of people to form tightly knit groups

Path – Shortest connection between two nodes

Community – Group of nodes with stronger internal links than external

ENTITY : In a social network, an entity could be:

A person

A company

A Facebook page

A group
