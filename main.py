import re
from time import time
from glob import glob
from shutil import copy
from os import replace
from sys import exit
from tempfile import NamedTemporaryFile as namedtemporaryfile
from os.path import expanduser #for test environment only
from os import system #for test environment only
import codecs

def update(rootdir, old_string, new_string):
    start = time() 
    dir_list = [] 
    dir_list += glob(rootdir + '/*/???????????????/???????/???.??????') 
    dir_list += glob(rootdir + '/*/???????????????/???.??????') #TODO- use
    #os.path.join() instead of appending paths
    for d in dir_list: 
        originalfile = codecs.open(d, 'r', 'cp65001') 
        originalfile.close()
        tempfile = namedtemporaryfile('w+', delete=False, encoding='cp65001') 
        copy(originalfile.name, tempfile.name) 
        for text in tempfile: 
            tempfile.write(re.sub (old_string, new_string, text,
                flags=re.IGNORECASE | re.MULTILINE))
        tempfile.close() 
        replace(tempfile.name, originalfile.name) 
        end = time()
    print ("All done-\n",len(dir_list),"files updated\n",
    "{0:.2f}".format(end - start), "seconds elapsed")

#system('clear') #for test environment only
print ("'xml-kinfig'\nConception, design and programming by yenic\nUse at"
        " your own peril, no warranty or support provided\n")
server = input("Enter servername eg. 'test' without quotes\n> ") #h1-chdevws13
rootdir = expanduser('~/') + server # r'//' + server + 'www'
old_string = input("Enter original text value eg."
        " 'internal.hubbardone.net' without quotes. This is not case"
        " sensitive.\n> ") 
new_string = input("Enter new text value eg. 'LocalHostTest' without quotes."
        " This is not case sensitive.\n> ") #internal.elitecorp.com

while True:
    print ('Run now? Y/N')
    tokenDict = {
        'Y':(update, (rootdir, old_string, new_string)),
        'N':(exit, ()),
        }
    user_input = (input("> "))
    fn, args = tokenDict.get(user_input, (None,None)) #unpack the tuple
    if fn == None:
        continue
    else:
        fn(*args)
        break
