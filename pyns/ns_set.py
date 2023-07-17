from pyns.ns_universe import NSuniverse

class NSset:
    """
    Class that defines a neutrosophic set over a given universe
    ----------------------------------------------------------------------------------
    author: Giorgio Nordo - Dipartimento MIFT. Università di Messina, Italy
    www.nordo.it   |  giorgio.nordo@unime.it
    """

    # costruttore
    def __init__(self, element):
        """
        Generic constructor of an empty neutrosophic set defined over a universe
        or copied by another object neutrosophic set.
        ----
        Parameters:
        - elemento: element on which the neutrosophic set is defined
          (can be a universe set or a neutrosophic set object to be copied)
        """
        neutrosophicset = dict()    # dizionario di liste che contiene i values dell'insieme neutrosofico
        #--------------------
        if type(element) == NSuniverse:   # viene passato un universo e generato un insieme neutrosofico vuoto
            universe = element
            for e in element.get():
                neutrosophicset[e] = [0,0,1]   # lista di tre elementi corrispondenti a appartenenza, indeterminatezza, non appartenenza
        elif type(element) == NSset:    # viene copiato un oggetto insieme neutrosofico
            universe = element.getUniverse()
            for e in universe:
                neutrosophicset[e] = element.getElement(e)
        self.__universe = NSuniverse(universe)
        self.__neutrosophicset = neutrosophicset

    #------------------------------------------------------------------------------------

    # assegna la tripla di appartenenza, indeterminatezza e non appartenenza ad un elemento
    def setElement(self, u, triple):
        """
        Assign simultaneously the membership, indeterminacy and non-membership degree
        to a specific element of the neutrosophic set.
        ----
        Parameters:
        - u: element of the universe
        - tripla: string, list or tuple of membership, indeterminacy and non-membership degree
        """
        u = str(u)   # converte in stringa per confrontarla con gli elementi dell'universo che è lista di stringhe
        if u not in self.getUniverse():
            raise IndexError('non-existent element')
        if type(triple) == str:   # se il parametro è una stringa lo converte in lista
            sostituz = { "(":"", ")":"", ",":" ", ";":" " }
            for k in sostituz:
                triple = triple.replace(k, sostituz[k])
            triple = triple.split()
        else:
            triple = list(triple)   # converte in lista in caso fosse una tupla
        if len(triple) != 3:
            raise ValueError('error in the number of parameters passed')
        triple = [float(e) for e in triple]
        (mu, sigma, omega) = triple
        if not (0 <= mu <= 1):
            raise ValueError("incompatible membership degree value")
        if not (0 <= sigma <= 1):
            raise ValueError("incompatible indeterminacy degree value")
        if not (0 <= omega <= 1):
            raise ValueError("incompatible non-membership degree value")
        # assert 0 <= mu <= 1
        # assert 0 <= sigma <= 1
        # assert 0 <= omega <= 1
        self.__neutrosophicset[u] = triple


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
        u = str(u)  # converte in stringa per confrontarla con gli elementi dell'universo che è lista di stringhe
        if u not in self.getUniverse():
            raise IndexError('non-existent element')
        mu = float(mu)
        if not (0 <= mu <= 1):
            raise ValueError("incompatible membership degree value")
        self.__neutrosophicset[u][0] = mu


    # assegna il grado di indeterminatezza ad un elemento
    def setIndeterminacy(self, u, sigma):
        """
        Assign the indeterminacy degree to a specific element of the neutrosophic set.
        ----
        Parameters:
        - u: element of the universe
        - sigma: value of the indeterminacy degree
        """
        u = str(u)  # converte in stringa per confrontarla con gli elementi dell'universo che è lista di stringhe
        if u not in self.getUniverse():
            raise IndexError('non-existent element')
        sigma = float(sigma)
        if not (0 <= sigma <= 1):
            raise ValueError("incompatible indeterminacy degree value")
        self.__neutrosophicset[u][1] = sigma


    # assegna il grado di non appartenenza ad un elemento
    def setNonMembership(self, u, omega):
        """
        Assign the non membership degree to a specific element of the neutrosophic set.
        ----
        Parameters:
        - u: element of the universe
        - omega: value of the non membership degree
        """
        u = str(u)  # converte in stringa per confrontarla con gli elementi dell'universo che è lista di stringhe
        if u not in self.getUniverse():
            raise IndexError('non-existent element')
        omega = float(omega)
        if not (0 <= omega <= 1):
            raise ValueError("incompatible non-membership degree value")
        self.__neutrosophicset[u][2] = omega


    #------------------------------------------------------------------------------------


    # metodo che restituisce l'universo come lista
    def getUniverse(self):
        """
        Method that returns the universe of the neutrosophic set as a list of string.
        ---
        Returns: list of the elements of the universe
        """
        return self.__universe.get()


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
        """ private method that returns the i-th degree (for i=0,1,2) of a given element of the current neutrosophic set
            i = 0 : membership
            i = 1 : indeterminacy
            i = 2 : non-membership
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
        return nset.isNSsubset(self)


    #------------------------------------------------------------------------------------

    # confronta due insiemi neutrosofici col metodo speciale __eq__
    # sovraccaricando l'operatore di uguaglianza == e restituisce True se sono uguali
    def __eq__(self, nsins):
        """ Checks if the current NS set is equal to another one.
        ----
        Parameters:
        - nset second neutrosophic set
        ----
        Returns: True if the current neutrosophic set neutrosofically coincides with the second one
        """
        equal = self.isNSsubset(nsins) and nsins.isNSsubset(self)
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
        different = not (self == nset)
        return different


    #------------------------------------------------------------------------------------

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
        C = NSset(self.__universe)
        for e in self.getUniverse():
            (muA, sigmaA, omegaA) = self.getElement(e)
            (muB, sigmaB, omegaB) = nset.getElement(e)
            #----
            triple = [max(muA, muB), max(sigmaA, sigmaB), min(omegaA, omegaB)]   # i.e. (muC, sigmaC, omegaC)
            C.setElement(e, triple)
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
        C = NSset(self.__universe)
        for e in self.getUniverse():
            (muA, sigmaA, omegaA) = self.getElement(e)
            (muB, sigmaB, omegaB) = nset.getElement(e)
            #----
            triple = [min(muA, muB), min(sigmaA, sigmaB), max(omegaA, omegaB)]  # i.e. (muC, sigmaC, omegaC)
            C.setElement(e, triple)
        return C


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
        C = NSset(self.__universe)
        for e in self.getUniverse():
            (muA, sigmaA, omegaA) = self.getElement(e)
            (muB, sigmaB, omegaB) = nset.getElement(e)
            #----
            triple = [min(muA, omegaB), min(sigmaA, 1 - sigmaB), max(omegaA, muB)]   # i.e. (muC, sigmaC, omegaC)
            C.setElement(e, triple)
        return C


    #------------------------------------------------------------------------------------


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


    # restituisce l'insieme neutrosofico come stringa col metodo speciale __str__
    def __str__(self):
        """ Method that returns the neutrosophic set in string format for the user.
        ----
        Returns: string containing a table representing the degree of membership, indeterminacy and
                 non-membership of every element of the neutrosophic set
        """
        dashes = "-"*64
        s = "\n            |   membership   |  indeterminacy | non-membership |\n" + dashes + "\n"
        for e in self.getUniverse():
            (mu, sigma, omega) = self.getElement(e)
            s += f" {str(e):10} | {mu:14} | {sigma:14} | {omega:14} |\n"
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