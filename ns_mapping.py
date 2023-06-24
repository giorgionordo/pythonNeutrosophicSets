from pyns.ns_universe import NSuniverse
from pyns.ns_set import NSset

class NSmapping:
    """
    class defining a function between two universes of neutrosophic sets
    ----------------------------------------------------------------------------------
    author: Giorgio Nordo - Dipartimento MIFT Università di Messina, Italy
    www.nordo.it   |  giorgio.nordo@unime.it
    """

    # costruttore
    def __init__(self, unv_dominio, unv_codominio=None, valori=None):
        """
        Parameters:
        - unv_dominio: universe set that will constitute the domain of the function
        - unv_codominio: universe set that will constitute the codomain of the function
        - valori: optional list (as a list or tuple) of codomain values that correspond
                  neatly to the elements of the domain
        """
        map = dict()
        #--------------------
        if type(unv_dominio) == NSmapping:
            unv_codominio = unv_dominio.getDomain()
            map = unv_dominio.getMap()
            unv_dominio = unv_dominio.getDomain()
        else:
            card_dominio = unv_dominio.cardinality()
            for i in range(card_dominio):      # prepara il dizionario vuoto (con le sole chiavi)
                map[unv_dominio.get()[i]] = ''
            if type(valori) in [list,tuple]:
                valori = [str(e) for e in valori]
            elif type(valori) == str:
                valori = valori.replace("(", "")
                valori = valori.replace(")", "")
                valori = valori.replace(",", " ")
                valori = valori.replace(";", " ")
                valori = valori.split()   # riduce a lista
            if valori != None:
                if len(valori) != card_dominio:
                    raise ValueError("il numero di valori passati non coincide con la cardinalità del dominio dichiarato")
                # controlla che tra i valori non ci siano elementi estranei al codominio
                insieme_valori = set(valori)
                insieme_codominio = set(unv_codominio.get())
                if not insieme_valori.issubset(insieme_codominio):
                    raise ValueError("uno o più valori non appartengono al codominio dichiarato")
                for i in range(card_dominio):
                    map[unv_dominio.get()[i]] = valori[i]
        self.__dominio = unv_dominio
        self.__codominio = unv_codominio
        self.__map = map


    # ------------------------------------------------------------------------------------

    # restituisce il dominio della funzione
    def getDomain(self):
        """
        Returns: the universe set corresponding to the domain of the current mapping
        """
        return self.__dominio.get()


    # restituisce il codominio della funzione
    def getCodomain(self):
        """
        Returns: the universe set corresponding to the codomain of the current mapping
        """
        return self.__codominio.get()

    # restituisce le coppie elemento-valore come dizionario
    def getMap(self):
        """
        Returns: the dictionary containing the element-value pairs of the mapping
        """
        return self.__map


    # ------------------------------------------------------------------------------------

    # assegna il valore mediante la funzione per uno specifico elemento
    def setValue(self, u, valore):
        """
        assign a single value by the neutrosophic mapping to a specific element of the domain
        ----
        Parameters:
        - u: element of the domain
        - valore: element of the codomain
        """
        u = str(u)
        valore = str(valore)  # converte in stringa per confrontarla con gli elementi dell'universo che è lista di stringhe
        if u not in self.__dominio.get():
            raise IndexError('elemento inesistente nel dominio della funzione')
        if valore not in self.__codominio.get():
            raise IndexError('elemento inesistente nel codominio della funzione')
        self.__map[u] = valore


    # ------------------------------------------------------------------------------------

    # ottiene il valore mediante la funzione di un determinato elemento del dominio
    def getValue(self, u):
        """
        get the value by the neutrosophic mapping of a specific element of the domain
        ----
        Parameters:
        - e: element of the domain
        Returns: the value of u by the current mapping
        """
        u = str(u)  # converte in stringa per confrontarla con gli elementi dell'universo che è lista di stringhe
        if u not in self.__dominio.get():
            raise IndexError('elemento inesistente nel dominio della funzione')
        return self.__map[u]


    # ------------------------------------------------------------------------------------

    # ottiene la fibra delaa funzione di un determinato elemento del codominio
    def getFibre(self, v):
        """
        get the fibre by the neutrosophic mapping of a specific element of the codomain
        ----
        Parameters:
        - v: element of the codomain
        Returns: the fibre of v expressed as list of elements of the domain
        """
        v = str(v)  # converte in stringa per confrontarla con gli elementi dell'universo che è lista di stringhe
        if v not in self.__codominio.get():
            raise IndexError('elemento inesistente nel codominio della funzione')
        ris = list()
        for e in self.__map:
            if self.__map[e] == v:
                ris.append(e)
        return ris


    # ------------------------------------------------------------------------------------

    # confronta due funzioni col metodo speciale __eq__
    # sovraccaricando l'operatore di uguaglianza == e restituisce True se sono uguali
    def __eq__(self, g):
        """ compares two neutrosophic mappings
        Parameters:
        - g: second mapping
        Returns: True if the current mapping coincides with the second one
        """
        uguali = True
        for e in self.getDomain():
            if self.getValue(e) != g.getValue(e):
                uguali = False
                break
        return uguali


    # confronta due funzioni col metodo speciale __ne__
    # sovraccaricando l'operatore di non uguaglianza != e restituisce True se sono diversi
    def __ne__(self, g):
        """ compares two neutrosophic mappings
        Parameters:
        - g: second mapping
        Returns: True if the current mapping is different from the second one
        """
        differenti = not (self == nsins)
        return differenti


    # ------------------------------------------------------------------------------------

    # restituisce l'immagine di un insieme neutrosofico mediante una funzione
    def NSimage(self, nsins):
        """
        returns the image of a neutrosophic set by a mapping
        ----
        Parameters:
        - nsins: neutrosophic set on the domain
        Returns: neutrosophic image of nsins by the current mapping
        """
        ris = NSset(self.__codominio)
        for v in self.getCodomain():
            fibra = self.getFibre(v)
            if fibra == []:
                (mu, sigma, omega) = (1,1,0)
            else:
                valori_mu = list()
                valori_sigma = list()
                valori_omega = list()
                for u in fibra:
                    valori_mu.append(nsins.getMembership(u))
                    valori_sigma.append(nsins.getIndeterminacy(u))
                    valori_omega.append(nsins.getNonMembership(u))
                mu = max(valori_mu)
                sigma = max(valori_sigma)
                omega = min(valori_omega)
            tripla = (mu, sigma, omega)
            ris.setElement(v, tripla)
        return ris


    # restituisce la controimmagine di un insieme neutrosofico mediante una funzione
    def NScounterimage(self, nsins):
        """
        returns the counterimage of a neutrosophic set by a mapping
        ----
        Parameters:
        - nsins: neutrosophic set on the codomain
        Returns: neutrosophic counterimage of nsins by the current mapping
        """
        ris = NSset(self.__dominio)
        for u in self.getDomain():
            valore = self.getValue(u)
            mu = nsins.getMembership(valore)
            sigma = nsins.getIndeterminacy(valore)
            omega = nsins.getNonMembership(valore)
            tripla = (mu, sigma, omega)
            ris.setElement(u, tripla)
        return ris

    # ------------------------------------------------------------------------------------

    # restituisce la funzione neutrosofica come stringa col metodo speciale __str__
    def __str__(self):
        """ returns the mapping representation in string format for the user
        Returns: string containing a map of the current mapping
        """
        s = "\n"
        for e in self.__map:
            s += f" {e:>10} --> {self.__map[e]:<10}\n"
        return s


    # restituisce la rappresentazione funzione neurtosofica come stringa col metodo speciale __repr__
    # che viene implicitamente utilizzata nelle altre classi
    def __repr__(self):
        """ returns the universe for other implementations (e.g., for use in other classes)
        Returns: string containing a map of the current mapping
        """
        return str(self)
