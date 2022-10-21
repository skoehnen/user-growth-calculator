import sys
import pandas
import logging
import datetime

from dateutil.relativedelta import *

logging.basicConfig(level=logging.DEBUG)


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
    logging.debug("calculateMonthlyUsers function called")

    monthList = []
    userCountPerMonth = []

    for i in zip(dateRange[:-1], dateRange[1:]):
        filtered_df = data.loc[(data['Date'] >= i[0]) & (data['Date'] < i[1])]
        monthList.append(i[0].strftime('%Y-%m'))
        userCountPerMonth.append(len(filtered_df))

    return pandas.DataFrame(zip(monthList, userCountPerMonth), columns=['Month', 'Number of users'])


def calculateAverageGrowthRate(data):
    logging.debug(f"calculateAverageGrowthRate function called")
    
    n = 2
    averageGrowthRates = [0]

    for present in (data['Number of users'])[1:]:
        past = data['Number of users'][0]
        logging.debug(f"Past value: {past}")
        logging.debug(f"Present value: {present}")
        logging.debug(f"n value: {n}")

        averageGrowthRate = (((float(present) / float(past)) ** (1.0 / float(n))) - 1.0) * 100.0

        averageGrowthRates.append(averageGrowthRate)

        print(averageGrowthRate)

        n += 1

    print(averageGrowthRates)

    data['Average Growth Rates'] = averageGrowthRates

    print(data)

    return data

def main(argv):
    logging.debug("Main function called")
    splitArguments = splitArgv(argv)
    data = read_csv_file(splitArguments["filename"])

    usersPerMonth = calculateMonthlyUsers(data, getDateRange(getStartDate(data), getEndDate(data)))

    averageGrowthRates = calculateAverageGrowthRate(usersPerMonth)

    averageGrowthRates.to_csv("test.csv")

if __name__ == '__main__':
    print("User growth calculator")
    # Read input file-name from command parameter
    inputFile = sys.argv[1]
    logging.info(f"argv: {sys.argv}")
    main(sys.argv)