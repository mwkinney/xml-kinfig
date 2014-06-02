#! /usr/bin/env python

from __future__ import print_function
import re
from time import time
from glob import glob
from shutil import move
from sys import exit
from os import remove
from tempfile import NamedTemporaryFile as namedtemporaryfile

GREETING = ("""'xml-kinfig' v1.1 - bulk file update utility
Conception, design and programming by yenic
Use at your own peril, no warranty or support provided 
Ctrl-C to exit at any time\n""")

END = ("\nPress ENTER to exit")

ENTERSERVER = ("Enter servername and share eg. 'h1-chdevws13\www2'"
        " without quotes\n> ")

ENTEROLD = ("\nEnter original text value eg."
        " 'internal.hubbardone.net' without quotes \nThis is not case"
        " sensitive\n> ")

ENTERNEW = ("\nEnter new text value eg. 'internal.elitecorp.com'"
        " without quotes \nThis will appear as you case it\n> ")

RUNNOW = ("\nRun now? Y/N")

def update(rootdir, old_string, new_string):
    start = time() 
    dir_list = [] 
    #TODO- os.path.join() 
    dir_list += glob(rootdir + '/*/*/???????????????/???????/???.??????') 
    dir_list += glob(rootdir + '/*/*/???????????????/???.??????')  
    errors = []
    for d in dir_list: 
        try:
            with open (d) as input:
                with namedtemporaryfile('w+', delete=False) as output:
                    for text in input:
                        output.write(re.sub (old_string, new_string, text,
                        flags=re.IGNORECASE | re.MULTILINE))
            move(output.name, input.name)
        except EnvironmentError as e:
            errors.append(e.filename)
        try:
            remove(output.name)
        except EnvironmentError:
            pass
    end = time()
    if len(errors) > 0:
        print ("\nPermission errors for the following (check for read-only)"
            "\n", "\n".join(errors), sep="", end="\n")
    print ("\nAll done-\n",len(dir_list)," files found\n",
    "{0:.2f}".format(end - start)," seconds elapsed", sep="")
    raw_input(END)

print (GREETING)
server = raw_input(ENTERSERVER) 
rootdir = r'//' + server 
old_string = raw_input(ENTEROLD) 
new_string = raw_input(ENTERNEW)

while True:
    print (RUNNOW)
    tokenDict = {
        'Y':(update, (rootdir, old_string, new_string)),
        'N':(exit, ()),
        }
    user_input = (raw_input("> "))
    fn, args = tokenDict.get(user_input, (None,None))
    if fn:
        fn(*args)
        break
