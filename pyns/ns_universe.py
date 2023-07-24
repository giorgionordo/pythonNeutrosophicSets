class NSuniverse:
    """
    Class defining a universe set for neutrosophic sets
    ----------------------------------------------------------------------------------
    author: Giorgio Nordo - Dipartimento MIFT, Università di Messina, Italy
    www.nordo.it   |  giorgio.nordo@unime.it
    """

    # costruttore
    def __init__(self, *args):
        """
        Generic constructor of a universe which accepts list, tuple, string,
        list of af values, or other universe object.
        ----
        Parameters:
        - args: generic argument (list, tuple, string, list of values or an universe object)
        """
        universe = list()   # lista di stringhe
        #--------------------
        length = len(args)
        if length == 1:
            elem = args[0]
            if type(elem) in [list, tuple]:
                universe = [str(e) for e in elem]
            elif type(elem) == NSuniverse:
                universe = elem.get()
            elif type(elem) == str:
                sostituz = { "{":"", "}":"", "(":"", ")":"", "[":"", "]":"",
                             ",":" ", ";":" " }
                for k in sostituz:
                    elem = elem.replace(k, sostituz[k])
                universe = elem.split()
            else:
                universe = [str(elem)]
        elif length > 1:   # se la lunghezza è maggiore di 1
            for i in range(length):
                universe.append(str(args[i]))
        # memorizza il valore ottenuto nella proprietà dell'oggetto
        self.__universe = universe


    #------------------------------------------------------------------------------------

    # restituisce l'universo come lista di stringhe
    def get(self):
        """
        Method that returns the universe as a list of strings.
        ----
        Returns: list of the elements of the universe
        """
        return self.__universe


    # metodo che restituisce la cardinalità (il numero di elementi) dell'universo
    def cardinality(self):
        """
        Method that returns the cardinality (the number of elements) of the universe set
        ----
        Returns: the number of elements of the current universe set
        """
        return len(self.__universe)


    #------------------------------------------------------------------------------------

    # confronta due insiemi universo col metodo speciale __eq__
    # sovraccaricando l'operatore di uguaglianza == e restituisce True se sono uguali
    def __eq__(self, unv):
        """ Checks if the current universe is equal to another one.
        ----
        Returns: True if the universes are equal
        """
        equal = (self.__universe == unv.get())
        return equal


    # confronta due insiemi universo col metodo speciale __ne__
    # sovraccaricando l'operatore di non uguaglianza != e restituisce True se sono diversi
    def __ne__(self, unv):
        """ Checks if the current universe is different from another one.
        ----
        Returns: True if the universes are different
        """
        different = not (self == unv)
        return different


    #------------------------------------------------------------------------------------


    # restituisce l'universo come stringa col metodo speciale __str__
    def __str__(self):
        """ Method that returns the universe in string format for the user.
        ----
        Returns: string containing a list of the elements of the current universe set
        """
        list_string_elements = [str(e) for e in self.__universe]
        s = "{ " + ", ".join(list_string_elements) + " }"
        return s


    # restituisce la rappresentazione universo come stringa col metodo speciale __repr__
    # che viene implicitamente utilizzata nelle altre classi
    def __repr__(self):
        """ Method that returns the universe in string format for other implementations
            (e.g., for use in other classes).
        ----
        Returns: a detailed representation of the current universe set
        """
        return f"Universe set: {str(self)}"