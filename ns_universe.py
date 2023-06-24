class NSuniverse:
    """
    class defining a universe set for neutrosophic sets
    ----------------------------------------------------------------------------------
    author: Giorgio Nordo - Dipartimento MIFT Università di Messina, Italy
    www.nordo.it   |  giorgio.nordo@unime.it
    """

    # costruttore
    def __init__(self, *args):
        """
        costruttore generico di un universo
        ----
        Parameters:
        - args: argomento generico (lista, tupla, stringa o elenco di valori)
        """
        universo = list()   # lista di stringhe
        lunghezza = len(args)
        if lunghezza == 1:
            elem = args[0]
            if type(elem) in [list, tuple]:
                universo = [str(e) for e in elem]
            elif type(elem) == NSuniverse:
                universo = elem.get()
            elif type(elem) == str:
                elem = elem.replace("(", "")
                elem = elem.replace(")", "")
                elem = elem.replace(",", " ")
                elem = elem.replace(";", " ")  # la lunghezza potrebbe cambiare perché abbiamo rimosso i separatori
                universo = elem.split()
            else:
                universo = [str(elem)]
        elif lunghezza > 1 :   # se la lunghezza è maggiore di 1
            for i in range(lunghezza):
                universo.append(str(args[i]))
        self.__universo = universo


    #------------------------------------------------------------------------------------

    # metodo che restituisce l'universo come lista
    def get(self):
        """
        Returns: lista degli elementi dell'universo
        """
        return self.__universo


    # metodo che restituisce la cardinalità (il numero di elementi) dell'universo
    def cardinality(self):
        """
        Returns: the number of elements of the current universe
        """
        return len(self.__universo)


    #------------------------------------------------------------------------------------

    # confronta due insiemi universo col metodo speciale __eq__
    # sovraccaricando l'operatore di uguaglianza ==
    # e restituisce True se sono uguali
    def __eq__(self, unv):
        """ compare the current universe with another one
        Returns: True if the universes are equal
        """
        uguali = (self.__universo == unv.get())
        return uguali

    # confronta due insiemi universo col metodo speciale __ne__
    # sovraccaricando l'operatore di non uguaglianza !=
    # e restituisce True se sono diversi
    def __ne__(self, unv):
        """ compare the current universe with another one
        Returns: True if the universes are different
        """
        differenti = not (self == unv)
        return differenti


    #------------------------------------------------------------------------------------


    # restituisce l'universo come stringa col metodo speciale __str__
    def __str__(self):
        """ returns the universe in string format for the user
        Returns: string containing a list of the elements of the current universe
        """
        lista_elementi_stringa = [str(e) for e in self.__universo]
        s = "{ " + ", ".join(lista_elementi_stringa) + " }"
        return s


    # restituisce la rappresentazione universo come stringa col metodo speciale __repr__
    # che viene implicitamente utilizzata nelle altre classi
    def __repr__(self):
        """ returns the universe in string format for other implementations (e.g., for use in other classes)
        Returns: string containing a list of the elements of the current universe
        """
        return str(self)
