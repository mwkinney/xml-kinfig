import re
from time import time
from glob import glob
from shutil import copy
from sys import exit
from tempfile import NamedTemporaryFile as namedtemporaryfile

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
    print "\nAll done-\n",len(dir_list),"files updated\n",\
    "{0:.2f}".format(end - start), "seconds elapsed"
    raw_input("\nPress ENTER to exit")

print "'xml-kinfig'\nBulk file update utility\n"\
        "Conception, design and programming by yenic\n"\
        "Use at your own peril, no warranty or support provided\nCtrl-C"\
        " to exit at any time\n"
server = raw_input("Enter servername and share eg. 'h1-chdevws13\www2'"\
        " without quotes\n> ") 
rootdir = r'//' + server 
old_string = raw_input("\nEnter original text value eg."
        " 'internal.hubbardone.net' without quotes \nThis is not case"
        " sensitive\n> ") 
new_string = raw_input("\nEnter new text value eg. 'internal.elitecorp.com'"
        " without quotes \nThis will appear as you case it\n> ")

while True:
    print '\nRun now? Y/N'
    tokenDict = {
        'Y':(update, (rootdir, old_string, new_string)),
        'N':(exit, ()),
        }
    user_input = (raw_input("> "))
    fn, args = tokenDict.get(user_input, (None,None))
    if fn == None:
        continue
    else:
        fn(*args)
        break
