

def decode(message_file):
    with open(message_file, 'r') as file: 
        lines = file.readlines()
    pyramid = []
    