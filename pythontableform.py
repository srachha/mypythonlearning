from tabulate import tabulate

table = [['First Name', 'Last Name', 'Age'], ['John', 'Smith', 39], ['Mary', 'Jane', 25], ['Jennifer', 'Doe', 28]]

def printingtable():
    tabledata = f.write(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
    return tabledata

with open('tablesprint.txt','w') as f:
    printingtable()


f.close()