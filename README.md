# PYNS (PYthon Neutrosophic Sets framework)


Giorgio Nordo - Dipartimento MIFT, Università di Messina, Italy
www.nordo.it   |  giorgio.nordo@unime.it 

---
## Introduction

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

Both the code and the underlying data structures of the three classes NSuniverse, NSset
and NSmapping have been explained in detail and also concrete examples of using the introduced
objects and methods have been given.
The attention given to the usability of these classes and the extensive documentation provided
with a rich assortment of examples and use cases, gives us confidence that, in addition to
being used for the exploration of uncertain data and practical applications, it can be the subject
of further study and expansion opening up new research perspectives in various scientific
and applied disciplines that use the tools of neutrosophic set theory.

## Notation

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
``` 
an extended dictionary can be expressed as strings of the type:
```
"key1->value1,key2|->value2; . . . keyn->valuen"
```



## Examples

In order to better illustrate how the above methods are used,
let us consider the following example of code executed interactively in the Python console.

```
>>> from pyns.ns_universe import NSuniverse
>>> from pyns.ns_set import NSset
>>> U = NSuniverse("a,b,c")
>>> A = NSset(U)
>>> A.setElement('a', (0.8,0.2,0.1))
>>> A.setElement('c', (0.3,0.2,0.4))
>>> A.getMembership('a')
0.8
>>> A.getNonMembership('c')
0.4
>>> print(A.getElement(c))
[0.3, 0.2, 0.4]
>>> A.setIndeterminacy('b',0.9)
>>> print(A)
< a/(0.8,0.2,0.1), b/(0.0,0.9,1.0), c/(0.3,0.2,0.4) >
>>> print(f"{A:t}")
            |   membership   |  indeterminacy | non-membership |
----------------------------------------------------------------
 a          |            0.8 |            0.2 |            0.1 |
 b          |              0 |            0.9 |              1 |
 c          |            0.3 |            0.2 |            0.4 |
----------------------------------------------------------------
>>> A.setAbsolute()
>>> print(A)
< a/(1,1,0), b/(1,1,0), c/(1,1,0) >
```

The following example illustrates how the neutrosophic set operators can
easily and profitably used in the interactive mode by means of the Python console.

```
>>> from pyns.ns_universe import NSuniverse
>>> from pyns.ns_set import NSset
>>> U = NSuniverse(’a’,’b’,’c’)
>>> A = NSset(U, "(0.5,0.3,0.2), (0.6,0.2,0.3), (0.4,0.2,0.7)")
>>> print(A)
< a/(0.5,0.3,0.2), b/(0.6,0.2,0.3), c/(0.4,0.2,0.7) >
>>> B = NSset(U, "(0.2,0.2,0.2), (0.4,0.1,0.6), (0.8,0.3,0.1)")
>>> print(B)
< a/(0.2,0.2,0.2), b/(0.4,0.1,0.6), c/(0.8,0.3,0.1) >
>>> print(A + B)
< a/(0.5,0.3,0.2), b/(0.6,0.2,0.3), c/(0.8,0.3,0.1) >
>>> print(A & B)
< a/(0.2,0.2,0.2), b/(0.4,0.1,0.6), c/(0.4,0.2,0.7) >
>>> print(˜A)
< a/(0.2,0.7,0.5), b/(0.3,0.8,0.6), c/(0.7,0.8,0.4) >
>>> F = A - B
>>> print(F)
< a/(0.2,0.3,0.2), b/(0.6,0.2,0.4), c/(0.1,0.2,0.8) >
>>> print(F <= A)
True
>>> print(F == A & ˜B)
True
```

Finally, the following code executed in interactive mode in the Python console illustrates
how to define and manage mappings on neutrosophic sets.
```
>>> from pyns.ns_universe import NSuniverse
>>> from pyns.ns_set import NSset
>>> from pyns.ns_mapping import NSmapping
>>> U = NSuniverse("a,b,c")
>>> V = NSuniverse(1,2)
>>> f = NSmapping(U,V, (2,1,2))
>>> print(f)
{ a, b, c } -> { 1, 2 }
----------------------------------------------------------------
a |-> 2
b |-> 1
c |-> 2
>>> print(f.getValue(’a’))
2
>>> g = NSmapping("a->2 b->1 c->2")
>>> print( f==g )
True
>>> print(g)
{ a, b, c } -> { 1, 2 }
----------------------------------------------------------------
a |-> 2
b |-> 1
c |-> 2
>>> print(h.getDomain())
{ a, b, c }
>>> print(h.getCodomain())
{ 1, 2 }
>>> print(f.getMap())
{’a’: ’2’, ’b’: ’1’, ’c’: ’2’}
>>> h = NSmapping("a,b,c", "1,2", "a->2 b->1 c->2")
>>> print( f==h )
True
```


