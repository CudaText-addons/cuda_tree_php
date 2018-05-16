from . import pyphptree

def kind_to_icon(s):
    if s=='class': return 1
    if s=='function': return 5
    return 0

def get_headers(filename, lines):
    r = []
    for v in pyphptree.get_headers(filename, lines):
        name = v['name'] or '??'
        kind = kind_to_icon(v['kind'])
        
        r += [ (
            v['line'], 
            v['level']+1, 
            name, 
            kind,
            ) ]
    return r
        

helper = {
  'PHP': get_headers,
}
