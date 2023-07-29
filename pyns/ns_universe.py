from .ns_util import NSreplace

class NSuniverse:
    """
    Package Python Neutrosophic Sets (PYNS)
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
        if length == 0:
            raise IndexError("the universe set must contain at least an element")
        elif length == 1:
            elem = args[0]
            if type(elem) == set:
                raise ValueError("type set is not suitable because the elements of the universe set must be assigned in a specific order")
            elif type(elem) in [list, tuple]:
                universe = [str(e) for e in elem]
            elif type(elem) == NSuniverse:
                universe = elem.get()
            elif type(elem) == str:
                sostituz = { "{":"", "}":"", "[":"", "]":"", "(":"", ")":"",
                             ",":" ", ";":" " }
                elem = NSreplace(elem, sostituz)
                universe = elem.split()
            else:  # se si tratta di un solo elemento non di tipo stringa
                universe = [str(elem)]
        elif length > 1:   # se la lunghezza è maggiore di 1
            for i in range(length):
                universe.append(str(args[i]))
        # controlla che non siano stati assegnati elementi ripetuti
        univset = set(universe)
        if len(universe) != len(univset):
            raise ValueError("the universe set cannot contain repeated elements")
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

    #----------------- iteratore di oggetti NSuniverse

    # definisce l'iteratore per l'oggetto insieme universo azzerando l'indice
    def __iter__(self):
        """ Method that initializes iterator on elements of the current universe set
        """
        self.__i = 0   # inizializza l'indice privato __i da usare come contatore
        return self

    # restituisce il prossimo elemento iterato dell'oggetto insieme universo
    def __next__(self):
        """ Method that returns the iterated element of the current universe set
        ----
        Returns: the element of index self.__i  of the universe set
        """
        if self.__i < len(self.__universe):    # se l'indice __i non eccede la lunghezza dell'insieme universo
            elem = self.__universe[self.__i]  # preleva l'elemento di indice __i
            self.__i +=1                       # incremente il contatore privato __i
            return elem                        # e restituisce l'elemento
        raise StopIteration                    # altrimenti interrompi l'iterazione


    # ------------------------------------------------------------------------------------

    # restituisce l'universo come stringa col metodo speciale __str__
    def __str__(self):
        """ Method that returns the universe in string format for the user.
        ----
        Returns: string containing a list of the elements of the current universe set
        """
        list_string_elements = [str(e) for e in self.__universe]
        s = "{ " + ", ".join(list_string_elements) + " }"
        return s


    # metodo privato per la stampa formattata
    def __format__(self, spec):
        """ Method that returns the formatted string according to a given specifier
            provided as the second parameter.
        ----
        Returns: the formatted string according to the spec specifier
        """
        unvstr = str(self)
        result = f"{unvstr:{spec}}"
        return result


    # restituisce la rappresentazione universo come stringa col metodo speciale __repr__
    # che viene implicitamente utilizzata nelle altre classi
    def __repr__(self):
        """ Method that returns the universe in string format for other implementations
            (e.g., for use in other classes).
        ----
        Returns: a detailed representation of the current universe set
        """
        return f"Universe set: {str(self)}"