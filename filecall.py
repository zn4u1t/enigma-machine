class PlugBoard():
    '''Create a dict from a .txt file'''
    try:
        with open('plugboard dictionary.txt') as f:
            d = {}
            for line in f:
                key, value = line.split(":")
                d[key] = value.strip("\n")
    except FileNotFoundError:
        print("Could not locate file.")

    def plugboard_rev():
        dict_in =  PlugBoard.d
        dict_out = {v: k for k, v in dict_in.items()}

PlugBoard.plugboard_rev()
