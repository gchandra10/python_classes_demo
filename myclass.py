class Classroom:
    def __init__(self):
        self.number = None
        self.building = None
        self.size = None
        self.floor = None
    
    def printClass(self):
        return self.number,self.building
    

class Faculty:
    def __init__(self):
        self.name = None
        self.course = None
    
    def printFaculty(self):
        return self.name,self.course
    
class helper:
    @staticmethod
    def cleanNames(name):
        return (name.title())
    
    @staticmethod
    def cleanPhonenumber(num):
        num_str = str(num)
        return '-'.join([num_str[i:i+3] for i in range(0, len(num_str), 3)])
