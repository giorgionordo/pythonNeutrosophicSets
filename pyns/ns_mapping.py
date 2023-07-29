from .ns_universe import NSuniverse
from .ns_set import NSset
#--
from .ns_util import NSreplace
#----
from ast import literal_eval

class NSmapping:
    """
    Package Python Neutrosophic Sets (PYNS)
    Class that defines a mapping between two universes of neutrosophic sets
    ----------------------------------------------------------------------------------
    author: Giorgio Nordo - Dipartimento MIFT, Università di Messina, Italy
    www.nordo.it   |  giorgio.nordo@unime.it
    """

    # costruttore
    def __init__(self, *args):
        """
        Generic constructor of a mapping between two universes.
        It can be defined:
        - by assigning only the domain and the codomain and, optionally, a list of values
        - by passing another object mapping
        ----
        Parameters:
        - args: generic argument; it can be a single parameter corresponding to an alread existent object NSmapping
                or a triple of arguments representing respectively, the domain, codomain
                and the list of function values expressed as strings, lists or tuples
        """
        map = dict()
        #--------------------
        length = len(args)
        if length == 0:
            raise ValueError("constructor method must have at least one parameter")
        elif length == 1:   # se c'è un solo argomento deve trattarsi di una funzione
            if type(args[0]) == NSmapping:   # se è un oggetto NSmapping lo ricopia
                domain = args[0].getDomain()
                codomain = args[0].getDomain()
                map = args[0].getMap()
            #-------------------------------------------------------
            elif type(args[0]) == dict:   # se è un dizionario
                map = args[0]
                domain = NSuniverse(list(map.keys()))
                codomain = NSuniverse(list(set(map.values())))  # elimina gli elementi ripetuti nei valori
            elif type(args[0]) == str:    # se è un dizionario in formato stringa preleva gli elementi
                values = args[0]
                # rimuove apici e virgolette nonché le parentesi delle coppie e consente l'utilizzo
                # alternativo di ; come separatore tra coppie e delle freccette come corrispondenza
                # ottenendo sempre una stringa contenente una sequenza di coppie chiave:valore separate da ,
                sostituz = { "'":"", '"':"", "(":"", ")":"", "[":"", "]":"",
                             "{":"", "}":"", " ":",", ";":",", ",,":",", "->":':' }
                values = NSreplace(values, sostituz)
                # avendo rimosso le stringhe (e i delimitatori) trasforma prima le chiavi in formato stringa
                if '"' not in values and "'" not in values:
                    listcouples = values.split(',')  # spezza le coppie
                    # elabora ciascuna coppia chiave-valore per costruire la nuova stringa
                    listkeysvalues = []
                    # ricrea la lista che rappresenta il dizionario ma con le stringhe
                    for couple in listcouples:
                        key, value = couple.split(':')
                        keyvalue = "'" + key.strip() + "':'" + value.strip()+"'"
                        listkeysvalues.append(keyvalue)
                    values = ", ".join(listkeysvalues)  # ricrea la stringa con le coppie chiave:valore separate da ,
                # aggiunge le graffe alla stringa per ottenere l'espressione del dizionario
                if '{' not in values:
                    values = '{' + values
                if '}' not in values:
                    values = values + '}'
                # trasforma la stringa in dizionario
                map_dict = literal_eval(values)
                nsmap = NSmapping(map_dict)  # utilizza lo stesso costruttore per funzioni da dizionario
                # ottiene dominio, codominio e mappa dall'aggetto NSmapping
                domain = nsmap.getDomain()
                codomain = nsmap.getCodomain()
                map = nsmap.getMap()
            #-------------------------------------------------------
            else:   # altrimenti solleva una eccezione
                raise ValueError("the type or number of parameters do not match those of the constructor method")
        elif length == 3: # devono esserci tre parametri (dominio, codominio ed elenco valori)
            domain = NSuniverse(args[0])
            codomain = NSuniverse(args[1])
            values = args[2]
            if type(domain) != NSuniverse or type(codomain) != NSuniverse:
                raise ValueError("the first two parameters of the constructor method (domain and codomain) must be universe sets")
            card_domain = domain.cardinality()
            for i in range(card_domain):      # prepara il dizionario vuoto (con le sole chiavi)
                map[domain.get()[i]] = ''
            if type(values) in [list, tuple]:        # i valori vengono passati come lista o tupla
                values = [str(e) for e in values]    # e convertiti in lista di stringhe
            elif type(values) == str:             # i valori vengono passati dentro una stringa
                sostituz = { "[":"", "]":"", "(":"", ")":"", ",":" ", ";":" " }
                values = NSreplace(values, sostituz)
                values = values.split()   # riduce a lista
            else:
                raise ValueError("the third parameter of the constructor method must contain a list of codomain values")
            if values != None:
                if len(values) != card_domain:
                    raise IndexError("the number of values passed does not coincide with the cardinality of the declared domain")
                # controlla che tra i values non ci siano elementi estranei al codominio
                values_set = set(values)
                codomain_set = set(codomain.get())
                if not values_set.issubset(codomain_set):
                    raise ValueError("one or more values do not belong to the declared codomain")
                for i in range(card_domain):
                    map[domain.get()[i]] = values[i]
        else:
            raise IndexError("the number of parameters do not match those of the constructor method")
        # memorizza i valori ottenuti nelle proprietà dell'oggetto
        self.__domain = domain
        self.__codomain = codomain
        self.__map = map


    # ------------------------------------------------------------------------------------

    # restituisce il dominio della funzione
    def getDomain(self):
        """ Obtain the domain of the mapping.
        ----
        Returns: the universe set corresponding to the domain of the current mapping
        """
        return NSuniverse(self.__domain.get())


    # restituisce il codominio della funzione
    def getCodomain(self):
        """ Obtain the codomain of the mapping.
        ----
        Returns: the universe set corresponding to the codomain of the current mapping
        """
        return NSuniverse(self.__codomain.get())


    # restituisce le coppie elemento-value come dizionario
    def getMap(self):
        """ Obtain all the element-value pair defining the mapping.
        ----
        Returns: the dictionary containing the element-value pairs of the mapping
        """
        return self.__map


    # ------------------------------------------------------------------------------------

    # assegna il value mediante la funzione per uno specifico elemento
    def setValue(self, u, v):
        """
        Assigns a single value by the neutrosophic mapping to a specific element of the domain, i.e. f(u)=v
        ----
        Parameters:
        - u: element of the domain
        - v: element of the codomain
        """
        u = str(u)
        v = str(v)  # converte in stringa per confrontarla con gli elementi dell'universo che è lista di stringhe
        if u not in self.__domain.get():
            raise IndexError('non-existent element in the domain of the function')
        if v not in self.__codomain.get():
            raise IndexError('non-existent element in the codomain of the function')
        self.__map[u] = v


    # ------------------------------------------------------------------------------------

    # ottiene il value mediante la funzione di un determinato elemento del dominio
    def getValue(self, u):
        """
        Get the value by the neutrosophic mapping of a specific element of the domain.
        ----
        Parameters:
        - e: element of the domain
        ----
        Returns: the value of u by the current mapping
        """
        u = str(u)  # converte in stringa per confrontarla con gli elementi dell'universo che è lista di stringhe
        if u not in self.__domain.get():
            raise IndexError('non-existent element in the domain of the function')
        return self.__map[u]


    # ------------------------------------------------------------------------------------

    # ottiene la fibra della funzione di un determinato elemento del codominio
    def getFibre(self, v):
        """
        Get the fibre (i.e. the inverse image of a singleton) by the neutrosophic mapping
        of a specific element of the codomain.
        ----
        Parameters:
        - v: element of the codomain
        ----
        Returns: the fibre of v expressed as list of elements of the domain
        """
        v = str(v)  # converte in stringa per confrontarla con gli elementi dell'universo che è lista di stringhe
        if v not in self.__codomain.get():
            raise IndexError('non-existent element in the codomain of the function')
        fibre = list()
        for e in self.__map:
            if self.__map[e] == v:
                fibre.append(e)
        return fibre


    # ------------------------------------------------------------------------------------

    # restituisce l'immagine di un insieme neutrosofico mediante una funzione
    def NSimage(self, nset):
        """
        Method that returns the neutrosophic image of a neutrosophic set by a mapping.
        ----
        Parameters:
        - nset: neutrosophic set on the domain
        ----
        Returns: neutrosophic image of nset by the current mapping
        """
        result = NSset(self.__codomain)
        for v in self.getCodomain():
            fibre = self.getFibre(v)
            if fibre == []:
                triple = [1,1,0]
            else:
                mu_values = list()
                sigma_values = list()
                omega_values = list()
                for u in fibre:
                    mu_values.append(nset.getMembership(u))
                    sigma_values.append(nset.getIndeterminacy(u))
                    omega_values.append(nset.getNonMembership(u))
                triple = [max(mu_values), max(sigma_values), min(omega_values)]  # i.e. (mu, sigma, omega)
            result.setElement(v, triple)
        return result


    # restituisce la controimmagine di un insieme neutrosofico mediante una funzione
    def NScounterimage(self, nset):
        """
        Method that returns the neutrosophic counterimage of a neutrosophic set by a mapping.
        ----
        Parameters:
        - nset: neutrosophic set on the codomain
        ----
        Returns: neutrosophic counterimage of nset by the current mapping
        """
        result = NSset(self.__domain)
        for u in self.getDomain():
            value = self.getValue(u)
            triple = nset.getElement(value)   # i.e. (mu, sigma, omega)
            result.setElement(u, triple)
        return result


    # ------------------------------------------------------------------------------------


    # confronta due funzioni col metodo speciale __eq__
    # sovraccaricando l'operatore di uguaglianza == e restituisce True se sono uguali
    def __eq__(self, g):
        """ Checks if the current mapping is equal to another one.
        ----
        Parameters:
        - g: second mapping
        ----
        Returns: True if the current mapping coincides with the second one
        """
        if self.getDomain() != g.getDomain() or self.getCodomain() != g.getCodomain():
            return False
        else:
            equal = True
            for e in self.getDomain():
                if self.getValue(e) != g.getValue(e):
                    equal = False
                    break
            return equal


    # confronta due funzioni col metodo speciale __ne__
    # sovraccaricando l'operatore di non uguaglianza != e restituisce True se sono diversi
    def __ne__(self, g):
        """ Checks if the current mapping is different from another one.
        ----
        Parameters:
        - g: second mapping
        ----
        Returns: True if the current mapping is different from the second one
        """
        different = not (self == g)
        return different


    # ------------------------------------------------------------------------------------

    # restituisce la funzione neutrosofica come stringa col metodo speciale __str__
    def __str__(self):
        """ Method that returns the mapping in string format for the user.
        ----
        Returns: string containing a map of the current mapping
        """
        unvwidth = 28               # larghezza in colonne del dominio e del codominio
        totwidth = unvwidth*2 + 8   # calcolo della larghezza totale
        s = f"\n {self.getDomain():>{unvwidth}}   ->   {self.getCodomain():<{unvwidth}}\n" + "-" * totwidth + "\n"
        for e in self.__map:
            s += f" {e:>{unvwidth}}  |->  {self.__map[e]:<{unvwidth}}\n"
        return s


    # restituisce la rappresentazione funzione neutrosofica come stringa col metodo speciale __repr__
    # che viene implicitamente utilizzata nelle altre classi
    def __repr__(self):
        """ Method that returns the mapping for other implementations
        (e.g., for use in other classes).
        ----
        Returns: a detailed representation of the current mapping
        """
        return f"Neutrosophic mapping: {str(self)}"
