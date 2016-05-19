import itertools
import logging
import os
import time
import signal
import subprocess

import psutil


logfile = 'leetlog_' + str(int(time.time())) + '.log'
logging.basicConfig(filename=logfile, filemode='w', level=logging.DEBUG)

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


def decrypt(filename, timeout, cnt):
    cmd = AXE + ' -d ' + PTH.format(filename)
    run_dec = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    try:
        run_dec.wait(timeout=timeout)
        msg = 'successful decryption at count %s' % cnt
        return {'end': True, 'msg': msg}
    except subprocess.TimeoutExpired:
        logging.debug('timed out')
        kill(run_dec.pid)
        try:
            os.system('taskkill /im AxCrypt.exe')
        except:
            pass
        time.sleep(10)
        clear_cache = subprocess.Popen(CLR, stdout=subprocess.PIPE, shell=True)
        try:
            clear_cache.wait(timeout=timeout)
            msg = 'unable to decrypt at count %s' % cnt
            return {'end': False, 'msg': msg}
        except subprocess.TimeoutExpired:
            msg = 'clear cache timeout, exiting at count %s' % cnt
            return {'end': True, 'msg': msg}

 
def gen_words(word):
    built_list = [LEETTERS[w] for w in word]
    for pre in PREFIXES:
        for combo in list(itertools.product(*built_list)):
            leet = ''.join(combo)
            yield leet
            yield leet + pre
            yield pre + leet + pre


def test_length(word, cnt):
    g = gen_words(word)
    c = 0
    for w in g:
        c+=1
        if c % cnt == 0:
            logging.debug(c)


def gen_file(word):
    g = gen_words(word)
    cnt = 0
    out_file = 'gen_list_' + str(int(time.time())) + '.txt'
    with open(out_file, 'w') as f:
        for w in g:
            cnt+=1
            f.write('{i}, {word}\n'.format(i=cnt, word=w))


def do_thing(word, filename, max_cache=5000, timeout=60):
    cnt = 0
    ck = subprocess.check_output(CLR, shell=True)
    stime = int(time.time())
    if ck:
        logging.debug('issue clearing cache')
        return
    for pwd in gen_words(word):
        cnt += 1
        ak = subprocess.check_output(ADD + pwd, shell=True)
        if cnt % max_cache == 0:
            logging.debug('count = {c} check_output = {o}'.format(c=cnt, o=ak))
            res = decrypt(filename, timeout, cnt)
            logging.debug('msg: {}'.format(res['msg']))
            if res['end']:
                return
    res = decrypt(filename, timeout, cnt)
    logging.debug('msg: {}'.format(res['msg']))
    return
