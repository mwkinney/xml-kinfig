import time
import glob
from os.path import expanduser
from sys import exit
import re
#from tempfile import TemporaryFile
import tempfile
import shutil
#import os

class XmlHandler(object):
    def __init__(self, rootdir):
        start = time.time()
        #make/reset list
        dir_list = []
        #make a list of files (and folders)
        dir_list += glob.glob(rootdir + '/*/???????????????/???????/???.??????')
        dir_list += glob.glob(rootdir + '/*/???????????????/???.??????')

    def modify_files(self, old_string, new_string):
        for d in dir_list: # for-each file
            originalFile = open(d, 'r') # open file and read it
            tempFile = tempfile.NamedTemporaryFile('w+b', delete=False) # open a tempfile for read/write 
            shutil.copy (originalFile, tempFile.name) #copy originalFile over tempFile
            for line in tempfile: #replace strings in tempfile
                tempfile.write(re.sub(line.replace(old_string, new_string flags=re.IGNORECASE | re.MULTILINE)))
            #close the tempfile
            #rename tempfile over original file's name
            #deleteme- shutil.copy (originalFile, tempFile) #copy tempFile over originalFile 
            #deleteme- originalFile.close() #save?? close originalFile
            #deleteme- tempFile.close() #close tempfile (deletes it, also GC'd by default)
        end = time.time()
        print ('All done\n', len(dir_list),'files updated\n', \
        '{0:.2f}'.format(end - start), 'seconds elapsed')

class UserInput(object):
    def __init__(self):
		#server_string = input("Enter servername eg. 'h1-chdevws13' without quotes\n> ")
        server = input("Enter servername eg. 'test' without quotes\n> ")
        #rootdir = r'//' + server_string + '/www'
        rootdir = expanduser('~/') + server
        #new_string = input("Enter SMTP value eg. 'internal.elitecorp.com' without "
        #"quotes\n> ")
        old_string = input("Enter original text value eg.\
        'internal.hubbardone.net' without quotes. This is not case\
        sensitive.\n> ")
        new_string = input("Enter SMTP value eg. 'localhost' without\
                quotes. This is not case sensitive.\n> ")

    def accept_parameters(self):
        print ('xml-kinfig\nby Mark Kinney\nUse at your own peril, no warranty or'\
        ' support provided\n')

        while True:
            print ('Run now? Y/N')
            tokenTuple = {
                'Y':(modify_files, (old_string, new_string)),
                'N':(exit, ()),
                }
            user_input = (input("> "))
            fn, args = tokenTuple.get(user_input, (None,None))
            if fn == None:
                continue
            else:
                fn(*args)
                break

startup = UserInput()
xml = XmlHandler()
startup.accept_parameters()
xml.modify_files()
