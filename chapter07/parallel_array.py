def main():
    file = open('parallel.txt', 'w')
    standard = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h',
                'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p',
                'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x',
                'Y', 'y', 'Z', 'z', ' ', '!', '.', ',', '?']

    secret = ['-', 'w', '#', 'D', '@', 'e', '$', 'B', '&', 'p', ')', '(', 'C', '%', 'E', 'P',
              '*', 'G', 'v', 'X', 'z', '^', '_', 'd', 'S', '+', 'L', 'H', 'h', '>', '<', ':',
              'A', 'Z', 'W', 'g', 'o', '~', '=', 'T', 't', 'x', '{}', '[]', '|', 'Y', 'y', 'c'
              'O', '4', '6', '3', ' ', '!', '.', ',', '?']

    phrase = input('Please enter your secret phrase to be encoded: ')
    coded_phrase = ""
    for letter in phrase:
        for item in range(len(standard)):
            if letter == standard[item]:
                coded_phrase += (secret[item] + "")
    print(coded_phrase)
    file.write(coded_phrase)
    file.close()


main()
