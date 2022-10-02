# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/FacultadInformatica-LinkedData/Curso2022-2023/blob/master/Assignment4/course_materials/notebooks/Task07.ipynb

**Task 07: Querying RDF(s)**
"""

#!pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""

# TO DO
from rdflib.plugins.sparql import prepareQuery
ns = Namespace("http://somewhere#")
q1 = prepareQuery ('''
    SELECT ?subj WHERE {
        ?subj rdfs:subClassOf ns:Person.
    }
''',
  initNs = {"rdfs": RDFS, "ns": ns}
)

# Visualize the results

for r in g.query(q1):
 print(r)

for s, p, o in g.triples((None,RDFS.subClassOf,ns.Person)):
 print(s,p,o)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

# TO DO
q2 = prepareQuery ('''
    SELECT ?subj ?subj2 WHERE {
      {
        ?subj rdfs:type ns:Person.}
        UNION
        {?subc rdfs:subClassOf* ns:Person.
        ?subj2 rdfs:type ?subc.}
    }
''',
  initNs = { "rdf": RDF, "ns": ns}
)

# Visualize the results

for r in g.query(q2):
 print(r)

for s, p, o in g.triples((None, RDF.type, ns.Person)):
 print(s)

for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
  for subj, prop, value in g.triples((None,RDF.type,s)):
    print(subj)

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**

"""

# TO DO
q3 = prepareQuery ('''
    SELECT ?subj ?property ?class WHERE { 
      {?subj rdf:type ns:Person.
       ?subj ?property ?class}
       UNION 
      {?aux rdfs:subClassOf* ns:Person.
       ?subj rdf:type ?aux.
       ?subj ?property ?class}
    }
''',
 initNs = {"rdfs": RDFS, "rdf": RDF, "ns": ns}
)
# Visualize the results
for r in g.query(q3):
 print(r)

for person,prop,c in g.triples((None,RDF.type,ns.Person)):
  for x,prop,cl in g.triples((person,None,None)):
    print(person,prop,c)

for scPerson,prop,c in g.triples((None,RDFS.subClassOf,ns.Person)):
  for x,prop,val in g.triples((None,RDF.type,scPerson)):
    for person,prop,c in g.triples((x,None,None)):
      print(person,property,c)