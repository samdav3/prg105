print('This program will decode a coded text file.')


def main():

    standard = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h',
                'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p',
                'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x',
                'Y', 'y', 'Z', 'z', ' ', '!', '.', ',', '?']

    secret = ['-', 'w', '#', 'D', '@', 'e', '$', 'B', '&', 'p', ')', '(', 'C', '%', 'E', 'P',
              '*', 'G', 'v', 'X', 'z', '^', '_', 'd', 'S', '+', 'L', 'H', 'h', '>', '<', ':',
              'A', 'Z', 'W', 'g', 'o', '~', '=', 'T', 't', 'x', '{}', '[]', '|', 'Y', 'y', 'c',
              'O', '4', '6', '3', ' ', '!', '.', ',', '?']

    outline = []

    file = input('Please enter the name of the file to decode: ')

    try:
        in_file = open(f'{file}', 'r')
        in_file.readline()
        for all_lines in in_file:
            all_lines = all_lines.rstrip('\n')
            for letter in all_lines:
                encoded_index = secret.index(letter)
                decoded_index = standard[encoded_index]
                outline.append(decoded_index)
                out_str = ''.join([str(item) for item in outline])
                print(out_str)
    except FileNotFoundError:
        print('File was not found, please try a different filename.')
        main()


main()
