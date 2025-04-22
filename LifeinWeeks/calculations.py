import datetime as dt

class Date:
    
    def __init__(self, date):
        self.date = date
        self.year = date.year
        self.month = date.month
        self.cal_week = date.isocalendar().week
        
        if ((self.month == 1 and self.cal_week == 52)
            or
            (self.month == 12 and self.cal_week == 1)):
            self.year += 1
            self.cal_week = 0
 
        
    def __str__(self):
        return (f"{self.date}")


def calculate_weeks(birthday: dt.date, date: dt.date, verbose: bool):
    
    print(f"calculate_weeks: {birthday = }, {date = }")
    
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
    
    print(f"{birthday.month = }")
    print(f"{birthday.cal_week = }")
    print(f"{birthday.year = }")
    
    print(f"{date.month = }")
    print(f"{date.cal_week = }")
    
    print(deltas)

    if  deltas["tot_days"] < 0:
        print(f"The date was {deltas["tot_days"]} days before you were born.")
        return 0
    
    """
    # Control for the fact that the week of the final week of a year can be labled as week = 1
    if (birthday.isocalendar().week == 1 and birthday.month == 12):
        deltas["cal_weeks"] = date.isocalendar().week - 53
        print("Test")
        
    elif (birthday.isocalendar().week == 52 and birthday.month == 1):
        pass
        
    if (date.isocalendar().week == 1 and date.month == 12):
        deltas["cal_weeks"] = 53 - birthday.isocalendar().week
        print("Test 2")
        
    elif (date.isocalendar().week == 52 and date.month == 1):
        pass
    """

    
    print(deltas)
    
    # Birthday in Year after last birthday (add weeks of last year)
    if deltas["cal_weeks"] == 0:
        output["weeks"] = 52
        output["years"] = deltas["years"] - 1 
        
        # print("The date is in the week of your birthday:")
        
    elif deltas["cal_weeks"] > 0:
        output["weeks"] = deltas["cal_weeks"]
        output["years"] = deltas["years"]
        
    elif deltas["cal_weeks"] < 0:
        output["weeks"] = 52 + deltas["cal_weeks"]
        output["years"] = deltas["years"] - 1
    

        

    print(f"Date: {date}")
    print(f"Year: {output['years']}\nWeek: {output['weeks']}")
    
    if verbose:
        print("Actual Numbers")
    
    return 0