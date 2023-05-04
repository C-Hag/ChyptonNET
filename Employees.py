class Employees:
    
        def __init__(self, name, department, role, salary, years_employeed):
                self.name = name
                self.department = department
                self.role = role
                self.salary = salary
                self.years_employeed = years_employeed
        
        def eligible_for_retirement(self):
                if self.years_employed >= 20:
                        return True
                
                else: 
                        return False