#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 17:03:15 2019

@author: petern
"""


#https://py2neo.org/v4/data.html#node-and-relationship-objects
from py2neo import Graph, Node, Relationship
from py2neo import Database
#from py2neo import Database

a = Node("Person", name="Alice")
b = Node("Person", name="Bob")
ab = Relationship(a, "KNOWS", b)

# phải run server trước
#
graph = Graph("http://localhost:7474", auth=("neo4j", "Abc123"))
print(graph)
graph.create(ab)
#
#
#selector = NodeSelector(graph)
#
#graph_3 = Graph("bolt://localhost:7687")



#class HelloWorldExample(object):
#    def __init__(self,uri,user,password):
#        self._driver=GraphDatabase.driver(uri,auth=(user,password))
#    def close(self):
#            self._driver.close()
#    def print_greeting(self,message):
#        with self._driver.session() as session:
#            greeting=session.write_transaction(self._create_and_return_greeting,message)
#        print(greeting)
#    @staticmethod
#    def _create_and_return_greeting(tx,message):
#        result=tx.run("CREATE (a:Greeting) "
#                      "SET a.message = $message "
#                      "RETURN a.message + ', from node ' + id(a)",message=message)
#        return result.single()[0]

    