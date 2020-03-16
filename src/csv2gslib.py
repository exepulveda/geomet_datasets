
'@author Exequiel Sepulveda https://github.com/exepulveda'
import csv
import argparse
import sys

parser = argparse.ArgumentParser(description='Convert a CSV format to GSLIB format')

parser.add_argument('-i','--input', required=False, type=str, default=None, help='Name of the CSV file. If it is not provided, standard input is assumed')
parser.add_argument('-o','--output', required=False, type=str, default=None, help='Name of the GSLIB file. If it is not provided, standard output is assumed')
parser.add_argument('-d','--delimiter', required=False, type=str, default=',', help='delimiter of the CSV file')
parser.add_argument('-t','--title', required=False, type=str, default='Generated GSLIB file from CSV', help='Title of the GSLIB file')


if __name__ == '__main__':
    args = parser.parse_args()

    print(args)

    if args.input is not None:
        fd_csv = open(args.input)
    else:
        fd_csv = sys.stdin

    if args.output is not None:
        fd_gslib = open(args.output)
    else:
        fd_gslib = sys.stdout


    reader = csv.reader(fd_csv,delimiter=args.delimiter,skipinitialspace=True)
    writer = csv.writer(fd_gslib,delimiter=' ',quoting=csv.QUOTE_MINIMAL) #GSLIB uses space as delimiter
    #first row has the column names
    colnames = next(reader)

    #write file title
    fd_gslib.write(args.title+"\n")
    #write numbers of columns
    writer.writerow([len(colnames)])
    #write name of columns
    for varname in colnames:
        fd_gslib.write(varname+"\n")
    #write data
    for row in reader:
        writer.writerow(row)
