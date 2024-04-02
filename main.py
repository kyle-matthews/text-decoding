def decode(message_file):
    #Opens text file specified by user.
    with open(message_file, 'r') as file: 
        lines = file.readlines()
    
    pyramid = []
    for line in lines:
        num, word = line.strip().split(' ')
        pyramid.append(word)

    decoded_message = ''
    index = 0
    for i in range(1, len(lines)):
        print(f"Index: {index}, Word: {pyramid[index]}")
        decoded_message += pyramid[index] + ' '
        index += i
        if index >= len(pyramid):
            break
    return decoded_message.strip()

#Example:
decoded_message = decode('coding_qual_input.txt')
print(decoded_message)