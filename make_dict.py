# The Digital Enigma
# FileDict Class
# Zach Nault
# 6/9/2018
# Class for transferring message through the wheels.
# Change Log: 001:6/22/2018. Added functionality for infinte amount of wheels.

import sys
from the_end import KillZone as kz

class FileDict:
    ''' Takes flat files and creates wheels, and then runs code through them.'''
    def __init__(self):
        self.d = {}

    def file_dict(self, infile):
        '''Take flat file and make into a dict.'''
        with infile as f:
                  for line in f:
                      key, value = line.split(':')
                      self.d[key] = value.strip("\n")    

    def enter_message(self, secret):
        '''Message entry point for encryption.'''
        try:
            with open(secret) as f:
                message = f.read()
                self.enc = ''.join([self.d.get(c, '') for c in message])
                #print(self.enc)
        except FileNotFoundError:
            print ("File not encryptable!")
            input ("You must restart the machine!\nPress enter to exit.")
            kz.fatality()
            sys.exit()
                        
    def wheel_trans(self):
        ''' Gives the values as output for keys input.'''
        self.new = ''.join([self.d.get(c, '') for c in self.enc])
        

    def output_check(self):
        ''' Output messaage to file'''
        outmes = open('MESSAGE.txt', 'w')
        for i in self.new:
            outmes.write(i)
        outmes.close()

    def loops(self, x):
        ''' Generates output file based on user input.'''
        count = 1
        fd = FileDict()
        while (count <= x):         # Dictates how many dicts will be read.
            self.new = ''.join([self.d.get(c, '') for c in self.enc])
            fd.file_dict(open('Delete_me\dict_in' + str(count) + '.csv'))
            count = count + 1
        




