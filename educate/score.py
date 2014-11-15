from re import sub
import Levenshtein

def score(given, correct):
    """
    Compare the answer with the given, attempting to be slightly smart.
    Remove irrelevant words (and, or); remove punctuation; sort alphabetically,
    then compare using Levenshtein.
    Return the distance value
    """
    regex = '[,:;-]+]|, | the | and | or | a | of | per '
    g = sub(regex, '', given).lower()
    c = sub(regex, '', str(correct)).lower()
    g = sub(r'per', '/', g)
    c = sub(r'per', '/', c)
    g = sub(r'\.$', '', g)
    c = sub(r'\.$', '', c)
    g = sub(r'up to', 'max', g)
    c = sub(r'up to', 'max', c)
    g = sub(r' to ', ' - ', g)
    g = sub(r'-', ' - ', g)
    c = sub(r' to ', ' - ', c)
    c = sub(r'-', ' - ', c)
    g = sub(r'\' *x', '\' x ', g)
    g = sub(r' by ', ' x ', g)
    c = sub(r'\' *x', '\' x ', c)
    c = sub(r' by ', ' x ', c)
    g = ''.join(sorted(g.split()))
    c = ''.join(sorted(c.split()))
    dist = Levenshtein.distance(g, c)
    return dist


    
