file = open('tale_of_two_cities.txt', 'r')

all_lines = file.readline()
count = 1
words_dictionary = {}
k_v_exchanged = []
for keys in file:
    words_dictionary[all_lines] = keys
    keys.rstrip('\n')

    for key, val in words_dictionary.items():
        if val not in k_v_exchanged:
            k_v_exchanged.append(val)
            words_dictionary[key] = val
            val.rstrip('\n')
            print(val)
