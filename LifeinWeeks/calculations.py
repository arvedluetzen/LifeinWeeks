import datetime as dt




def calculate_weeks(birthday: dt.date, date: dt.date, verbose: bool):
    
    print(f"calculate_weeks: {birthday = }, {date = }")
    
    deltas = {
        "tot_days": 0,
        "cal_weeks": 0,
        "years": 0,

        }
    
    
    deltas["tot_days"] = date - birthday
    deltas["cal_weeks"] = date.isocalendar().week - birthday.isocalendar().week
    deltas["years"] = date.year - birthday.year
    
    print(deltas)



    if  deltas["tot_days"] < 0:
        print(f"The date was {deltas["tot_days"]} days before you were born.")
        return 0
    
    
    # Delta Years

    # Delta Weeks

    # Control for Weirdness around new years
   
    if verbose:
        print("Actual Numbers")
    
    return 0