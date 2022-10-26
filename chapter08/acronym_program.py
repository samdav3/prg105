print('This program accepts a phrase and returns the acronym.')
phrase = input('Please enter a phrase to convert: ')
phrase = phrase.split()
acronym = ''
for word in phrase:
    acronym += word[0]
    acronym = acronym.upper()
print(f'{acronym}')
