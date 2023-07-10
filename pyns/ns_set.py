from pyns.ns_universe import NSuniverse

class NSset:
    """
    Class that defines a neutrosophic set over a given universe
    ----------------------------------------------------------------------------------
    author: Giorgio Nordo - Dipartimento MIFT. Università di Messina, Italy
    www.nordo.it   |  giorgio.nordo@unime.it
    """

    # costruttore
    def __init__(self, elemento):
        """
        Generic constructor of an empty neutrosophic set defined over a universe
        or copied by another object neutrosophic set.
        ----
        Parameters:
        - elemento: element on which the neutrosophic set is defined
          (can be a universe set or a neutrosophic set object to be copied)
        """
        insiemeneutrosofico = dict()
        if type(elemento) == NSuniverse:   # viene passato un universo e generato un insieme neutrosofico vuoto
            universo = elemento
            for e in elemento.get():
                insiemeneutrosofico[e] = [0,0,1]   # lista di tre elementi corrispondenti a appartenenza, indeterminatezza, non appartenenza
        elif type(elemento) == NSset:    # viene copiato un oggetto insieme neutrosofico
            universo = elemento.getUniverse()
            for e in universo:
                insiemeneutrosofico[e] = elemento.getElement(e)
        self.__universo = NSuniverse(universo)
        self.__insiemeneutrosofico = insiemeneutrosofico

    #------------------------------------------------------------------------------------

    # assegna la tripla di appartenenza, indeterminatezza e non appartenenza ad un elemento
    def setElement(self, u, tripla):
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
        if type(tripla) == str:   # se il parametro è una stringa lo converte in lista
            sostituz = { "(":"", ")":"", ",":" ", ";":" " }
            for k in sostituz:
                tripla = tripla.replace(k, sostituz[k])
            tripla = tripla.split()
        else:
            tripla = list(tripla)   # converte in lista in caso fosse una tupla
        if len(tripla) != 3:
            raise ValueError('error in the number of parameters passed')
        tripla = [float(e) for e in tripla]
        (mu, sigma, omega) = tripla
        if not (0 <= mu <= 1):
            raise ValueError("incompatible membership degree value")
        if not (0 <= sigma <= 1):
            raise ValueError("incompatible indeterminacy degree value")
        if not (0 <= omega <= 1):
            raise ValueError("incompatible non-membership degree value")
        # assert 0 <= mu <= 1
        # assert 0 <= sigma <= 1
        # assert 0 <= omega <= 1
        self.__insiemeneutrosofico[u] = tripla


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
        self.__insiemeneutrosofico[u][0] = mu


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
        self.__insiemeneutrosofico[u][1] = sigma


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
        self.__insiemeneutrosofico[u][2] = omega


    #------------------------------------------------------------------------------------


    # metodo che restituisce l'universo come lista
    def getUniverse(self):
        """
        Method that returns the universe of the neutrosophic set as a list of string.
        ---
        Returns: list of the elements of the universe
        """
        return self.__universo.get()


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
        return self.__insiemeneutrosofico[u]


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
        u = str(u)  # converte in stringa per confrontarla con gli elementi dell'universo che è lista di stringhe
        if u not in self.getUniverse():
            raise IndexError('non-existent element')
        return self.__insiemeneutrosofico[u][0]


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
        u = str(u)  # converte in stringa per confrontarla con gli elementi dell'universo che è lista di stringhe
        if u not in self.getUniverse():
            raise IndexError('non-existent element')
        return self.__insiemeneutrosofico[u][1]


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
        u = str(u)  # converte in stringa per confrontarla con gli elementi dell'universo che è lista di stringhe
        if u not in self.getUniverse():
            raise IndexError('non-existent element')
        return self.__insiemeneutrosofico[u][2]

    #------------------------------------------------------------------------------------

    # pone l'insieme neutrosofico uguale all'insieme neutrosofico vuoto
    def setEmpty(self):
        """
        Makes the neutrosophic set equal to the null neutrosophic set.
        """
        for e in self.__universo.get():
            self.__insiemeneutrosofico[e] = [0, 0, 1]


    # pone l'insieme neutrosofico uguale all'insieme neutrosofico assoluto
    def setAbsolute(self):
        """
        Makes the neutrosophic set equal to the absolute neutrosophic set.
        """
        for e in self.__universo.get():
            self.__insiemeneutrosofico[e] = [1, 1, 0]


    #------------------------------------------------------------------------------------

    # restituisce true se l'insieme neutrosofico corrente è contenuto in quello
    # passato come parametro
    def isNSsubset(self, nsins):
        """
        Checks if the current NS set is contained in the second one passed as parameter.
        ----
        Parameters:
        - nsins: second neutrosophic set
        ----
        Returns: True if the current neutrosophic set is neutrosofically contained in the second one
        """
        if self.getUniverse() != nsins.getUniverse():
            return False
        else:
            risultato = True
            for e in self.getUniverse():
                (muA, sigmaA, omegaA) = self.getElement(e)
                (muB, sigmaB, omegaB) = nsins.getElement(e)
                if (muA > muB) or (sigmaA > sigmaB) or (omegaA < omegaB):
                    risultato = False
                    break
            return risultato


    # restituisce true se l'insieme neutrosofico corrente contiene in quello
    # passato come parametro
    def isNSsuperset(self, nsins):
        """
        Checks if the current NS set contains the second one passed as parameter.
        ----
        Parameters:
        - nsins second neutrosophic set
        ----
        Returns: True if the current neutrosophic set neutrosofically contains the second one
        """
        return nsins.isNSsubset(self)


    #------------------------------------------------------------------------------------

    # confronta due insiemi neutrosofici col metodo speciale __eq__
    # sovraccaricando l'operatore di uguaglianza == e restituisce True se sono uguali
    def __eq__(self, nsins):
        """ Checks if the current NS set is equal to another one.
        ----
        Parameters:
        - nsins second neutrosophic set
        ----
        Returns: True if the current neutrosophic set neutrosofically coincides with the second one
        """
        uguali = self.isNSsubset(nsins) and nsins.isNSsubset(self)
        return uguali


    # confronta due insiemi neutrosofici col metodo speciale __ne__
    # sovraccaricando l'operatore di non uguaglianza != e restituisce True se sono diversi
    def __ne__(self, nsins):
        """ Checks if the current NS set is different from another one.
        ----
        Parameters:
        - nsins second neutrosophic set
        ----
        Returns: True if the current neutrosophic set neutrosofically is different from the second one
        """
        differenti = not (self == nsins)
        return differenti


    #------------------------------------------------------------------------------------

    # unione neutrosofica
    def NSunion(self, nsins):
        """ Calculates and returns the neutrosophic union of the current set with the second one
        passed as parameter.
        ----
        Parameters:
        - nsins second neutrosophic set
        ----
        Returns: the neutrosophic union of the current neutrosophic set with the second one
        """
        C = NSset(self.__universo)
        for e in self.getUniverse():
            (muA, sigmaA, omegaA) = self.getElement(e)
            (muB, sigmaB, omegaB) = nsins.getElement(e)
            #----
            (muC, sigmaC, omegaC) = (max(muA, muB), max(sigmaA, sigmaB), min(omegaA, omegaB))
            tripla = [muC, sigmaC, omegaC]
            C.setElement(e, tripla)
        return C


    # intersezione neutrosofica
    def NSintersection(self, nsins):
        """ Calculates and returns the neutrosophic intersection of the current set with the second one
        passed as parameter.
        ----
        Parameters:
        - nsins second neutrosophic set
        ----
        Returns: the neutrosophic intersection of the current neutrosophic set with the second one
        """
        C = NSset(self.__universo)
        for e in self.getUniverse():
            (muA, sigmaA, omegaA) = self.getElement(e)
            (muB, sigmaB, omegaB) = nsins.getElement(e)
            #----
            (muC, sigmaC, omegaC) = (min(muA, muB), min(sigmaA, sigmaB), max(omegaA, omegaB))
            tripla = [muC, sigmaC, omegaC]
            C.setElement(e, tripla)
        return C


    # complementare neutrosofico
    def NScomplement(self):
        """ Calculates and returns the neutrosophic complement of the current neutrosophic set.
        ----
        Returns: the neutrosophic complement of the current neutrosophic set
        """
        C = NSset(self.__universo)
        for e in self.getUniverse():
            (muA, sigmaA, omegaA) = self.getElement(e)
            #----
            (muC, sigmaC, omegaC) = (omegaA, 1 - sigmaA, muA)
            tripla = [muC, sigmaC, omegaC]
            C.setElement(e, tripla)
        return C


    # differenza neutrosofica
    def NSdifference(self, nsins):
        """ Calculates and returns the neutrosophic difference of the current set with the second one
        passed as parameter.
        ----
        Parameters:
        - nsins second neutrosophic set
        ----
        Returns: the neutrosophic difference of the current neutrosophic set with the second one
        """
        C = NSset(self.__universo)
        for e in self.getUniverse():
            (muA, sigmaA, omegaA) = self.getElement(e)
            (muB, sigmaB, omegaB) = nsins.getElement(e)
            #----
            (muC, sigmaC, omegaC) = (min(muA, omegaB), min(sigmaA, 1 - sigmaB), max(omegaA, muB))
            tripla = [muC, sigmaC, omegaC]
            C.setElement(e, tripla)
        return C


    #------------------------------------------------------------------------------------


    # operatore unione (+) con overloading sul metodo __add__
    def __add__(self, nsins):
        return self.NSunion(nsins)


    # operatore intersezione (&) con overloading sul metodo __and__
    def __and__(self, nsins):
        return self.NSintersection(nsins)


    # operatore complementare (~ = tilde) con overloading sul metodo __invert__
    def __invert__(self):
        return self.NScomplement()


    # operatore differenza (-) con overloading sul metodo __sub__
    def __sub__(self, nsins):
        return self.NSdifference(nsins)


    # operatore sottoinsieme (<=) con overloading sul metodo __le__
    def __le__(self, nsins):
        return self.isNSsubset(nsins)


    # operatore sovrainsieme (>=) con overloading sul metodo __ge__
    def __ge__(self, nsins):
        return self.isNSsuperset(nsins)


    #------------------------------------------------------------------------------------

    # verifica se un insieme neutrosofico è disgiunto da un altro
    def isNSdisjoint(self, nsins):
        """ Checks if the current set is neutrosophically disjoint with the second one
        passed as parameter.
        ----
        Parameters:
        - nsins second neutrosophic set
        Returns: True if the current neutrosophic set is neutrosophically disjoint from the second one
        """
        nsvuoto = NSset(self.__universo)
        disgiunti = self.NSintersection(nsins) == nsvuoto
        return disgiunti

    #------------------------------------------------------------------------------------


    # restituisce l'insieme neutrosofico come stringa col metodo speciale __str__
    def __str__(self):
        """ Method that returns the neutrosophic set in string format for the user.
        ----
        Returns: string containing a table representing the degree of membership, indeterminacy and
        non-membership of every element of the neutrosophic set
        """
        barra = "-"*64
        s = "\n            |   membership   |  indeterminacy | non-membership |\n" + barra + "\n"
        for e in self.getUniverse():
            (mu, sigma, omega) = self.getElement(e)
            s += f" {str(e):10} | {mu:14} | {sigma:14} | {omega:14} |\n"
        s += barra + "\n"
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