# PYNS (PYthon Neutrosophic Sets framework)


Giorgio Nordo - Dipartimento MIFT, Università di Messina, Italy
www.nordo.it   |  giorgio.nordo@unime.it 
---

**PYthon Neutrosophic Sets framework** (**PYNS** for short) is an open source framework developed in Python and consisting of three
distinct classes designed to manipulate in a simple and intuitive way both symbolic representations of neutrosophic
sets over universes of various types as well as mappings between them. The code is described in detail
and many examples and use cases are also provided.

The PYthon Neutrosophic Sets framework consists of three classes designed 
to manage respectively universe sets (the NSuniverse class),
neutrosophic sets (the NSset class) and functions between them (the NSmapping class. As
is natural, the class NSset depends on (i.e. uses) the class NSuniverse class) while the
NSmapping class uses the other two.

These three classes are respectively contained in the Python files ns_universe.py,
ns_set.py and ns_mapping.py which are located in the package directory pyns. The
same directory contains also the file ns_util.py where are defined some utility functions
external to the classes but employed by them. 

We will make extensive use of Python’s dict (dictionary) data structure
both for the internal representation of neutrosophic sets and for the definition of functions
between universe sets. To make it even easier and more streamlined to use such structures
both in interactive mode as well as in writing client code based on such classes, it was chosen
to also allow their representation as a string and in free format, i.e., leaving the user free to:
-  indifferently use not only the usual symbol : (colon) but also alternatively the strings
-> (arrow) and |-> (maps-to) as separators between keys and values
- indifferently use not only the usual symbol , (comma) but also ; (semicolon) as separators
of the value-key pairs
in any combination thereof, and we will refer to this type of representation by the name
extended dictionary. In other words, while a classical Python dictionary has a form like:
```
{key1 : value1, key2 : value2, . . . keyn : valuen}
``` ,
an extended dictionary can be expressed as strings of the type:
```
"key1->value1,key2|->value2; . . . keyn->valuen"'
```
