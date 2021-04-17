work_hours = [('Hrishab',100),('Ajay',20),('Rahul',15)]

def best_employee(work_hours):
    max_hrs = 0
    employee_name = ''
    for name,hrs in work_hours:
        if(hrs>max_hrs):
            employee_name = name
            max_hrs = hrs
        else:
            pass
    return (employee_name,max_hrs) 

result = best_employee(work_hours)
name,hrs = best_employee(work_hours)
print(f'Best Employee : {result}')
print(f'Best Employee Name: {name}')