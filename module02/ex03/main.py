from csvreader import CsvReader
import sys

if __name__ == "__main__":
    with CsvReader('good.csv', skip_top=0) as file:
        if file is None:
            print('File is corrupted')
            sys.exit(1)
        data = file.getdata()
        header = file.getheader()
    print(data)
    print(header)
