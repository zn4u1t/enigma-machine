# The Digital Enigma
# Main Script
# Zach Nault
# 5/25/2018
# Runs the Enigma Machine
# Change Log: 001:5/26/2018. Added temporary print statements to show that the imports worked correctly.
# 002:5/29/2018. Added a wheels import, and a flat file del.
# 003:6/5/2018. Added duplicates of the wheel class.
# 004:6/16/2018. Was originally (main.py. + maindecrypt.py. = enigma.py)
# 005:6/16/2018. Start menu added, along with user input requests
# 006:6/26/2018. Added option for encrypted message to be sent to an e-mail.
# 007:6/27/2018. Made number of wheels, more user friendly 

import sys
from wheels2 import Wheels
from make_dict import FileDict
from make_decrypt import FileDecrypt
from send_mail import EmailCode
from the_end import KillZone as kz

def main():
    wheel_menu()
    make_menu()
    kz.fatality()
    sys.exit()

def make_menu():
    fileIn = open("mainMenu.txt", "r") 
    for i in range(16):
        lineIn = fileIn.readline () 
        print (lineIn)
    fileIn.close()
    choice = str(input("Enter number and press enter:"))
    if choice == "1":
        ins = open('READ ME.txt', 'r')
        prin = ins.readlines()
        for i in prin:
            print (i)
        input ('Press enter to return to machine')
        main()
    elif choice == "2":
        encrypt()
    elif choice == "3":
        maindecrypt()
    elif choice== "4":
        kz.fatality()  
        sys.exit()
    else:
        main()
        print ("You must only select a number 1-4.")
        print ("Please try again")

def menu_2():
    choice = input ("Send encrypted message to e-mail? y/n?")
    if choice == "y":
        ec = EmailCode()
        ec.create_mes()
    else:
        kz.fatality()
        sys.exit()

def wheel_menu():
    we = Wheels()
    global x
    x = int(input("Set number of wheels for encryption/decryption:\nThe larger the number the slower the run time."))
    we.loops(x)

def encrypt():
    fd = FileDict()
    fd.file_dict(open('Plugboard dictionary.txt'))
    secret = input("Enter file name to be converted:")
    fd.enter_message(secret)
    fd.wheel_trans()
    fd.file_dict(open('Static\dict_inA.csv'))
    fd.loops(x)
    fd.wheel_trans()
    fd.file_dict(open('Static\dict_inB.csv'))
    fd.wheel_trans()
    fd.output_check()
    print ("Message saved in file MESSAGE.txt ")
    menu_2()

def maindecrypt():
    fde = FileDecrypt()
    fde.file_dict(open('Static\dict_outB.csv'))
    secret = input("Enter file name to be converted:")
    fde.enter_message(secret)
    fde.wheel_trans()
    fde.loops(x)
    fde.wheel_trans()
    fde.file_dict(open('Static\dict_outA.csv'))
##    fde.wheel_trans()
##    fde.file_dict(open('Plugboard_out.csv'))
##    fde.wheel_trans()
    #fde.output_check()
    fde.output_check2()
    input ("Decrypted message saved in file DECRYPTION.txt \nPress enter to exit")
        
if __name__ == '__main__':
    main()




