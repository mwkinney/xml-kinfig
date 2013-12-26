import time
import glob
from xml.etree import ElementTree
from os.path import expanduser
from sys import exit


def update(rootdir, new_string):
    start = time.time()
    #make/reset list
    dir_list = []

    #make a list of files (and folders)
    dir_list += glob.glob(rootdir + '/*/???????????????/???????/???.??????')
    dir_list += glob.glob(rootdir + '/*/???????????????/???.??????')
    for d in dir_list: # for-each file
        doc = ElementTree.parse(d)
        root = doc.getroot()

        tree = ElementTree.ElementTree.parse(d, parse)
        for r in tree('ApplicationInfo'):
            ApplicationInfo.set('SMTPServer', new_string)
            ElementTree.ElementTree.write(r)
    end = time.time()
    print ('All done\n', len(dir_list),'files updated\n', \
    '{0:.2f}'.format(end - start), 'seconds elapsed')


print ('xml-kinfig\nby Mark Kinney\nUse at your own peril, no warranty or'\
        ' support provided\n')
server = input("Enter servername eg. 'test' without quotes\n> ")
rootdir = expanduser('~/') + server
new_string = input("Enter SMTP value eg. 'localhost' without quotes\n> ")

while True:
    print ('Run now? Y/N')
    tokenTuple = {
            'Y':(update, (rootdir, new_string)),
            'N':(exit, ()),
            }
    user_input = (input("> "))
    fn, args = tokenTuple.get(user_input, (None,None))
    if fn == None:
        continue
    else:
        fn(*args)
        break
