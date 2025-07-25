from model.entity.user_entity import Employee, Visit, Payment

user_1 = Employee(56, 'Mahdi', 'Salimi', 'Scorpion', 'mm.salimi84', 'Employee')

print(user_1)


user_1 = Visit(56, '2025/05/23', 'Ali Afshari', 'Mahdi Salimi','Visited')

print(user_1)


user_1 = Payment(56, 'Ali Afshari', '2025/05/23', '1850000', 'Paid')

print(user_1)



