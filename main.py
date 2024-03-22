#!/usr/bin/env python

# calculate and display days ramiaining till your next birth day
# if actual birth day is on a leap year on february 29,
# then birth day on a non leap year is calculated as if birth day is on February 28th.
import datetime as dt

def get_birth_month():
    '''
    input --> none
    output --> birth month
    validate user input and if valid, returns birth month
    '''
    while True:
        try:
            birth_month = int(input("Enter your birth month(1 - 12): "))
            if birth_month <= 12 and birth_month >=1:
                return birth_month
            else:
                print("Please type a valid month(1 - 12)!")
                continue
        except ValueError:
            print("Not a number!")
            continue

def is_leap_year(year):
    '''
    input --> year
    output --> boolean True or False
    check whether an year is leap or not and returns True or False
    '''
    if (year % 4 == 0) and (not (year % 100 == 0) or (year % 400 == 0)):
        return True
    else:
        return False


def get_birth_day(birth_month):
    '''
    input --> birth_month
    output --> birth day
    validate user input and returns valid day number
    '''
    not_leap = {1: list(range(1, 32)), 2: list(range(1, 29)), 3: list(range(1, 32)),
                4: list(range(1, 31)), 5: list(range(1, 32)), 6: list(range(1, 31)),
                7: list(range(1, 32)), 8: list(range(1, 32)), 9: list(range(1, 31)),
                10: list(range(1, 32)), 11: list(range(1, 31)), 12: list(range(1, 32))}
    leap = {2: list(range(1, 30))}

    current_year = dt.date.today().year

    while True:
        try:
            birth_day = int(input("Enter the birth day: "))
            if birth_month == 2 and is_leap_year(current_year):
                if birth_day in leap[birth_month]:
                    return birth_day
                else:
                    print("Not a valid day!")
                    continue
            elif is_leap_year(current_year) or not is_leap_year(current_year):
                if birth_day in not_leap[birth_month]:
                    return birth_day
                else:
                    print("Not va valid day!")
                    continue
            else:
                print("Enter a valid day please!")
                continue
        except ValueError:
            print("Enter a valide day please!")
            continue


def get_required_year(birth_month, birth_day):
    '''
    input --> birth_month, birth_day
    output --> required_year
    compute the year in which next birthday resides
    '''
    current_day = dt.date.today().day
    current_month = dt.date.today().month
    current_year = dt.date.today().year

    if birth_month > current_month:
        return current_year
    elif birth_month == current_month and birth_day >= current_day:
        return current_year
    else:
        return current_year + 1


def get_days_remaining(birth_month, birth_day, required_year):
    '''
    input --> birth_month, birth_day and required_year
    output --> number of days left
    calculate number of days left till your next birth day
    if the required year is not leap and if the birth day occurs on leap year february 29,
    then the days remaining is calculated as if birth day is on February 28th
    '''
    current_month = dt.date.today().month
    current_day = dt.date.today().day
    if current_month == birth_month and current_day == birth_day:
        return 0
    if not is_leap_year(required_year) and birth_day == 29:
        birth_day = birth_day - 1
        birth_month = birth_month
        current_date = dt.date.today()
        next_birth_date = dt.date(year=required_year, month=birth_month, day=birth_day)

        days_remaining = str(next_birth_date - current_date).split(',')[0].split(" ")[0]
        return int(days_remaining)
    else:
        current_date = dt.date.today()
        next_birth_date = dt.date(year=required_year, month=birth_month, day=birth_day)

        days_remaining = str(next_birth_date - current_date).split(',')[0].split(" ")[0]

        return int(days_remaining)


def main():
    '''
    driver function
    '''
    print("Hello, today is {:%A %B %d %Y}".format(dt.date.today()))
    print("Welcome to the program!")
    print("Provide your birth month and birth day and you will get")
    print("how many days are left till your next birth day!")
    
    while True:

        choice = input("Do you want to continue? Yes or No: ")

        if choice == "":
            print('invalid choice!')
            continue
        elif choice[0] == 'Y' or choice[0] == 'y':
            birth_month = get_birth_month()
            birth_day = get_birth_day(birth_month)
            required_year = get_required_year(birth_month, birth_day)
            days_left = get_days_remaining(birth_month, birth_day, required_year)

            print("There are {} days left till your next birth day!".format(days_left))
            continue

        elif choice[0] == 'N' or choice[0] == 'n':
            print("Exiting...")
            break
        else:
            print("invalid choice!")
            continue

    print("Thank your for using me. Come and visit again! ")


main()
