import itertools

LEETTERS = {
    'a' : ['A', 'a', '4'],
    'b' : ['B', 'b', '8'],
    'c' : ['C', 'c'],
    'd' : ['D', 'd'],
    'e' : ['E', 'e', '3'],
    'f' : ['F', 'f'],
    'g' : ['G', 'g'],
    'h' : ['H', 'h'],
    'i' : ['I', 'i', '1'],
    'j' : ['J', 'j'],
    'k' : ['K', 'k'],
    'l' : ['L', 'l', '1'],
    'm' : ['M', 'm'],
    'n' : ['N', 'n'],
    'o' : ['O', 'o', '0'],
    'p' : ['P', 'p'],
    'q' : ['Q', 'q'],
    'r' : ['R', 'r', '5'],
    's' : ['S', 's', '5'],
    't' : ['T', 't', '7'],
    'u' : ['U', 'u', '5'],
    'v' : ['V', 'v'],
    'w' : ['W', 'w'],
    'x' : ['X', 'x'],
    'y' : ['Y', 'y', '7'],
    'z' : ['Z', 'z']}

PREFIXES = ['!', '!!!', '?', '???']

def gen_words(word):
    built_list = [LEETTERS[w] for w in word]
    for pre in PREFIXES:
        for combo in list(itertools.product(*built_list)):
            leet = ''.join(combo)
            yield leet
            yield leet + pre
            yield pre + leet + pre
