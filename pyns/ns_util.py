"""
Package Python Neutrosophic Sets (PYNS)
Utility functions for all the class of the package
----------------------------------------------------------------------------------
author: Giorgio Nordo - Dipartimento MIFT. Università di Messina, Italy
www.nordo.it   |  giorgio.nordo@unime.it
"""

def NSreplace(elem, sostituz={}):
    """ restituisce la stringa elem dopo aver eseguito tutti i rimpiazzamenti
        di sottostringhe contenuti nel dizionario sostituz
        ----
        Parameters:
        - elem: string
        - sostituz: dictionary having as keys the substrings to replace with their respective values
        ---
        Returns: the same string after all the replacements
        """
    for k in sostituz:
        elem = elem.replace(k, sostituz[k])
    return elem