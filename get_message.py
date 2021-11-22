'''Create a class or function to grab message file to be encrypted,
and read it into the enigma machine.'''
class GetFile:
        
    def read_file(ffr):
        read_it = ffr.readlines()
        for i in read_it:
            print (i)
