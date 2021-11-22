# The Digital Enigma
# File cleanup class
# Zach Nault
# 6/5/2018
# A class to delete folders and files associated with the machine.
# Change Log:

import os
import shutil

class KillZone:
    '''Deletes files and folders from computer.'''
    def fatality():
        shutil.rmtree('Delete_me')
        os.remove('Plugboard_out.csv')
        #os.remove('Plugboard dictionary.txt')
        
    
    
    
