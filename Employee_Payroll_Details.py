print('*******************EMPLOYEE PAYROLL**************************')
print('')
n=int(input('Enter the number of employees ='))
print('')
payroll={x:[] for x in range(1,n+1)}
for i in range(1,n+1):
    employee_num=input('Enter the employee Id  =')
    payroll[i].append(employee_num)
    employee=input('Enter the name of employee =')
    payroll[i].append(employee)
    employee_joining=input('Enter the date of joining =')
    payroll[i].append(employee_joining)
    employee_salary=int(input('Enter the salary ='))
    payroll[i].append(employee_salary)
    print('______________________')
print('*********************************************')
print('To see the employee details         : Press 1')
print('')
print('To see the salary of employee       : Press 2')
print('')
print('To see the date of joining          : Press 3')
print('')
print('To search details using NAME or ID  : Press 4')
print('')
print('To update the employee detail       : Press 5')
print('*********************************************')
while(True):
    s=str(input('Enter the number to display ='))
    print('------------------------------------')
    if s=='1':
        for j in range(1,n+1):
            print('ID.No           :',payroll[j][0])
            print('Name            :',payroll[j][1])
            print('Date of joining :',payroll[j][2])
            print('Salary          :',payroll[j][3])
            print('_______________________________')
    elif s=='2':
        for j in range(1,n+1): 
            print('ID.No   :',payroll[j][0])
            print('Name    :',payroll[j][1])
            print('Salary  :',payroll[j][3])
            print('_______________________________')
    elif s=='3':
        for j in range(1,n+1):
            print('ID.No           :',payroll[j][0])
            print('Name            :',payroll[j][1])
            print('Date of joining :',payroll[j][2])
            print('_______________________________')
    elif s=='4':
        a=str(input('Enter the name or ID to be Searched :'))
        print('_______________________________')
        for j in range(1,n+1):
            for k in range(0,n):
                if a==payroll[j][k]:
                    print('ID.No           :',payroll[j][0])
                    print('Name            :',payroll[j][1])
                    print('Date of joining :',payroll[j][2])
                    print('Salary          :',payroll[j][3])
                    print('_______________________________')
                    break
    elif s=='5':
        a=input('Enter the NAME to change his/her details :')
        print('_______________________________')
        for j in range(1,n+1):
            for k in range(0,n):
                if a==payroll[j][k]:
                    print('ID.No           :',payroll[j][0])
                    print('Name            :',payroll[j][1])
                    print('Date of joining :',payroll[j][2])
                    print('Salary          :',payroll[j][3])
                    print('_______________________________')
                    print('')
                    print('To change ID     :Press 1')
                    print('To change Name   :press 2')
                    print('To change date   :Press 3')
                    print('To change salary :Press 4')
                    press=input('Enter the number to be changed :')
                    if press=='1':
                        new=input('enter the new id :')
                        payroll[j][0]=new
                    elif press=='2':
                        new=input('Enter the new Name :')
                        payroll[j][1]=new
                    elif press=='3':
                        new=input('Enter the new Date :')
                        payroll[j][2]=new
                    elif press=='4':
                        new=int(input('Enter the changed Salary'))
                        payroll[j][3]=new
                    print('**********************')
                    print('Updated Successfully :)')
                    print('Id     :',payroll[j][0])
                    print('Name   :',payroll[j][1])
                    print('Date   :',payroll[j][2])
                    print('Salary :',payroll[j][3])
                    print('**********************')   
    else:
        print('*********************************************')
        print('To see the employee details         : Press 1')
        print('')
        print('To see the salary of employee       : Press 2')
        print('')
        print('To see the date of joining          : Press 3')
        print('')
        print('To search details using NAME or ID  : Press 4')
        print('')
        print('To update the employee detail       : Press 5')
        print('*********************************************')
