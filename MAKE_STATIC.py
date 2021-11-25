
import os
import csv
from random import shuffle
from filecall import PlugBoard as pb


class StaticWheel(object):
    '''Create and shuffle the wheels for the machine.'''
    os.mkdir("Static")

    def __init__(self):
        self.dict_in = {}
        self.dict_out = {}

    def wheel_in(self):
        ''' Creates inbound wheel based on a shuffle of PB.'''
        values = list(pb.d.values())
        keys = list(pb.d.keys())
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


sw = StaticWheel()
sw.wheel_in()
sw.make_static_in((open('Static\dict_inA.csv', 'w', newline='')))
sw.wheel_out()
sw.make_static_out((open('Static\dict_outA.csv', 'w', newline='')))
sw.wheel_in()
sw.make_static_in((open('Static\dict_inB.csv', 'w', newline='')))
sw.wheel_out()
sw.make_static_out((open('Static\dict_outB.csv', 'w', newline='')))
