# examples of neutrosophic sets
from pyns.ns_universe import NSuniverse
from pyns.ns_set import NSset

U = NSuniverse(1,2,3)
A = NSset(U)
A.setElement(1,(0.7,0.3,0.1))
A.setElement(2,(0.4,0.6,0.9))
A.setMembership(3, 1)
A.setIndeterminacy(3, 0.2)
print(A)

V = NSuniverse('a','b','c')
B = NSset(V)
B.setElement('a',(0.4,0.2,0.3))
print(B)

B.setAbsolute()
print(B)