from time import time
from glob import glob
from tempfile import NamedTemporaryFile as namedtemporaryfile
from os import remove
from shutil import copy
from sys import exit
from re import sub
from os.path import expanduser #for test environment only
from os import system #for test environment only

class Engine(object):
    def __init__(self):
        system('clear') #for test environment only
        print ("'xml-kinfig'\nConception, design and programming by yenic\nUse at your own peril, no warranty or"\
        " support provided\n")
		#server = input("Enter servername eg. 'h1-chdevws13' without quotes\n> ")
        self.server = raw_input("Enter servername eg. 'test' without quotes\n> ") #for test environment only
        #rootdir = r'//' + server + '/www'
        self.rootdir = expanduser('~/') + self.server #for test environment only
        self.old_string = raw_input("Enter original text value eg."\
        "'internal.hubbardone.net' without quotes. This is not case"\
        " sensitive.\n> ") 
        #new_string = input("Enter new text value eg. 'internal.elitecorp.com' without "
        #"quotes. This is not case sensitive.\n> ")
        self.new_string = raw_input("Enter new text value eg. 'LocalHostTest' without"\
                " quotes. This is not case sensitive.\n> ") #for test environment only

    def modify_files(self, old_string, new_string, dir_list):
        start = time() #begin counter
        for d in dir_list: # for-each file
            self.originalfile = open(d, 'r') # open file and read it
            self.originalfile.close()
            self.tempfile = namedtemporaryfile('w+b', delete=False) # open a tempfile for read/write 
            copy(self.originalfile, self.tempfile.name) #copy originalFile over tempFile
            for line in self.tempfile: #replace strings in tempfile
                self.tempfile.write(re.sub (line.replace (self.old_string, self.new_string, flags=re.IGNORECASE | re.MULTILINE)))
            self.tempfile.close() #close the tempfile
            shutil.copy(self.tempfile.name, self.originalfile) #rename (move) tempfile over original file's name
            os.remove(self.tempfile.name) #delete tempfile
        end = time()
        print ("All done\n", len(dir_list),"files updated\n", \
        "{0:.2f}".format(end - start), "seconds elapsed")

class Validator(object):
    def __init__(self, startup):
        self.startup = startup
        self.dir_list = [] #make/reset list
        self.dir_list += glob(startup.rootdir + '/*/???????????????/???????/???.??????') #make list of files (and folders)
        self.dir_list += glob(startup.rootdir + '/*/???????????????/???.??????') #TODO- use os.path.join() instead of appending paths

    def accept_parameters(self, startup):
        while True:
            print ('Run now? Y/N')
            tokenTuple = {
                'Y':(self.startup.modify_files, (self.startup.old_string, self.startup.new_string, self.dir_list)),
                'N':(exit, ()),
                } #pack the tuple
            self.user_input = (raw_input("> "))
            fn, args = tokenTuple.get(self.user_input, (None,None)) #unpack the tuple, TODO- better comments here
            if fn == None:
                continue
            else:
                fn(*args)
                break

startup = Engine()
xml = Validator(startup)
xml.accept_parameters(startup)

#xml.accept_parameters()
#startup.modify_files()
