import argparse

from .dateparser import parse_date
from .calculations import calculate_weeks


def main():
    
    parser = argparse.ArgumentParser(description='Calculate Weeks')
    
    parser.add_argument('birthday', help="Specify the date you were born")
    
    parser.add_argument("-d", "--dates", help="Directly specify dates you want to be calculated")
    
    parser.add_argument("-c", "--continuous", help="Will let you calculate dates continuously.",
                        action="store_true")
    
    parser.add_argument("-v", "--verbose", help="Output also corrected calculations.",
                        action="store_true")
    
    
    args = parser.parse_args()
    
    birthday = parse_date(args.birthday)[0]
    
    if not birthday:
        raise ValueError("Birthday had a format that could not be parsed")
    
    if args.dates is not None:
        for date in parse_date(args.dates):
            calculate_weeks(birthday, date, args.verbose)
        
    elif not args.input:
        calculate_weeks(birthday, parse_date("now")[0], args.verbose)
        

    if args.input:
        
        active = True
        while active:
            date_input = input("Input dates or exit to quit: ")
            
            if "exit" in date_input.lower():
                print("Exiting")
                active = False
                continue
            
            for date in parse_date(date_input):
                calculate_weeks(birthday, date, args.verbose)


    return 0