# -*- coding: utf-8 -*-

github_storage = "https://github.com/edw9318/Curso2022-2023/tree/master/Assignment4/course_materials/rdf"

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS

g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**

**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**
"""