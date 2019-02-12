from . import pyphptree

def _icon(s):

    if s=='class':
        return 1
    if s=='function':
        return 5
    if s=='trait':
        return 2
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
        kind = _icon(v['kind'])
        y = v['line']
        x = v['col']
        lev = v['level']+1 

        r += [ ( 
            (x, y, x+len(name), y),
            lev,
            name,
            kind,
            ) ]
    return r
