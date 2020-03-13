import csv
import argparse
import sys

parser = argparse.ArgumentParser(description='Convert a GSLIB format to CSV format')

parser.add_argument('-i','--input', required=False, type=str, default=None, help='Name of the GSLIB file. If it is not provided, standard input is assumed')
parser.add_argument('-o','--output', required=False, type=str, default=None, help='Name of the CSV file. If it is not provided, standard output is assumed')
parser.add_argument('-d','--delimiter', required=False, type=str, default=',', help='delimiter of the CSV file')

if __name__ == '__main__':
    args = parser.parse_args()

    if args.input is not None:
        fd_gslib = open(args.input)
    else:
        fd_gslib = sys.stdin

    if args.output is not None:
        fd_csv = open(args.output)
    else:
        fd_csv = sys.stdout


    reader = csv.reader(fd_gslib,delimiter=' ',skipinitialspace=True) #GSLIB uses space as delimiter
    writer = csv.writer(fd_csv,delimiter=args.delimiter)

    #read file title
    title = next(reader)
    #read number of variables
    row = next(reader)
    n_cols = int(row[0])
    #read name of variables
    var_names = []
    for i in range(n_cols):
        row = next(reader)
        name = ' '.join(row) #trick to join each separated text with spaces
        var_names += [name.strip()]

    #write column names
    writer.writerow(var_names)

    #read values
    for row in reader:
        writer.writerow(row[:n_cols])
