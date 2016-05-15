import itertools
import os
import signal
import subprocess

import psutil


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

PTH = '"C:\leeterhosen\\test\{}"'
AXE = '"C:\Program Files\Axantum\AxCrypt\AxCrypt.exe"'
ADD = AXE + ' -k '
CLR = AXE + ' -t'


def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()


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


def do_thing(word, filename, max_cache):
    ck = subprocess.check_output(CLR, shell=True)
    print(ck)
    if ck:
        print('there is?')
    else:
        print('ck none')
    cnt = 0
    ps = input('press key')
    for pwd in gen_words(word):
        cnt += 1
        print('ak')
        ak = subprocess.check_output(ADD + pwd, shell=True)
        print('zerps: %s - %s' % (cnt, ak))
	#if cnt % max_cache == 0:
    print('running...')
    run_dec = subprocess.Popen(decrypt(filename), stdout=subprocess.PIPE, shell=True)
    try:
        run_dec.wait(timeout=5)
    except subprocess.TimeoutExpired:
        print('timed out')
        kill(run_dec.pid)

