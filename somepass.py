import itertools
import subprocess

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

## AxCrypt
## "%ProgramFiles%\Axantum\AxCrypt\AxCrypt" -k "passphrase"
## "%ProgramFiles%\Axantum\AxCrypt\AxCrypt" -d "filename"
##
## cache pass 'dog'
## .\AxCrypt.exe -k "dog"
##
## decrypt using "dog" as the password
## .\AxCrypt.exe -k "dog" -d .\z-txt.axx
##
## decrypt file using pass in cache
## .\AxCrypt.exe -d .\z-txt.axx
##
## clear cache
## .\AxCrypt.exe -t

PTH = '"C:\Program Files\Axantum\AxCrypt\{}\"'
AXE = '"C:\Program Files\Axantum\AxCrypt\AxCrypt.exe"'
ADD = AXE + ' -k '
CLR = AXE + ' -t'

def decrypt(filename):
    return AXE + ' -d ' + PTH.format(filename)
 
def gen_words(word):
    built_list = [LEETTERS[w] for w in word]
    for pre in PREFIXES:
        for combo in list(itertools.product(*built_list)):
            leet = ''.join(combo)
            yield leet
            yield leet + pre
            yield pre + leet + pre
