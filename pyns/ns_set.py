from pyns.ns_universe import NSuniverse
#----
from re import findall
from ast import literal_eval

class NSset:
    """
    Class that defines a neutrosophic set over a given universe
    ----------------------------------------------------------------------------------
    author: Giorgio Nordo - Dipartimento MIFT. Università di Messina, Italy
    www.nordo.it   |  giorgio.nordo@unime.it
    """

    degreename = ["membership", "indeterminacy", "non-membership"]   # variabile di classe

    # costruttore
    def __init__(self, *args):
        """
        Generic constructor of an empty neutrosophic set defined over a universe
        or copied by another object neutrosophic set.
        ----
        Parameters:
        - args: generic argument which can be an element referable to an object together universe
                (list, tuple, string, list of values, universe set object)
                or a pair constituted by an element attributable to a universe set
                and a list of tuples of real values representing the membership degrees of the various elements
        """
        neutrosophicset = dict()    # dizionario di liste che contiene i valori dell'insieme neutrosofico
        #--------------------
        length = len(args)
        if length == 1:
            element = args[0]
            if type(element) in [list, tuple, str, NSuniverse]:   # viene passato un oggetto riconducibile a universo e generato un insieme neutrosofico vuoto
                universe = NSuniverse(element)   # altri tipi vengono convertiti in oggetto universo
                for e in universe.get():
                    neutrosophicset[e] = [0,0,1]  # lista di tre elementi corrispondenti a appartenenza, indeterminatezza, non appartenenza
            elif type(element) == NSset:
                universe = element.getUniverse() # viene copiato un oggetto insieme neutrosofico
                for e in universe:
                    neutrosophicset[e] = element.getElement(e)
            else:
                raise ValueError("value not compatible with the type universe set")
        elif length == 2:
            # ricava i due parametri (insieme universo e lista dei valori)
            nset = NSset(args[0])  # utilizza lo stesso costruttore
            universe = nset.getUniverse()  # preleva l'insieme universo come lista
            values = args[1]   # preleva la lista dei valori
            if type(values) not in [list, tuple, str]:
                raise ValueError("the second parameter of the constructor method must contain a list of triples of real numbers")
            if type(values) != str and len(values) != len(universe):
                raise IndexError("the number of value triples does not correspond with the number of elements")
            # tratta il caso in cui il secondo parametro è una stringa
            if type(values) == str:   # preleva le triple (liste o tuple) dalla stringa fornita come secondo parametro
                pattern = r'\[.*?\]|\(.*?\)'   # usa le espressioni regolari per isolare le triple
                str_list = findall(pattern, values)   # usa il modulo ast per convertire le strutture
                tpl_list = [tuple(literal_eval(s)) for s in str_list]
                nset = NSset(universe,tpl_list)  # utilizza lo stesso costruttore
                neutrosophicset = nset.get()
            else:   # tratta il caso in cui il secondo parametro è una lista o una tupla
                for i in range(len(universe)):
                    elem = universe[i]
                    t = values[i]  # prende la tripla della lista corrispondente all'elemento e secondo lo stesso ordine
                    if type(t) not in [tuple,list] or len(t) !=3:
                        raise IndexError("the second parameter of the constructor method must contain only triple")
                    t = [float(t[j]) for j in range(3)]
                    for j in range(3):   # controlla che i valori della tripla siano compatibili
                        if not 0 <= t[j] <= 1:
                            raise ValueError(f"incompatible {self.degreename[j]} degree value")
                    neutrosophicset[elem] = t
        else:
            raise IndexError("the number of parameters do not match those of the constructor method")
        # memorizza i valori ottenuti nelle proprietà dell'oggetto
        self.__universe = NSuniverse(universe)
        self.__neutrosophicset = neutrosophicset


    #------------------------------------------------------------------------------------

    # metodo privato che assegna l'i-esimo (i=0,1,2) grado dell'elemento u
    def __setDegree(self, u, i, r):
        """ private method that returns the i-th degree (for i=0,1,2) of a given element
        of the current neutrosophic set.
        ----
        Parameters:
        - u: element of the universe
        - i: index of the degree (i=0: membership, i=1: indeterminacy, i=2: non-membership
        . r: value of the i-th degree
        """
        u = str(u)  # converte in stringa per confrontarla con gli elementi dell'universo che è lista di stringhe
        if u not in self.getUniverse():
            raise IndexError('non-existent element')
        r = float(r)
        if not (0 <= r <= 1):
            raise ValueError(f"incompatible {self.degreename[i]} degree value")
        self.__neutrosophicset[u][i] = r


    #------------------------------------------------------------------------------------


    # assegna il grado di appartenenza ad un elemento
    def setMembership(self, u, mu):
        """
        Assign the membership degree to a specific element of the neutrosophic set.
        ----
        Parameters:
        - u: element of the universe
        - mu: value of the membership degree
        """
        self.__setDegree(u, 0, mu)


    # assegna il grado di indeterminatezza ad un elemento
    def setIndeterminacy(self, u, sigma):
        """
        Assign the indeterminacy degree to a specific element of the neutrosophic set.
        ----
        Parameters:
        - u: element of the universe
        - sigma: value of the indeterminacy degree
        """
        self.__setDegree(u, 1, sigma)


    # assegna il grado di non appartenenza ad un elemento
    def setNonMembership(self, u, omega):
        """
        Assign the non membership degree to a specific element of the neutrosophic set.
        ----
        Parameters:
        - u: element of the universe
        - omega: value of the non membership degree
        """
        self.__setDegree(u, 2, omega)

    #------------------------------------------------------------------------------------

    # assegna la tripla di appartenenza, indeterminatezza e non appartenenza ad un elemento
    def setElement(self, u, triple):
        """
        Assign simultaneously the membership, indeterminacy and non-membership degree
        to a specific element of the neutrosophic set.
        ----
        Parameters:
        - u: element of the universe
        - triple: string, list or tuple of membership, indeterminacy and non-membership degree
        """

        if type(triple) == str:   # se il parametro è una stringa lo converte in lista
            sostituz = { "(":"", ")":"", ",":" ", ";":" " }
            for k in sostituz:
                triple = triple.replace(k, sostituz[k])
            triple = triple.split()
        else:
            triple = list(triple)   # converte in lista in caso fosse una tupla
        if len(triple) != 3:
            raise ValueError('error in the number of parameters passed')
        triple = [float(e) for e in triple]   # i.e. (mu, sigma, omega)
        for i in range(3):
            self.__setDegree(u, i, triple[i])

    #------------------------------------------------------------------------------------

    # metodo che restituisce l'universo come lista
    def getUniverse(self):
        """
        Method that returns the universe of the neutrosophic set as a list of string.
        ---
        Returns: list of the elements of the universe
        """
        return self.__universe.get()


    # metodo che restituisce l'intero insieme neutrosofico come dizionario
    def get(self):
        """ method that returns the dictionary containg the degrees of each element
        """
        return self.__neutrosophicset


    # restituisce la lista dei gradi di appartenenza, indeterminazione e non appartenenza
    def getElement(self, u):
        """
        Obtain the three degrees of membership of a given element of the current neutrosophic set.
        ----
        Parameters:
        - u: element of the universe
        ----
        Returns: the list of floats containing the three degrees (membership, indeterminacy and non-membership)
        of the element u
        """
        u = str(u)  # converte in stringa per confrontarla con gli elementi dell'universo che è lista di stringhe
        if u not in self.getUniverse():
            raise IndexError('non-existent element')
        return self.__neutrosophicset[u]

    #------------------------------------


    # metodo privato che restituisce l-i-esimo (i=0,1,2) grado dell'elemento u
    def __getDegree(self, u, i):
        """ private method that returns the i-th degree (for i=0,1,2) of a given element
        of the current neutrosophic set.
        ----
        Parameters:
        - u: element of the universe
        - i: index of the degree (i=0: membership, i=1: indeterminacy, i=2: non-membership
        ----
        Returns: i-th degree of u
        """
        u = str(u)  # converte in stringa per confrontarla con gli elementi dell'universo che è lista di stringhe
        if u not in self.getUniverse():
            raise IndexError('non-existent element')
        return self.__neutrosophicset[u][i]


    #------------------------------------


    # restituisce il grado di appartenenza
    def getMembership(self, u):
        """
        Obtain the degree of membership of a given element of the current neutrosophic set.
        ----
        Parameters:
        - u: element of the universe
        ----
        Returns: degree of membership of u
        """
        return self.__getDegree(u, 0)


    # restituisce il grado di indeterminazione
    def getIndeterminacy(self, u):
        """
        Obtain the degree of indeterminacy of a given element of the current neutrosophic set.
        ----
        Parameters:
        - u: element of the universe
        ----
        Returns: degree of indeterminacy of u
        """
        return self.__getDegree(u, 1)


    # restituisce il grado di non appartenenza
    def getNonMembership(self, u):
        """
        Obtain the degree of non-membership of a given element of the current neutrosophic set.
        ----
        Parameters:
        - u: element of the universe
        ----
        Returns: degree of non-membership of u
        """
        return self.__getDegree(u, 2)


    #------------------------------------------------------------------------------------


    # pone l'insieme neutrosofico uguale all'insieme neutrosofico vuoto
    def setEmpty(self):
        """
        Makes the neutrosophic set equal to the null neutrosophic set.
        """
        for e in self.__universe.get():
            self.__neutrosophicset[e] = [0, 0, 1]


    # pone l'insieme neutrosofico uguale all'insieme neutrosofico assoluto
    def setAbsolute(self):
        """
        Makes the neutrosophic set equal to the absolute neutrosophic set.
        """
        for e in self.__universe.get():
            self.__neutrosophicset[e] = [1, 1, 0]


    #------------------------------------------------------------------------------------


    # metodo che restituisce la cardinalità (il numero di elementi) dell'insieme neutrosofico
    def cardinality(self):
        """
        Method that returns the cardinality (the number of elements) of the neutrosophic set
        ----
        Returns: the number of elements of the current neurosophic set
        """
        return self.__universe.cardinality()


    #------------------------------------------------------------------------------------

    # restituisce true se l'insieme neutrosofico corrente è contenuto in quello
    # passato come parametro
    def isNSsubset(self, nset):
        """
        Checks if the current NS set is contained in the second one passed as parameter.
        ----
        Parameters:
        - nset: second neutrosophic set
        ----
        Returns: True if the current neutrosophic set is neutrosofically contained in the second one
        """
        if self.getUniverse() != nset.getUniverse():
            raise ValueError("the two neutrosophic sets cannot be defined on different universe sets")
        if self.getUniverse() != nset.getUniverse():
            return False
        else:
            result = True
            for e in self.getUniverse():
                (muA, sigmaA, omegaA) = self.getElement(e)
                (muB, sigmaB, omegaB) = nset.getElement(e)
                if (muA > muB) or (sigmaA > sigmaB) or (omegaA < omegaB):
                    result = False
                    break
            return result


    # restituisce true se l'insieme neutrosofico corrente contiene in quello
    # passato come parametro
    def isNSsuperset(self, nset):
        """
        Checks if the current NS set contains the second one passed as parameter.
        ----
        Parameters:
        - nset second neutrosophic set
        ----
        Returns: True if the current neutrosophic set neutrosofically contains the second one
        """
        if self.getUniverse() != nset.getUniverse():
            raise ValueError("the two neutrosophic sets cannot be defined on different universe sets")
        return nset.isNSsubset(self)


    #------------------------------------------------------------------------------------

    # metodo privato per operazione generica su oggetti di tipo insieme neutrosofico
    def __NSoperation(self, nset, fm, fs, fo):
        """ private method that returns the neutrosophic set obtained by applying the neutrosophic
        operation of the current neutrosophic set with the second one passed as parameter
        by three functions applied to their membership, indeterminacy and non-membership degrees respectively.
        Parameters:
        - nset second neutrosophic set
        - fm, fs, fo first, second and third function
        ----
        Returns: the neutrosophic set obtained by the current one with the second one by
        applying the functions fm, fs and fo to their respective degrees
        """
        if self.getUniverse() != nset.getUniverse():
            raise ValueError("the two neutrosophic sets cannot be defined on different universe sets")
        if callable(fm) == False or callable(fs) == False or callable(fo) == False:
            raise  ValueError("the last three parameters must be functions")
        C = NSset(self.__universe)
        for e in self.getUniverse():
            (muA, sigmaA, omegaA) = self.getElement(e)
            (muB, sigmaB, omegaB) = nset.getElement(e)
            #----
            triple = [fm(muA, muB), fs(sigmaA, sigmaB), fo(omegaA, omegaB)]   # i.e. (muC, sigmaC, omegaC)
            C.setElement(e, triple)
        return C


    # unione neutrosofica
    def NSunion(self, nset):
        """ Calculates and returns the neutrosophic union of the current set with the second one
        passed as parameter.
        ----
        Parameters:
        - nset second neutrosophic set
        ----
        Returns: the neutrosophic union of the current neutrosophic set with the second one
        """
        C = self.__NSoperation(nset, max, max, min)
        return C


    # intersezione neutrosofica
    def NSintersection(self, nset):
        """ Calculates and returns the neutrosophic intersection of the current set with the second one
        passed as parameter.
        ----
        Parameters:
        - nset second neutrosophic set
        ----
        Returns: the neutrosophic intersection of the current neutrosophic set with the second one
        """
        C = self.__NSoperation(nset, min, min, max)
        return C


    #------------------------------------------------------------------------------------

    # verifica se un insieme neutrosofico è disgiunto da un altro
    def isNSdisjoint(self, nset):
        """ Checks if the current set is neutrosophically disjoint with the second one
        passed as parameter.
        ----
        Parameters:
        - nset second neutrosophic set
        Returns: True if the current neutrosophic set is neutrosophically disjoint from the second one
        """
        nsempty = NSset(self.__universe)  # prepare the empty neutrosophic set
        disjoint = self.NSintersection(nset) == nsempty
        return disjoint


    #------------------------------------------------------------------------------------


    # complementare neutrosofico
    def NScomplement(self):
        """ Calculates and returns the neutrosophic complement of the current neutrosophic set.
        ----
        Returns: the neutrosophic complement of the current neutrosophic set
        """
        C = NSset(self.__universe)
        for e in self.getUniverse():
            (muA, sigmaA, omegaA) = self.getElement(e)
            #----
            triple = [omegaA, 1 - sigmaA, muA]    # i.e. (muC, sigmaC, omegaC)
            C.setElement(e, triple)
        return C


    # differenza neutrosofica
    def NSdifference(self, nset):
        """ Calculates and returns the neutrosophic difference of the current set with the second one
        passed as parameter.
        ----
        Parameters:
        - nset second neutrosophic set
        ----
        Returns: the neutrosophic difference of the current neutrosophic set with the second one
        """
        if self.getUniverse() != nset.getUniverse():
            raise ValueError("the two neutrosophic sets cannot be defined on different universe sets")
        C = NSset(self.__universe)
        for e in self.getUniverse():
            (muA, sigmaA, omegaA) = self.getElement(e)
            (muB, sigmaB, omegaB) = nset.getElement(e)
            #----
            triple = [min(muA, omegaB), min(sigmaA, 1 - sigmaB), max(omegaA, muB)]   # i.e. (muC, sigmaC, omegaC)
            C.setElement(e, triple)
        return C


    #------------------------------------------------------------------------------------

    # confronta due insiemi neutrosofici col metodo speciale __eq__
    # sovraccaricando l'operatore di uguaglianza == e restituisce True se sono uguali
    def __eq__(self, nset):
        """ Checks if the current NS set is equal to another one.
        ----
        Parameters:
        - nset second neutrosophic set
        ----
        Returns: True if the current neutrosophic set neutrosofically coincides with the second one
        """
        if self.getUniverse() != nset.getUniverse():
            raise ValueError("the two neutrosophic sets cannot be defined on different universe sets")
        equal = self.isNSsubset(nset) and nset.isNSsubset(self)
        return equal


    # confronta due insiemi neutrosofici col metodo speciale __ne__
    # sovraccaricando l'operatore di non uguaglianza != e restituisce True se sono diversi
    def __ne__(self, nset):
        """ Checks if the current NS set is different from another one.
        ----
        Parameters:
        - nset second neutrosophic set
        ----
        Returns: True if the current neutrosophic set neutrosofically is different from the second one
        """
        if self.getUniverse() != nset.getUniverse():
            raise ValueError("the two neutrosophic sets cannot be defined on different universe sets")
        different = not (self == nset)
        return different


    #--------------------------

    # operatore unione (+) con overloading sul metodo __add__
    def __add__(self, nset):
        """ neutrosophic union
        """
        return self.NSunion(nset)


    # operatore intersezione (&) con overloading sul metodo __and__
    def __and__(self, nset):
        """ neutrosophic intersection
        """
        return self.NSintersection(nset)


    # operatore complementare (~ = tilde) con overloading sul metodo __invert__
    def __invert__(self):
        """ neutrosophic complement
        """
        return self.NScomplement()


    # operatore differenza (-) con overloading sul metodo __sub__
    def __sub__(self, nset):
        """ neutrosophic difference
        """
        return self.NSdifference(nset)


    # operatore sottoinsieme (<=) con overloading sul metodo __le__
    def __le__(self, nset):
        """ neutrosophic subset
        """
        return self.isNSsubset(nset)


    # operatore sovrainsieme (>=) con overloading sul metodo __ge__
    def __ge__(self, nset):
        """ neutrosophic superset
        """
        return self.isNSsuperset(nset)


    #------------------------------------------------------------------------------------


    # restituisce l'insieme neutrosofico come stringa col metodo speciale __str__
    def __str__(self):
        """ Method that returns the neutrosophic set in string format for the user.
        ----
        Returns: string containing a table representing the degree of membership, indeterminacy and
                 non-membership of every element of the neutrosophic set
        """
        (dashes, elemwidth, valwidth) = ("-"*64, 10, 14)
        s = "\n            |   membership   |  indeterminacy | non-membership |\n" + dashes + "\n"
        
        for e in self.getUniverse():
            (mu, sigma, omega) = self.getElement(e)
            s += f" {str(e):{elemwidth}} | {mu:{valwidth}} | {sigma:{valwidth}} | {omega:{valwidth}} |\n"
        s += dashes + "\n"
        return s



    # restituisce la rappresentazione insieme neutrosofico come stringa col metodo speciale __repr__
    # che viene implicitamente utilizzata nelle altre classi
    def __repr__(self):
        """ Method that returns the neutrosophic set in string format for other implementations
        (e.g., for use in other classes).
        ----
        Returns: a detailed representation of the current neutrosophic set
        """
        return f"Neutrosophic set: {str(self)}"