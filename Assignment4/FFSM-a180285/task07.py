# **Task 07: Querying RDF(s)**
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"
import pandas as pd
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery

g = Graph()
NS = Namespace("http://somewhere#")
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
g.namespace_manager.bind('ns', NS, override=False)
g.namespace_manager.bind('vcard', VCARD, override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

# **TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**
q1 = prepareQuery('''
  SELECT ?any 
  WHERE { 
    ?any rdfs:subClassOf ns:Person .
  }''',
  initNs = {"ns": NS, "rdfs":RDFS}
)

print("\n 7.1 Result")
for r in g.query(q1):
  print(f"{r.any} is subClass of {NS.Person}")


# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
q2 = prepareQuery('''
  SELECT ?person ?clss 
  WHERE { 
    {
      SELECT ?person ?clss
      WHERE {
        BIND(ns:Person as ?clss)
        ?person a ?clss.
      }
    }
    UNION
    {
      SELECT ?person ?clss
      WHERE {
        ?clss rdfs:subClassOf ns:Person .
        ?person a ?clss .
      }
    }
  }''',
  initNs = {"ns": NS, "rdf":RDF, "rdfs":RDFS}
)

print("\n 7.2 Result")
for r in g.query(q2):
  print(f"{r.person} is a {r.clss}")

# **TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**

# Using SPARQL:
q3 = prepareQuery('''
  SELECT ?person ?prop ?value
  WHERE { 
    ?person rdf:type ns:Person ;
      ?prop ?value .
  }''',
  initNs = {"ns": NS, "rdf":RDF}
)

q3a_result = []
for person, prop, value in g.query(q3):
  q3a_result.append((person, f"...{prop[-45:]}", value))

df = pd.DataFrame(q3a_result, columns =['Person', 'Property', 'Value'])

print("\n7.3a result Sparql🚀 ")
print(df)

# Using RDFLib:
q3b_result = []
for person,_,_ in g.triples((None, RDF.type, NS.Person)):
  for _,prop,value in g.triples((person, None, None)):
    q3b_result.append((person, f"...{prop[-45:]}", value))

df = pd.DataFrame(q3b_result, columns =['Person', 'Property', 'Value'])

print("\n7.3b result RDFLib🚀 ")
print(df)


