

def main():
    total = 0.0
    entries = 0
    num_list = open('num_list.txt', 'r')
    all_lines = num_list.readline()
    while all_lines != '':
        all_lines = all_lines.rstrip('\n')
        lines = float(all_lines)
        print(f'{lines:,.2f}')
        all_lines = num_list.readline()
        total += lines
        entries += 1
    average = total / entries
    print(f'Total: {total:,.2f} ')
    print(f'Total entries: {entries}')
    print(f'Average: {average:,.2f}')
    num_list.close()


main()
