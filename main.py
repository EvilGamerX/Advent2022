from Day01.solution import day01
from Day02.solution import day02
from Day03.solution import day03
from Day04.solution import day04
from Day05.solution import day05
from Day06.solution import day06

option = input('Which day would you like to run?\n')

days = {
        '01': day01,
        '02': day02,
        '03': day03,
        '04': day04,
        '05': day05,
        '06': day06
    }

def notFound():
    print('Day not found, please try again.\n')

def switcher(x):
    return days.get(x, notFound)

switcher(option)()

