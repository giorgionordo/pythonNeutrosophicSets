# some examples of universe sets
from pyns.ns_universe import NSuniverse

U = NSuniverse(3)
print(U)
print(repr(U))

U2 = NSuniverse([2,4,6,8])
print(U2)

V = NSuniverse(3,5,7,9)
print(V)

V2 = NSuniverse((2,4,5))
print(V2)

V3 = NSuniverse(3)
print(V3)

Z = NSuniverse("a")
print(Z)

T = NSuniverse(" ( a b c , d ; e )")
print(T)
print(f"Cardinality of T is è {T.cardinality()}")
