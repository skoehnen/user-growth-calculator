import sys
import pandas
import logging
import datetime

logging.basicConfig(level=logging.INFO)

def read_csv_file(fileName):
    logging.info("Read csv function called")
    logging.info(f"Reading from {fileName}")

    return pandas.read_csv(fileName)

def splitArgv(argv):
    logging.info("splitArgv function called")
    if len(argv) != 2:
        logging.critical("Not the correct number of arguments")
        raise Exception("Not the correct number of arguments")
    else:
        return {"filename": argv[1]}

def main(argv):
    logging.info("Main function called")
    splitArguments = splitArgv(argv)
    print(splitArguments)
    data = read_csv_file(splitArguments["filename"])
    print(data)

if __name__ == '__main__':
    print("User growth calculator")
    # Read input file-name from command parameter
    inputFile = sys.argv[1]
    logging.info(f"argv: {sys.argv}")
    main(sys.argv)