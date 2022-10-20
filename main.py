import sys
import pandas
import logging

logging.basicConfig(level=logging.INFO)

def read_csv_file(fileName):
    logging.info("Read csv function called")

if __name__ == '__main__':
    print("User growth calculator")
    # Read input file-name from command parameter
    inputFile = sys.argv[1]
    logging.info(f"Input file: {inputFile}")
    print(inputFile)