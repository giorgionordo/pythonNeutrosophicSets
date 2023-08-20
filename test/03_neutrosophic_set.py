"""
Package Python Neutrosophic Sets (PYNS)
----------------------------------------------------------------------------------
author: Giorgio Nordo - Dipartimento MIFT, Università di Messina, Italy
www.nordo.it   |  giorgio.nordo@unime.it
----------------------------------------------------------------------------------
some examples of neutrosophic sets
"""
from NS.pyns.ns_universe import NSuniverse
from NS.pyns.ns_set import NSset

A = NSset("a,b,c", [(0.4,0.4,0.3), (0.1,0.1,0.1), (0.2,0.2,0.2)])    # con lista di tuple
A = NSset("a,b,c", [[0.4,0.4,0.3], [0.1,0.1,0.1], [0.2,0.2,0.2]])    # con lista di liste
A = NSset("a,b,c", [[0.4,0.4,0.3], (0.1,0.1,0.1), [0.2,0.2,0.2]])    # con lista di liste e tuple mischiate
A = NSset("a,b,c", ([0.4,0.4,0.3], [0.1,0.1,0.1], [0.2,0.2,0.2]))    # con tupla di liste
A = NSset("a,b,c", ((0.4,0.4,0.3), (0.1,0.1,0.1), (0.2,0.2,0.2)))    # con tupla di tuple
A = NSset("a,b,c", ((0.4,0.4,0.3), [0.1,0.1,0.1], (0.2,0.2,0.2)))    # con tupla di tuple e liste mischiate
A = NSset("a,b,c", "[0.4,0.4,0.3], (0.1,0.1,0.1); [0.2,0.2,0.2]")    # con stringa di liste o tuple

U = NSuniverse('a','b','c')
U = NSuniverse("a,b;c")
A = NSset(U, "[0.4,0.4,0.3], (0.1,0.1,0.1); [0.2,0.2,0.2]")
print(f"A = {A}")
print(f"A = {A:t}")
print(f"La cardinalità è {A.cardinality()}")

U = NSuniverse(1,2,3)
A = NSset(U)


A.setElement(1,(0.7,0.3,0.1))  # con una tupla
A.setElement(1,[0.7,0.3,0.1])  # con una lista
A.setElement(2,"(0.7;0.3,0.1)")  # con una stringa
A.setMembership(3, 1)
A.setIndeterminacy(3, 0.2)
print("A= ", A)

V = NSuniverse('a','b','c')
B = NSset(V)
B = NSset("a,b,c,d")
B.setElement('a',(0.4,0.2,0.3))
print("B = ", B)
print(f"indeterminacy = {B.getIndeterminacy('d')}")

F = NSset(V)
F.setAbsolute()
print("F=", F)