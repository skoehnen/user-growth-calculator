import sys
import pandas
import logging

logging.basicConfig(level=logging.INFO)

def read_csv_file(fileName):
    print("Read csv function")

if __name__ == '__main__':
    print("User growth calculator")
    # Read input file-name from command parameter
    inputFile = sys.argv[1]
    logging.info(f"Input file: {inputFile}")
    print(inputFile)