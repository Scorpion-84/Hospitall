
#تعریف کلاس به تعداد موجودیت ها و رابطشون

class Sick():
    
    def __init__(self, code, name, family, username, password, date_of_visit, type_of_disease, doctor_name, role):
        
        self.code = code
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.date_of_visit = date_of_visit
        self.type_of_disease = type_of_disease
        self.doctor_name = doctor_name
        self.role = role
    
class Doctor():
    
    def __init__(self, code, name, family, username, password, time_visit, sick_name, role):
        
        self.code = code
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.time_visit = time_visit
        self.sick_name = sick_name
        self.role = role
    
class Employee():
    
    def __init__(self, code, name, family, username, password, role):
        
        self.code = code
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.role = role
    
class Visit():
    
    def __init__(self, code, ):
        pass
    
class Payment():
    
    def __init__(self):
        pass