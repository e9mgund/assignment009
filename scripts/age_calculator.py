import datetime

def ageCalculator():
    try:
        dob = list(map(int,input("Please enter date of birth in the format [YYYY-MM-DD]: ").strip().split("-")))
        return datetime.date.today().year - datetime.date(dob[0],dob[1],dob[2]).year
    except Exception as e:
        print(e)

print(ageCalculator())