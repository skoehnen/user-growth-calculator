import sys
import pandas
import logging
import datetime

from dateutil.relativedelta import *

logging.basicConfig(level=logging.INFO)


def getStartDate(data):
    return data['Date'].loc[data.index[0]]


def getEndDate(data):
    return data['Date'].loc[data.index[-1]]


def getDateRange(startDate, endDate):
    return pandas.date_range(start = startDate, end = endDate + relativedelta(months=+1), freq ='MS')


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


def calculateMonthlyUsers(data, dateRange):
    monthList = []
    userCountPerMonth = []

    for i in zip(dateRange[:-1], dateRange[1:]):
        filtered_df = data.loc[(data['Date'] >= i[0]) & (data['Date'] < i[1])]
        print(f"{i[0].strftime('%Y-%m')}: {len(filtered_df)}")
        monthList.append(i[0].strftime('%Y-%m'))
        userCountPerMonth.append(len(filtered_df))

    print(monthList)
    print(userCountPerMonth)

    return pandas.DataFrame(zip(monthList, userCountPerMonth), columns=['Month', 'Number of user'])


def main(argv):
    logging.info("Main function called")
    splitArguments = splitArgv(argv)
    data = read_csv_file(splitArguments["filename"])

    usersPerMonth = calculateMonthlyUsers(data, getDateRange(getStartDate(data), getEndDate(data)))

    usersPerMonth.to_csv("test.csv")

if __name__ == '__main__':
    print("User growth calculator")
    # Read input file-name from command parameter
    inputFile = sys.argv[1]
    logging.info(f"argv: {sys.argv}")
    main(sys.argv)