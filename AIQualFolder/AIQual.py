#This project reads a text file consisting of numbers and words for example '1 app'. it then creates a 
#pyramid with the numbers, for example:
#  1
# 2 3
#4 5 6
#The last number of each level of the pyramid correlates to a word in the
#text file that reveals a secret message. The decode function finds that message.

file = open(r"*path*/coding_qual_input.txt", "r")

message_file = file.read().splitlines()

def decode(message_file):
    word_nums = []

    num_amnt = 0
    level = 0

    while num_amnt < len(message_file):

        level += 1

        for x in range(level):
            num_amnt += 1

        word_nums.append(str(num_amnt))

    message_file = sorted(message_file, key=lambda x: int("".join([i for i in x if i.isdigit()])))
    message_file = [' ' + x for x in message_file]

    words = []

    for i in message_file:
        for j in word_nums:
            if (' ' + j + ' ') in i:
                words.append(i)

    final = str.maketrans('', '', '1234567890, ')
    words = [s.translate(final) for s in words]

    print(*words)

decode(message_file)

