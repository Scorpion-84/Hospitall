
#تعریف کلاس به تعداد موجودیت ها و رابطشون

#region class role
class Sick:
    
    def __init__(self, code, name, family, username, password, type_of_disease, doctor_name, role):
        
        self.code = code
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.type_of_disease = type_of_disease
        self.doctor_name = doctor_name
        self.role = role
        
    def __repr__(self):
        return f"Code: [{self.code}]  Name: {self.name}  Last Name: {self.family}   Type Of Disease: {self.type_of_disease}  Doctor Name: {self.doctor_name}   Role Of Person: {self.role}"
        
    
class Doctor:
    
    def __init__(self, code, name, family, username, password, time_visit, role):
        
        self.code = code
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.time_visit = time_visit
        self.role = role
    
    def __repr__(self):
        return f"Code: [{self.code}]  Name: {self.name}   Last Name: {self.family}   Date Of Visit: {self.time_visit}   Role: {self.role}"
    
    
class Employee:
    
    def __init__(self, code, name, family, username, password, role):
        
        self.code = code
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.role = role
    
    def __repr__(self):
        return f"Code: [{self.code}]   Name: {self.name}   Last Name: {self.family}    Role: {self.role}"
    
    
class Visit:
    
    def __init__(self, code, date, doctor_name, sick_name, status):
        
        self.code = code
        self.date = date
        self.doctor_name = doctor_name
        self.sick_name = sick_name
        self.status = status
        
    def __repr__(self):
        return f"Code: [{self.code}]   Date: {self.date}    Doctor Name: {self.doctor_name}   Sick Name: {self.sick_name}    Status: {self.status}"
    
    
class Payment:
    
    def __init__(self, code, code_of_visit, date, sum_price, status):
        
        self.code = code
        self.code_of_visit = code_of_visit
        self.date = date
        self.sum_price = sum_price
        self.status = status
        
    def __repr__(self):
        return f"Code: [{self.code}]   Sick Name: {self.code_of_visit}   Date: {self.date}   Sum Price: {self.sum_price}   Status: {self.status}"
    
    
    
    
#endregion