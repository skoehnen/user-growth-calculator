import sys
import pandas
import logging
import datetime

from dateutil.relativedelta import *

logging.basicConfig(level=logging.INFO)

def getDateRange(startDate, endDate):
    return pandas.date_range(start = startDate, end = endDate, freq ='MS')

def read_csv_file(fileName):
    logging.info("Read csv function called")
    logging.info(f"Reading from {fileName}")

    return pandas.read_csv(fileName, parse_dates=[0], sep=";")

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

    startDate = data['Date'].loc[data.index[0]]
    endDate = data['Date'].loc[data.index[-1]]
    
    print(f"startDate: {startDate}")
    print(f"endDate: {endDate}")

    start_date_range = getDateRange(startDate, endDate)

    print(start_date_range)

    startDate = startDate+relativedelta(months=+1)
    print(startDate)

    example_date_string="20220929"
    #obj=datetime.datetime.strptime(string, format)
    #data[foo..str.startswith('f')]
    filtered_df = data.loc[(data['Date'] >= '2020-04-01')
                     & (data['Date'] < '2020-05-01')]

    #print(filtered_df)
    print(len(filtered_df))

if __name__ == '__main__':
    print("User growth calculator")
    # Read input file-name from command parameter
    inputFile = sys.argv[1]
    logging.info(f"argv: {sys.argv}")
    main(sys.argv)