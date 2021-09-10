from flask import Flask
import csv
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello it's Catherine!"

def readCsv():
    filepath = './data/test_good.csv'
    ext = os.path.splitext(filepath)[-1].lower()
    if ext == '.csv':
        print(filepath, 'is a CSV file :)')
    else:
        print(filepath, 'is NOT a CSV file :(')
        print('\nTHE END\n')

    with open(filepath, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        numRows = len(list(reader))
        print(filepath, 'has', numRows, 'rows')
        for row in reader:
            numCol = len(row)
            print(row, 'has ', numCol, ' columns') # not sure why this isn't printing
    
    print('\nTHE END\n')

readCsv()

if __name__ == '__main__':
    app.run()