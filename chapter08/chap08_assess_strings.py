

def main():
    overdue = open('over90.txt', 'r')
    accounts = open('accounts.txt', 'r')
    for line in accounts:
        line = line.rstrip('\n')
        account = line.split()
        account_li = account[0:]
        for lines in overdue:
            lines = lines.rstrip('\n')
            due = lines.split()
            overdue_li = due[0:]
            if overdue_li in account_li:
                overdue_li += account_li
                print(overdue_li)

    accounts.close()
    overdue.close()


main()
