# 11.1 & 11.2

from zoo import A
menagerie = A
menagerie.hours()


# Setup for 16.8
import csv
with open('books.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print('\n',row['author'], row['book'])

# I still need to finish the 16.8 problem
