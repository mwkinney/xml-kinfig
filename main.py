import re
from time import time
from glob import glob
from shutil import copy
from sys import exit
from tempfile import NamedTemporaryFile as namedtemporaryfile
from shutil import copy
from os.path import expanduser #for test environment only
from os import system #for test environment only

def update(rootdir, old_string, new_string):
    start = time() 
    dir_list = [] 
    dir_list += glob(rootdir + '/*/???????????????/???????/???.??????') 
    dir_list += glob(rootdir + '/*/???????????????/???.??????') #TODO- use
    #os.path.join() instead of appending paths
    for d in dir_list: 
        with open (d) as input:
            with namedtemporaryfile('w+', delete=False) as output:
                for text in input:
                    output.write(re.sub (old_string, new_string, text,
                        flags=re.IGNORECASE | re.MULTILINE))
        copy(output.name, input.name)
    end = time()
    print "All done-\n",len(dir_list),"files updated\n",\
    "{0:.2f}".format(end - start), "seconds elapsed"

#system('clear') #for test environment only
print "'xml-kinfig'\nConception, design and programming by yenic\nUse at"\
        " your own peril, no warranty or support provided\nHit Ctrl-C to"\
        " exit at any time\n"
server = raw_input("Enter servername eg. 'h1-chdevws13' without quotes\n> ") 
rootdir = r'//' + server + 'www'
old_string = raw_input("Enter original text value eg."
        " 'internal.hubbardone.net' without quotes. This is not case"
        " sensitive.\n> ") 
new_string = raw_input("Enter new text value eg. 'internal.elitecorp.com' without quotes."
        "This will appear as you case it.\n> ")

while True:
    print 'Run now? Y/N'
    tokenDict = {
        'Y':(update, (rootdir, old_string, new_string)),
        'N':(exit, ()),
        }
    user_input = (raw_input("> "))
    fn, args = tokenDict.get(user_input, (None,None)) #unpack the tuple
    if fn == None:
        continue
    else:
        fn(*args)
        break
