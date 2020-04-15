#!/usr/bin/env python3

from csvreader import CsvReader

if __name__ == "__main__":
    with CsvReader('good.csv') as file:
        data = file.getdata()
        header = file.getheader()
        print(header)
        for each in data:
            print(each)

    with CsvReader('bad.csv') as file:
        if file == None:
            print("File is corrupted")
        else:
            print("Something went wrong")


    

   