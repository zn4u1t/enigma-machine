# The Digital Enigma
# Wheels class
# Zach Nault
# 6/9/2018
# Creates wheels for the machine, and outputs them into flat files.
# Change Log: 001: 6/19/2018. Added loop function to create multiple wheels

import os
import csv
from random import shuffle
from filecall import PlugBoard as pb


class Wheels(object):
    '''Create and shuffle the wheels for the machine.'''

    def __init__(self):
        self.dict_in = {}
        self.dict_out = {}

    def wheel_in(self):
        ''' Creates inbound wheel based on a shuffle of PB.'''
        values = list(pb.d.values())
        keys = list(pb.d.keys())
        s_val = shuffle(values)
        s_key = shuffle(keys)
        self.dict_in = dict(zip(keys, values))
        print("INBOUND", self.dict_in)
        print("====================================================")

    def wheel_out(self):
        ''' Reverses key/value input/output.'''
        self.dict_out = {v: k for k, v in self.dict_in.items()}
        print("OUTBOUND", self.dict_out)
        print("------------------------WHEEL SEPERATOR-------------")

    def make_static_in(self, outfile):
        with outfile as csv_file:
            writer = csv.writer(csv_file, delimiter=':')
            for key, value in self.dict_in.items():
                writer.writerow([key, value])

    def make_static_out(self, outfile):
        with outfile as csv_file:
            writer = csv.writer(csv_file, delimiter=':')
            for key, value in self.dict_out.items():
                writer.writerow([key, value])

    def loops(self, x):
        count = 1
        w = self.dict_in.items()
        we = Wheels()
        while (count <= x):         # Dictates how many wheels will be created.
            we.wheel_in()
            op = we.make_static_in(
                (open('Delete_me\dict_in' + str(count) + '.csv', 'w', newline='')))
            we.wheel_out()
            op2 = we.make_static_out(
                (open('Delete_me\dict_out' + str(count) + '.csv', 'w', newline='')))
            count = count + 1


os.mkdir("Delete_me")
