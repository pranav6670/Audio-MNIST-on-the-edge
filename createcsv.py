import os, csv

f = open('train.csv', 'r+')
w = csv.writer(f)
for path, dirs, files in os.walk('recordings'):
    for filename in files:
        w.writerow([filename])


