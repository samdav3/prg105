def main():
    file = open('parallel.txt', 'w')
    standard = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h',
                'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p',
                'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x',
                'Y', 'y', 'Z', 'z', ' ', '!', '.', ',', '?']

    secret = ['-', 'w', '#', 'D', '@', 'e', '$', 'B', '&', 'p', ')', '(', 'C', '%', 'E', 'P',
              '*', 'G', 'v', 'X', 'z', '^', '_', 'd', 'S', '+', 'L', 'H', 'h', '>', '<', ':',
              'A', 'Z', 'W', 'g', 'o', '~', '=', 'T', 't', 'x', '{}', '[]', '|', 'Y', 'y', 'c'
              'O', '4', '6', '3', 'K', ' ', '!', '.', ',', '?']
    outline = []
    print('This program will take your phrase and turn it into a secret code.')
    phrase = input('Please enter your secret phrase to be encoded: ')

    for letter in phrase:
        letter_index = standard.index(letter)
        secret_value = secret[letter_index]
        outline.append(secret_value)
    print(outline)

    for item in outline:
        file.write(str(item + '\n'))
    file.close()


main()
