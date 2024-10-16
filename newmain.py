from myclass import helper
from myclass import Faculty

ofaculty = Faculty()
ofaculty.name = "g"

helper.cleanNames(ofaculty.name)

def print_items():
    print(helper.cleanNames("ganesh"))
    print(helper.cleanPhonenumber("123232342"))
    
print_items()

