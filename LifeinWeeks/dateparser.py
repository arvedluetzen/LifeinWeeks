import datetime as dt


def parse_date(dates_str: str) -> list[dt.date]:
    
    print(f"parse_date: {dates_str}")
    
    dates = dates_str.split()
    
    date_list = []
    
    for date in dates:
        if date := to_date(date):
            date_list.append(date)
        
    return date_list

    

def to_date(date_str: str) -> dt.date:
    
    formats = (
                "%Y-%m-%d", # Example: 2025-04-22
                "%d-%m-%Y", # Example: 22-04-2025
                "%m/%d/%Y", # Example: 04/22/2025
                "%d.%m.%Y" # Example: 03.05.2024
                )

    
    
    if date_str.lower() == "now":
        return dt.datetime.now().date()
    
    else:
        for format in formats:
            try:
                date = dt.datetime.strptime(date_str, format).date()
                return date
            except:
                continue
    
    print(f"{date_str} could not be parsed.")  
    return None


if __name__ == "__main__":
    
    print("Test to_date:")
    
    print(f"{to_date("now") = }")
    print(f"{to_date("22.04.2025") = }")
    print(f"{to_date("22-04-2025") = }")
    print(f"{to_date("2025-04-22") = }")
    print(f"{to_date("2025-04-22") = }")
    print(f"{to_date("aklsdgjöa") = }")
    
    print()
    print("Test parse_date:")
    
    print(f"{parse_date("") = }")
    print(f"{parse_date("now") = }")
    print(f"{parse_date("21.04.2025") = }")
    print(f"{parse_date("22-04-2025") = }")
    print(f"{parse_date("2025-04-22") = }")
    print(f"{parse_date("now 21.04.2025 22-04-2025") = }")
    print(f"{parse_date("nowd 21.04.2adg25 22-04-2025") = }")
    

    

