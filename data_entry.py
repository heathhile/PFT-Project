from datetime import datetime

date_format = "%d-%m-%Y"


def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strptime(date_str, date_format)
    except ValueError:
        print("Invaid date format, try again..")
        return get_date(prompt, allow_default)

def get_amount():
    pass

def get_category():
    pass

def get_description():
    pass