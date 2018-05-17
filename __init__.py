from . import pyphptree

def kind_to_icon(s):
    if s=='class': return 1
    if s=='function': return 5
    if s=='trait': return 2
    return 0

def get_headers(filename, lines):
    r = []
    items = list(pyphptree.get_headers(filename, lines))

    # todo
    # post processing: merge nodes of namespaces with same names

    for v in items:
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
