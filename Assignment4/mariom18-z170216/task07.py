from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"


g = Graph()
ns = Namespace("http://somewhere#")
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
g.namespace_manager.bind('ns', ns, override=False)
g.namespace_manager.bind('vcard', VCARD, override=False)
g.parse(github_storage + "/rdf/example6.rdf", format="xml")


q1=prepareQuery('''  SELECT ?subj
  WHERE { 
    ?subj rdfs:subClassOf ns:Person. 
  }''',initNs = {"rdfs":RDFS, "ns":ns} )
#for s in g.query(q1):
#  print(s)

q2 = prepareQuery('''  SELECT DISTINCT ?subj
    WHERE { 
      {
        ?subj rdf:type ns:Person. 
      }
      UNION {
        ?pred rdfs:subClassOf/rdfs:subClassOf* ns:Person.
        ?subj rdf:type ?pred
      }
    }
    ''', initNs={"rdfs": RDFS, "rdf": RDF, "ns": ns})


#for s in g.query(q2):
 #   print(s)

q3 = prepareQuery(''' SELECT DISTINCT ?subj ?pred ?obj
    WHERE{
    	{
      ?subj rdf:type ns:Person .
      ?subj ?pred ?obj
      } UNION {
      ?subj2 rdfs:subClassOf/rdfs:subClassOf* ns:Person .
      ?s rdf:type ?subj2 .
      ?subj ?pred ?obj
      }
    } ''', initNs={"rdf": RDF, "rdfs": RDFS, "ns": ns}
                     )
for s in g.query(q3):
  print(s)
