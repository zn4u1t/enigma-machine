# The Digital Enigma
# E-mail script
# Zach Nault
#6/26/2018
# Sends the encrypted message to e-mail. I kept it limited to encryption only.
# Change Log:001:6/26/2018. Made into a class for use in the machine.

import os
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailCode(object):
    '''A class for sending the encrypted message through e-mail.'''

    def edit_email(self):
        '''Gets name and address for message.'''
        print("               Ex: John Jon123@email.com")
        name = input("Type name and e-mail address:")
        fill = open('mycontacts.txt', 'w')
        fill.write(name)

    def get_contacts(self, filename):
        '''Return two lists names, emails containing names and email addresses
        read from a file specified by filename.
        '''
        
        names = []
        emails = []
        with open(filename, mode='r', encoding='utf-8') as contacts_file:
            for a_contact in contacts_file:
                names.append(a_contact.split()[0])
                emails.append(a_contact.split()[1])
        return names, emails

    def read_template(self, filename):
        '''Returns a Template object comprising the contents of the 
        file specified by filename.
        '''
        
        with open(filename, 'r', encoding='utf-8') as template_file:
            template_file_content = template_file.read()
        return Template(template_file_content)

    def create_mes(self):
        ec = EmailCode()
        ec.edit_email()
        names, emails = ec.get_contacts('mycontacts.txt') # read contacts
        mess = open('message.txt')
        message_template = mess.read()
        MY_ADDRESS = 'enigmaMachine@hackermail.com'       # Use the e-mail you want to send from.
        PASSWORD = 'En!gmaM4ch!n3'                      # Adjust SMTP settings as well!!!!
        # set up the SMTP server
        s = smtplib.SMTP(host='smtp.mail.com', port=587)     #Set for your e-mail 
        s.starttls()
        s.login(MY_ADDRESS, PASSWORD)

        # For each contact, send the email:
        for email in zip(names, emails):
            msg = MIMEMultipart()       # create a message
            message = message_template
            msg['From']=MY_ADDRESS
            msg['To']=email
            msg['Subject']="SAVE THIS MESSAGE"
            msg.attach(MIMEText(message, 'plain'))
            s.send_message(msg)
            del msg
            
        # Terminate the SMTP session and close the connection
        s.quit()
        os.remove('mycontacts.txt')


