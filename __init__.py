from . import pyphptree

def kind_to_icon(s):

    if s=='class': return 1
    if s=='function': return 5
    if s=='trait': return 2
    return 0

def get_headers(filename, lines):
    '''
    gets list of tuples in format:
    ( (x1,y1,x2,y2), level, title, icon)
    '''
    r = []
    items = pyphptree.get_headers(filename, lines)

    # todo
    # post processing: merge nodes of namespaces with same names

    for v in items:
        name = v['name'] or '??'
        kind = kind_to_icon(v['kind'])
        line = v['line']
        col = v['col']

        r += [ ( 
            (col, line, col+1, line),
            v['level']+1,
            name,
            kind,
            ) ]
    return r
