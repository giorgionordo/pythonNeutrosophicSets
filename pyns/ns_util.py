from re import findall
from ast import literal_eval

"""
Package Python Neutrosophic Sets (PYNS)
ns_util.py
Utility functions for all the class of the package
----------------------------------------------------------------------------------
author: Giorgio Nordo - Dipartimento MIFT. Università di Messina, Italy
www.nordo.it   |  giorgio.nordo@unime.it
"""

# rimpiazza le chiavi coi valori del dizionario nel testo passato
def NSreplace(text, sostituz):
    """ returns the text string after performing all replacements
        of substrings contained in the substitutions dictionary.
    ----
    Parameters:
    - text: string
    - sostituz: dictionary having as keys the substrings to replace with their respective values
    ----
    Returns: the same string after all the replacements
    """
    for k in sostituz:
        text = text.replace(k, sostituz[k])
    return text


# converte una stringa in una tripla di liste
def NSstringToTriplesList(text):
    """
    Converts a string containing a list of tuples to the corresponding data structure
    ----
    Parameters:
    - text: string
    Returns: the list of triples of real numbers
    """
    pattern = r'\[.*?\]|\(.*?\)'  # usa le espressioni regolari per isolare le triple
    str_list = findall(pattern, text)  # usa il modulo ast per convertire le strutture
    tpl_list = [tuple(literal_eval(s)) for s in str_list]
    return tpl_list


# restituisce True se il valore è una stringa che rappresenta un dizionario esteso (con :, -> o |->)
def NSisExtDict(obj):
    """
    Checks if the passed parameter is a string expressing an extended dictionary
    ----
    Parameters:
    - obj: a generic object
    Returns: a boolean obj equals true if obj is an extended dictionary
    """
    result = False
    if type(obj) == str:
        result = (":" in obj) or ("->" in obj)
    return result


# converte una stringa in un dizionario corrispondente
def NSstringToDict(text):
    """
    Removes superscripts and quotation marks as well as parentheses of pairs and allows the use of
    alternate use of ; as a separator between pairs and of quotation marks as a match
    always obtaining a string containing a sequence of key:obj pairs separated by commas
    ----
    Parameters:
    - text: string
    ----
    Returns: the dictionary corresponding to the structure defined in the string
    """
    sostituz = {"'": "", '"': "", "(": "", ")": "", "[": "", "]": "",
                "{": "", "}": "", " ": ",", ";": ",", ",,": ",",
                "|->": ":", "->": ':'}
    text = NSreplace(text, sostituz)
    # avendo rimosso le stringhe (e i delimitatori) trasforma prima le chiavi in formato stringa
    listcouples = text.split(',')  # spezza le coppie
    # elabora ciascuna coppia chiave-valore per costruire la nuova stringa
    diz = dict()
    for couple in listcouples:
        key, value = couple.split(':')
        diz[key] = value
    return diz


# divide il testo in linee di lunghezza massima max_length
def NSsplitText(text, max_length):
    """
    Returns the text broken into multiple lines of a predetermined maximum length.
    ----
    Parameters:
    - text: string to split
    - max_length : the predetermined maximum length
    ----
    Returns: the text splitted in more lines long at most max_length
    """
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) <= max_length:
            current_line += word + " "  #  aggiungi la parola alla riga corrente
        else:
            lines.append(current_line.strip())    # aggiungi la riga corrente alle righe
            current_line = word + " "  # Inizia una nuova riga con la parola attuale
    lines.append(current_line.strip())    # aggiungi l'ultima riga rimanente
    result = "\n".join(lines)    # unisce le righe col carattere di andata a capo
    return result

