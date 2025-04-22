import datetime as dt

class Date:
    
    def __init__(self, date):
        self.date = date
        self.year = date.year
        self.month = date.month
        self.cal_week = date.isocalendar().week
        
        
        if self.month == 1 and self.cal_week == 52:
            self.year -= 1
            print("Warning: Probable Error Arround New Years")
    
        elif self.month == 12 and self.cal_week == 1:
            self.year += 1
            print("Warning: Probable Error Arround New Years")

        elif self.cal_week == 53:
            print("Warning: Probable Error Arround New Years")
            self.cal_week = 52
 
        
    def __str__(self):
        return (f"{self.date}")


def calculate_weeks(birthday: dt.date, date: dt.date, verbose: bool):
    
    # print(f"calculate_weeks: {birthday = }, {date = }")
    
    deltas = {
        "tot_days": 0,
        "cal_weeks": 0,
        "years": 0
        }
    
    output = {
        "years": 0,
        "weeks": 0
    }
    
    date = Date(date)
    birthday = Date(birthday)
    
    deltas["tot_days"] = (date.date - birthday.date).days
    deltas["cal_weeks"] = date.cal_week - birthday.cal_week
    deltas["years"] = date.year - birthday.year
    


    if  deltas["tot_days"] < 0:
        print(f"The date was {deltas["tot_days"]} days before you were born.")
        return 0

    """ Testing purposes
    print(deltas)
    
    print(f"{birthday.month = }")
    print(f"{birthday.cal_week = }")
    print(f"{birthday.year = }")
    
    print(f"{date.month = }")
    print(f"{date.cal_week = }")
    print(f"{date.year = }")
    """
    
    # Birthday in Year after last birthday (add weeks of last year
    if deltas["cal_weeks"] < 0:
        output["weeks"] = 52 + deltas["cal_weeks"]
        output["years"] = deltas["years"] - 1
        
    else:
        output["weeks"] = deltas["cal_weeks"]
        output["years"] = deltas["years"]
    
    
    # This is not very well solved yet.
    if (date.date.day == birthday.date.day) and (date.date.month == birthday.date.month):
        print("It is your birthday.")
        
        if output["weeks"] <= 1:
            output["weeks"] = 52
            output["years"] -= 1
        else:
            output["weeks"] = 52
          
    elif output["weeks"] == 0:
        output["weeks"] = 52
        output["years"] = output["years"] - 1
        
        print("The date is in the week of your birthday:")
        


    print()
    print(f"Date: {date}")
    print(f"Year: {output['years']}\nWeek: {output['weeks']}")
    
    if verbose:
        print("Rounded   vs\t Actual [Weeks]")
        print(f"{output['years']*52 + output['weeks']} \t\t {round(deltas['tot_days'] / 7, 2)}")
    
    return 0