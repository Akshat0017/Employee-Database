#Employee Payroll Management System
#MEMBER- AKSHAT SINGH, 12-D
#        ARYAN ARYAN CHOUDHARY, 12-D
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import random

import mysql.connector

mycon=None
mycursor=None
flag=0
sp=""

def check_connection():

    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aryan"
    )
    if mycon.is_connected():
        print("Successfully connected to MySQL")
        flag=1
    return flag



def create_database():
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="Somerville"
    )

    mycursor = mycon.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS emp_database")
    
    print("Database created or used")

 

def create_table():
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aryan",
      database="emp_database"
    )

    mycursor = mycon.cursor()


    mycursor.execute('''CREATE TABLE IF NOT EXISTS emp_payroll(empid int primary key auto_increment ,employeename varchar(20),department varchar(15),designation varchar(20),gross_salary float(10),hours_worked int(5),overtime_pay float(10),income_tax float(10)
                     ,net_salary float(10),increment float(10))''')


    
def add_new_record():
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aryan",
      database="emp_database"
    )
    mycursor = mycon.cursor()

    empid=int(input("ENTER EMPLOYEE ID:\t"))

    employeename=input("ENTER EMPLOYEE NAME:\t")

    department=input("ENTER DEPARTMENT OF EMPLOYEE:\t")

    designation=input("ENTER DESIGNATION OF EMPLOYEE\t")          

    gross_salary=float(input("ENTER GROSS SALARY OF THE EMPLOYEE\t"))
            
    hours_worked=int(input("ENTER TOTAL HOURS WORKED\t"))

    dif_hour=int(hours_worked-40)
            
    op=((0.05*gross_salary)*dif_hour)

    income_tax=float(0.05*gross_salary)
    
    net_salary=float(gross_salary+op-income_tax)

    increment=float('0')
    
    sql = '''INSERT INTO emp_payroll(empid,employeename,department,designation,gross_salary,hours_worked,overtime_pay,income_tax,net_salary,increment)
            VALUES({},'{}','{}','{}',{},{},{},{},{},{})'''.format(empid,employeename,department,designation,gross_salary,hours_worked,op,income_tax,net_salary,increment)
    
    mycursor.execute(sql)
    
    mycon.commit()

    print(mycursor.rowcount, "record inserted.")
               
    
def space(V):
    global sp
    sp=""
    l=15-len(str(V))
    for i in range(l):
        sp=sp+" "
    return sp

def display_all_record():
    
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aryan",
      database="emp_database"
    )


    mycursor = mycon.cursor()

    mycursor.execute("SELECT * FROM emp_payroll")

    myresult = mycursor.fetchall()
    print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")

    print("| empid",space("empid"),"employeename", space("employeename"),"department",space("department"),"designation",space("designation"),"gross_salary",space("gross_salary"),"hours_worked",space("hours_worked"),"overtime_pay",end=" ")
    print(space("overtime_pay"),"income_tax",space("income_tax"),"net_salary",space('net_salary'),'increment',space('increment')," |")

    
    print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
   
    for x in myresult:
      print('|',x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3],space(x[3]),x[4],space(str(x[4])),x[5],space(str(x[5])),x[6],space(str(x[6])),x[7],space(str(x[7])),x[8],space(str(x[8])),x[9],space(str(x[9])),' |')
      print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
    
    
def search_record():
    
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aryan",
      database="emp_database"
    )


    mycursor = mycon.cursor()
    print('''
***********************************************************************

*          TO SERACH USING EMPLOYEE NAME        1                     *

*          TO SEARCH USING EMPLOYEE ID          2                     *

*          TO SEARCH USING DESIGNATION          3                     *

*          TO SEARCH USING DEPARTMENT           4                     *

*          TO SEARCH USING GROSS SALARY         5                     *

***********************************************************************''')

    print('')
    detail=input('ENTER YOUR CHOICE:\t')
    
    if (detail=='1'):

        print('')

        NAME=input("Enter Employee name to search:\t")

        print('') 
        sql_select_query = "select * from emp_payroll where employeename = %s"

        mycursor.execute(sql_select_query, (NAME, ))

        myresult = mycursor.fetchall()

        if (mycursor.rowcount>0):
            print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")

            print("| empid",space("empid"),"employeename", space("employeename"),"department",space("department"),"designation",space("designation"),"gross_salary",space("gross_salary"),"hours_worked",space("hours_worked"),"overtime_pay",end=" ")
            print(space("overtime_pay"),"income_tax",space("income_tax"),"net_salary",space('net_salary'),'increment',space('increment')," |")
    
            print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
   
            for x in myresult:
                  print('|',x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3],space(x[3]),x[4],space(str(x[4])),x[5],space(str(x[5])),x[6],space(str(x[6])),x[7],space(str(x[7])),x[8],space(str(x[8])),x[9],space(str(x[9])),' |')
                  print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")

        else:

            print("No employee found")

    elif (detail=='2'):
        print('')

        ID=int(input("Enter Employee id to search:\t"))

        print('')
        sql_select_query = "select * from emp_payroll where empid = %s"

        mycursor.execute(sql_select_query, (ID, ))

        myresult = mycursor.fetchall()
        
        if (mycursor.rowcount>0):
            print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")

            print("| empid",space("empid"),"employeename", space("employeename"),"department",space("department"),"designation",space("designation"),"gross_salary",space("gross_salary"),"hours_worked",space("hours_worked"),"overtime_pay",end=" ")
            print(space("overtime_pay"),"income_tax",space("income_tax"),"net_salary",space('net_salary'),'increment',space('increment')," |")
    
            print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
   
            for x in myresult:
              print('|',x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3],space(x[3]),x[4],space(str(x[4])),x[5],space(str(x[5])),x[6],space(str(x[6])),x[7],space(str(x[7])),x[8],space(str(x[8])),x[9],space(str(x[9])),' |')
              print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")

        else:

            print("No employee found")

    elif (detail=='3'):
        print('')

        DESIG=input("Enter Designation to search:\t")

        print('')
        sql_select_query = "select * from emp_payroll where designation = %s"

        mycursor.execute(sql_select_query, (DESIG, ))

        myresult = mycursor.fetchall()
        
        if (mycursor.rowcount>0):
            print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")

            print("| empid",space("empid"),"employeename", space("employeename"),"department",space("department"),"designation",space("designation"),"gross_salary",space("gross_salary"),"hours_worked",space("hours_worked"),"overtime_pay",end=" ")
            print(space("overtime_pay"),"income_tax",space("income_tax"),"net_salary",space('net_salary'),'increment',space('increment')," |")
    
            print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
   
            for x in myresult:
              print('|',x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3],space(x[3]),x[4],space(str(x[4])),x[5],space(str(x[5])),x[6],space(str(x[6])),x[7],space(str(x[7])),x[8],space(str(x[8])),x[9],space(str(x[9])),' |')
              print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")

        else:

            print("No employee found")

    elif (detail=='4'):
        print('')

        DEP=input("Enter Department to search:\t")

        print('')
        sql_select_query = "select * from emp_payroll where department = %s"

        mycursor.execute(sql_select_query, (DEP, ))

        myresult = mycursor.fetchall()
        
        if (mycursor.rowcount>0):
            print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")

            print("| empid",space("empid"),"employeename", space("employeename"),"department",space("department"),"designation",space("designation"),"gross_salary",space("gross_salary"),"hours_worked",space("hours_worked"),"overtime_pay",end=" ")
            print(space("overtime_pay"),"income_tax",space("income_tax"),"net_salary",space('net_salary'),'increment',space('increment')," |")
    
            print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
   
            for x in myresult:
              print('|',x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3],space(x[3]),x[4],space(str(x[4])),x[5],space(str(x[5])),x[6],space(str(x[6])),x[7],space(str(x[7])),x[8],space(str(x[8])),x[9],space(str(x[9])),' |')
              print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")

        else:

            print("No employee found")

    elif (detail=='5'):
        print('')

        print('''
******************************************************************************************

*          TO SERACH GREATER THAN EQUAL TO A CERTAIN SALARY        1                     *

*          TO SERACH LESSER THAN EQUAL TO A CERTAIN SALARY         2                     *

******************************************************************************************''')
        print('')
        val=input('ENTER YOUR CHOICE:\t')

        if (val=='1'):
            print('')
            SAL=int(input("Enter Salary to search:\t"))

            print('')
            sql_select_query = "select * from emp_payroll where gross_salary >= %s"

            mycursor.execute(sql_select_query, (SAL, ))

            myresult = mycursor.fetchall()
        
            if (mycursor.rowcount>0):
                print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")

                print("| empid",space("empid"),"employeename", space("employeename"),"department",space("department"),"designation",space("designation"),"gross_salary",space("gross_salary"),"hours_worked",space("hours_worked"),"overtime_pay",end=" ")
                print(space("overtime_pay"),"income_tax",space("income_tax"),"net_salary",space('net_salary'),'increment',space('increment')," |")
    
                print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
   
                for x in myresult:
                  print('|',x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3],space(x[3]),x[4],space(str(x[4])),x[5],space(str(x[5])),x[6],space(str(x[6])),x[7],space(str(x[7])),x[8],space(str(x[8])),x[9],space(str(x[9])),' |')
                  print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
            else:

                print("No employee found")

        elif (val=='2'):
            print('')
            SAL=int(input("Enter Salary to search:\t"))

            print('')
            sql_select_query = "select * from emp_payroll where gross_salary <= %s"

            mycursor.execute(sql_select_query, (SAL, ))

            myresult = mycursor.fetchall()
        
            if (mycursor.rowcount>0):
                print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")

                print("| empid",space("empid"),"employeename", space("employeename"),"department",space("department"),"designation",space("designation"),"gross_salary",space("gross_salary"),"hours_worked",space("hours_worked"),"overtime_pay",end=" ")
                print(space("overtime_pay"),"income_tax",space("income_tax"),"net_salary",space('net_salary'),'increment',space('increment')," |")
    
                print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
   
                for x in myresult:
                  print('|',x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3],space(x[3]),x[4],space(str(x[4])),x[5],space(str(x[5])),x[6],space(str(x[6])),x[7],space(str(x[7])),x[8],space(str(x[8])),x[9],space(str(x[9])),' |')
                  print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
                  
            else:

                print("No employee found")

    else:
        print('WRONG CHOICE ENTERED')
    
def delete_record():

    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aryan",
      database="emp_database"
    )


    mycursor = mycon.cursor()

    print('''
***********************************************************************

*          TO DELETE USING EMPLOYEE NAME                1             *

*          TO DELETE USING EMPLOYEE ID                  2             *

***********************************************************************''')
    print('')
    detail=input('ENTER YOUR CHOICE:\t')

    if (detail=='1'):
        print('')

        NAME=input("Enter name to delete:\t")

        print('')
        
        sql_select_query = "DELETE FROM emp_payroll WHERE employeename = %s"

        mycursor.execute(sql_select_query, (NAME, ))

        mycon.commit()

        print(mycursor.rowcount, "record(s) deleted from offical details table")
        
        mycon = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="aryan",
          database="emp_database"
        )


        mycursor = mycon.cursor()

        sql_select_query = "DELETE FROM emp_personal WHERE employeename = %s"

        mycursor.execute(sql_select_query, (NAME, ))
            
        mycon.commit()

        print(mycursor.rowcount, "record(s) deleted from personal details table")
            

    elif (detail=='2'):

        print('')

        ID=int(input("Enter employee ID to delete:\t"))

        print('')

        sql_select_query = "DELETE FROM emp_payroll WHERE empid = %s"

        mycursor.execute(sql_select_query, (ID, ))

        mycon.commit()

        print(mycursor.rowcount, "record(s) deleted from offical details table")
        
        mycon = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="aryan",
          database="emp_database"
        )

        mycursor = mycon.cursor()

        sql_select_query = "DELETE FROM emp_personal WHERE empid = %s"

        mycursor.execute(sql_select_query, (ID, ))

        mycon.commit()

        print(mycursor.rowcount, "record(s) deleted from personal details table")
    
    else:
        print('WRONG ENTRY')

def update_record():
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aryan",
      database="emp_database"
    )


    mycursor = mycon.cursor()

    detail=int(input('Enter Employee id for updation:\t'))

    sql_select_query = "select * from emp_payroll where empid = %s"
    
    mycursor.execute(sql_select_query, (detail, ))
    
    myresult = mycursor.fetchall()

    if (len(myresult)!=0):

        print('''
********************************************************************

*     TO UPDATE DEPARTMANT OF THE EMPLOYEE              1          *

*     TO UPDATE DESIGNATION OF THE EMPLOYEE             2          *

*     TO UPDATE SALARY OF THE EMPLOYEE                  3          *

********************************************************************''')
        print('')
        
        sdetail=input("ENTER YOUR CHOICE:\t")
        
        if (sdetail=='1'):
                
            print('')

            NewDept=input("Enter new Department of employee:\t")

            print('')
            sql_select_query = "UPDATE emp_payroll set department =%s WHERE empid = %s"

            input1=(NewDept,detail)
            mycursor.execute(sql_select_query,input1)

            mycon.commit()

            print(mycursor.rowcount, "record(s) updated")

            mycursor.execute("SELECT * FROM emp_payroll")

            myresult = mycursor.fetchall()
    
      
            print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")

            print("| empid",space("empid"),"employeename", space("employeename"),"department",space("department"),"designation",space("designation"),"gross_salary",space("gross_salary"),"hours_worked",space("hours_worked"),"overtime_pay",end=" ")
            print(space("overtime_pay"),"income_tax",space("income_tax"),"net_salary",space('net_salary'),'increment',space('increment')," |")
    
            print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
   
            for x in myresult:
                print('|',x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3],space(x[3]),x[4],space(str(x[4])),x[5],space(str(x[5])),x[6],space(str(x[6])),x[7],space(str(x[7])),x[8],space(str(x[8])),x[9],space(str(x[9])),' |')
                print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")

    
    
        elif (sdetail=='2'):
            print('')    

            NewDesig=input("Enter new Designation of employee:\t")

            print('')

            sql_select_query = "UPDATE emp_payroll set designation =%s WHERE empid = %s"

            input1=(NewDesig,detail)
            mycursor.execute(sql_select_query,input1)

            mycon.commit()

            print(mycursor.rowcount, "record(s) updated")

            mycursor.execute("SELECT * FROM emp_payroll")

            myresult = mycursor.fetchall()
    
       
            print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")

            print("| empid",space("empid"),"employeename", space("employeename"),"department",space("department"),"designation",space("designation"),"gross_salary",space("gross_salary"),"hours_worked",space("hours_worked"),"overtime_pay",end=" ")
            print(space("overtime_pay"),"income_tax",space("income_tax"),"net_salary",space('net_salary'),'increment',space('increment')," |")
    
            print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
   
            for x in myresult:
                print('|',x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3],space(x[3]),x[4],space(str(x[4])),x[5],space(str(x[5])),x[6],space(str(x[6])),x[7],space(str(x[7])),x[8],space(str(x[8])),x[9],space(str(x[9])),' |')
                print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")

        elif (sdetail=='3'):
            print('')
            
            NewSal=float(input("Enter new Salary of employee:\t"))

            print('')
            
            sql_select_query = "select * from emp_payroll where empid = %s"

            mycursor.execute(sql_select_query, (detail, ))

            myresult = mycursor.fetchall()

            for x in myresult:
                hours=int(x[5])
                gsal=float(x[4])
        
            dif_hour=int(hours-40)
            
            newop=(0.05*dif_hour*int(NewSal))
        
            newtax=(0.05*int(NewSal))
            
            newnetsal=(NewSal+newop-newtax)

            increment=(NewSal-gsal)

            sql_select_query = "UPDATE emp_payroll set gross_salary =%s WHERE empid = %s"

            input1=(NewSal,detail)
            mycursor.execute(sql_select_query,input1)
            mycon.commit()

            sql_select_query = "UPDATE emp_payroll set overtime_pay =%s WHERE empid = %s"

            input2=(newop,detail)
            mycursor.execute(sql_select_query,input2)
            mycon.commit()

            sql_select_query = "UPDATE emp_payroll set income_tax =%s WHERE empid = %s"

            input3=(newtax,detail)
            mycursor.execute(sql_select_query,input3)
            mycon.commit()

            sql_select_query = "UPDATE emp_payroll set net_salary =%s WHERE empid = %s"

            input4=(newnetsal,detail)
            mycursor.execute(sql_select_query,input4)
            mycon.commit()

            sql_select_query = "UPDATE emp_payroll set increment =%s WHERE empid = %s"
            input5=(increment,detail)
            mycursor.execute(sql_select_query,input5)
            mycon.commit()


            print(mycursor.rowcount, "record(s) updated")

            mycursor.execute("SELECT * FROM emp_payroll")

            myresult = mycursor.fetchall()
    
       
            print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")

            print("| empid",space("empid"),"employeename", space("employeename"),"department",space("department"),"designation",space("designation"),"gross_salary",space("gross_salary"),"hours_worked",space("hours_worked"),"overtime_pay",end=" ")
            print(space("overtime_pay"),"income_tax",space("income_tax"),"net_salary",space('net_salary'),'increment',space('increment')," |")
    
            print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
   
            for x in myresult:
                print('|',x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3],space(x[3]),x[4],space(str(x[4])),x[5],space(str(x[5])),x[6],space(str(x[6])),x[7],space(str(x[7])),x[8],space(str(x[8])),x[9],space(str(x[9])),' |')
                print("|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")

        else:
            print('')
            print('WRONG ENTRY')

    elif (len(myresult)==0):
        print('')  
        print('NO EMPLOYEE WITH SUCH EMPLOYEE ID AS PER OFFICIAL DATA')


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#FOR TABLE 2:

def create_table_personal():
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aryan",
      database="emp_database"
    )

    mycursor = mycon.cursor()

    mycursor.execute("CREATE TABLE IF NOT EXISTS emp_personal(empid int(5) primary key auto_increment,employeename varchar(20),gender varchar(7),address varchar(25),mobile_number varchar(10),Qualification varchar(10))")

    print("Tables under emp_database: ")

    mycursor.execute("SHOW TABLES")

    for x in mycursor:
      print(x)
    

def add_new_record_personal_admin():
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aryan",
      database="emp_database"
    )
    mycursor = mycon.cursor()

    empid=input('ENTER EMPLOYEE ID:\t')

    sql_select_query = "select * from emp_payroll where empid = %s"
    
    mycursor.execute(sql_select_query, (empid, ))
    
    myresult = mycursor.fetchall()

    if len(myresult)!=0:
            
        for x in myresult:

            employeename=x[1]

            print('THE NAME OF EMPLOYEE AS PER OFFICAL DATA:\t',employeename)

            
        gender=input("ENTER GENDER:\t")

        address=input("ENTER ADDRESS:\t")

        mobile_number=int(input("ENTER MOBILE NUMBER:\t"))

        qualification=input("ENTER QUALIFICATION\t")
                  
        sql = "INSERT INTO emp_personal(empid,employeename,gender,address,mobile_number,qualification) VALUES({},'{}','{}','{}','{}','{}')".format(empid,employeename,gender,address,mobile_number,qualification)
    
        mycursor.execute(sql)

        mycon.commit()

        print(mycursor.rowcount, "record inserted.")


    elif len(myresult)==0:

        print('NO EMPLOYEE WITH SUCH EMPLOYEE ID AS PER OFFICAL DATA')


def add_new_record_personal():
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aryan",
      database="emp_database"
    )
    mycursor = mycon.cursor()

    empid=ID

    sql_select_query = "select * from emp_payroll where empid = %s"
    
    mycursor.execute(sql_select_query, (empid, ))
    
    myresult = mycursor.fetchall()

    if len(myresult)!=0:
            
        for x in myresult:

            employeename=x[1]

            print('THE NAME OF EMPLOYEE AS PER OFFICAL DATA:',employeename)

        gender=input("ENTER GENDER:\t")

        address=input("ENTER ADDRESS:\t")

        mobile_number=input("ENTER MOBILE NUMBER:\t")

        qualification=input("ENTER QUALIFICATION\t")
                  

        sql = "INSERT INTO emp_personal(empid,employeename,gender,address,mobile_number,qualification) VALUES({},'{}','{}','{}','{}','{}')".format(empid,employeename,gender,address,mobile_number,qualification)
    
        mycursor.execute(sql)

        mycon.commit()

        print(mycursor.rowcount, "record inserted.")

    elif len(myresult)==0:

        print('')
        print('NO EMPLOYEE WITH SUCH EMPLOYEE ID AS PER OFFICAL DATA')

    


def search_record_personal():
    
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aryan",
      database="emp_database"
    )


    mycursor = mycon.cursor()

    global ID

    sql_select_query = "select * from emp_personal where empid = %s"
    
    mycursor.execute(sql_select_query, (ID, ))
    
    myresult = mycursor.fetchall()

    if len(myresult)!=0:

        sql_select_query = "select * from emp_personal where empid = %s"

        mycursor.execute(sql_select_query, (ID, ))

        myresult = mycursor.fetchall()
        

        print("|--------------------------------------------------------------------------------------------------------|")

        print("| empid",space("empid"),"employeename", space("employeename"),"gender",space("gender"),"address",space("address"),"mobile_number",space("mobile_number"),"qualification",space("qualification")," |")

    
        print("|--------------------------------------------------------------------------------------------------------|")
   
        for x in myresult:
              
            print('|',x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3],space(x[3]),x[4],space(str(x[4])),x[5],space(str(x[5])),' |')
            print("|--------------------------------------------------------------------------------------------------------|")
    
    

    elif len(myresult)==0:

        print('') 
        print('NO EMPLOYEE WITH SUCH EMPLOYEE ID AS PER OFFICAL DATA')

    

def update_record_personal():
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aryan",
      database="emp_database"
    )
    
    mycursor = mycon.cursor()

    global ID

    sql_select_query = "select * from emp_personal where empid = %s"

    mycursor.execute(sql_select_query, (ID, ))

    myresult = mycursor.fetchall()

    if len(myresult)!=0:

        print('''
*****************************************************************************

*     TO UPDATE ADDRESS OF THE EMPLOYEE               1                     *

*     TO UPDATE MOBILE NUMBER OF THE EMPLOYEE         2                     *

*     TO UPDATE QUALIFICATIONS OF THE EMPLOYEE        3                     *

*****************************************************************************''')

        print('')
        sdetail_personal=input("ENTER YOUR CHOICE):\t")

        if (sdetail_personal=='1'):

            print('')
            
            NewAdd=input("Enter your new Address:\t")
            print('')

            sql_select_query = "UPDATE emp_personal set address =%s WHERE empid = %s"
    
            input5=(NewAdd,ID)
                
            mycursor.execute(sql_select_query,input5)

            mycon.commit()

            print(mycursor.rowcount, "record(s) updated")

            sql_select_query="SELECT * FROM emp_personal where empid= %s"

            mycursor.execute(sql_select_query, (ID, ))
            
            myresult = mycursor.fetchall()

            print("|--------------------------------------------------------------------------------------------------------|")
            print("| empid",space("empid"),"employeename", space("employeename"),"gender",space("gender"),"address",space("address"),"mobile_number",space("mobile_number"),"qualification",space("qualification")," |")
    
            print("|--------------------------------------------------------------------------------------------------------|")
   
            for x in myresult:
              
                print('|',x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3],space(x[3]),x[4],space(str(x[4])),x[5],space(str(x[5])),' |')
                print("|--------------------------------------------------------------------------------------------------------|")

        elif (sdetail_personal=='2'):

            print('')
            
            NewNumber=input("Enter your new Mobile Number:\t")
            print('')
            sql_select_query = "UPDATE emp_personal set mobile_number =%s WHERE empid = %s"
    
            input6=(NewNumber,ID)
                
            mycursor.execute(sql_select_query,input6)

            mycon.commit()

            print(mycursor.rowcount, "record(s) updated")

            sql_select_query="SELECT * FROM emp_personal where empid= %s"

            mycursor.execute(sql_select_query, (ID, ))

            myresult = mycursor.fetchall()

            print("|--------------------------------------------------------------------------------------------------------|")
            print("| empid",space("empid"),"employeename", space("employeename"),"gender",space("gender"),"address",space("address"),"mobile_number",space("mobile_number"),"qualification",space("qualification")," |")
    
            print("|--------------------------------------------------------------------------------------------------------|")
   
            for x in myresult:
              
                print('|',x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3],space(x[3]),x[4],space(str(x[4])),x[5],space(str(x[5])),' |')
                print("|--------------------------------------------------------------------------------------------------------|")

        elif (sdetail_personal=='3'):
                
            print('')
            
            NewQual=input("Enter your new Qualification:\t")

            print('')

            sql_select_query = "UPDATE emp_personal set qualification =%s WHERE empid = %s"
                
            input7=(NewQual,ID)
                
            mycursor.execute(sql_select_query,input7)

            mycon.commit()

            print(mycursor.rowcount, "record(s) updated")

            sql_select_query="SELECT * FROM emp_personal where empid= %s"

            mycursor.execute(sql_select_query, (ID, ))
                
            myresult = mycursor.fetchall()
                
            print("|--------------------------------------------------------------------------------------------------------|")
            print("| empid",space("empid"),"employeename", space("employeename"),"gender",space("gender"),"address",space("address"),"mobile_number",space("mobile_number"),"qualification",space("qualification")," |")

            print("|--------------------------------------------------------------------------------------------------------|")
   
            for x in myresult:
              
                print('|',x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3],space(x[3]),x[4],space(str(x[4])),x[5],space(str(x[5])),' |')
                print("|--------------------------------------------------------------------------------------------------------|")
        else:
            print('')
            print('WRONG ENTRY PLS CHECK AGAIN')
    else:
        print('')
        print("NO EMPLOYEE WITH SUCH EMPLOYEE ID AS PER OFFICAL DATA")


def display_record_personal():
    
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aryan",
      database="emp_database"
    )


    mycursor = mycon.cursor()

    mycursor.execute("SELECT * FROM emp_personal")

    myresult = mycursor.fetchall()
    print("|--------------------------------------------------------------------------------------------------------|")
    print("| empid",space("empid"),"employeename", space("employeename"),"gender",space("gender"),"address",space("address"),"mobile_number",space("mobile_number"),"qualification",space("qualification")," |")

    print("|--------------------------------------------------------------------------------------------------------|")
   
    for x in myresult:
              
        print('|',x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3],space(x[3]),x[4],space(str(x[4])),x[5],space(str(x[5])),' |')
        print("|--------------------------------------------------------------------------------------------------------|")



def delete_record_personal():

    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aryan",
      database="emp_database"
    )


    mycursor = mycon.cursor()

    global ID
 
    sql_select_query = "DELETE FROM emp_personal WHERE empid = %s"

    mycursor.execute(sql_select_query, (ID, ))

    mycon.commit()

    print('')
    print(mycursor.rowcount, "record(s) deleted")
    

def payroll_slip_data_from_personal_table():
     mycon = mysql.connector.connect(
       host="localhost",
       user="root",
       passwd="aryan",
       database="emp_database"
     )

     mycursor = mycon.cursor()

     global ID

     sql_select_query = "select * from emp_personal where empid = %s"
    
     mycursor.execute(sql_select_query, (ID, ))
    
     myresult = mycursor.fetchall()

     if len(myresult)!=0:

        sql_select_query = "select * from emp_personal where empid = %s"

        mycursor.execute(sql_select_query, (ID, ))

        myresult = mycursor.fetchall()

        for x in myresult:
            print('\t\t---------------------------------------')
            print('\t\tEMPLOYEE PAY SLIP')
            print('\t\t---------------------------------------')
            print('\t\tID             : ',str(x[0]) )
            print('')
            print('\t\tNAME           : ',x[1] )
            print('')
            print('\t\tGENDER         : ',x[2] )
            print('')
            print('\t\tADDRESS        : ',x[3] )
            print('')
            print('\t\tMOBILE NUMBER  : ',str(x[4]) )
            print('')
            print('\t\tQUALIFICATION  : ',x[5] )
        

     elif len(myresult)==0:
            print('')
            print('PERSONAL/PROFESSIONAL DETAILS OF THIS EMPLOYEE N0T FOUND')

def payroll_slip():
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aryan",
      database="emp_database"
    )

    mycursor = mycon.cursor()

    global ID

    sql_select_query = "select * from emp_personal where empid = %s"
    
    mycursor.execute(sql_select_query, (ID, ))
    
    myresult = mycursor.fetchall()

    if len(myresult)!=0:
        sql_select_query = "select * from emp_payroll where empid = %s"

        mycursor.execute(sql_select_query,(ID, ))

        myresult = mycursor.fetchall()

        emp_underpeforming_quotes = ['Life’s like a movie, write your own ending. Keep believing, keep pretending. —Jim Hensen', 'So many things are possible just as long as you don’t know they’re impossible. —Norton Juster',
                                     'The moment you doubt whether you can fly, you cease forever to be able to do it.', 'Opportunity is missed by most people because it is dressed in overalls and looks like work. —Thomas Edison']

        emp_good_performance_quotes = ['Your dedication is imperative for the growth of our company. Thank you for your efforts.',
                                       'It’s the vision of employees like you who turn desired plans into success. We value you and your work to the moon and back.',
                                       'An employee’s hard work is the fuel to great company culture. Thanks for adding extra miles to ours.',
                                       'The service you provided exceeded all expectations. I would also like to add how much you mean to our company. Thank you, and keep up with the good work.']

    
        for x in myresult:
            print('')
            print('\t\tDEPARTMENT     : ',x[2] )
            print('')
            print('\t\tDESIGNATION    : ',x[3] )
            print('')
            print('\t\tGROSS SALARY   : ',x[4] )
            print('')
            print('\t\tHOURS WORKED   : ',x[5],"Hours" )
            print('')
            print('\t\tOVERTIME PAY   : ',x[6] )
            print('')
            print('\t\tINCOME TAX     : ',x[7] )
            print('')
            print('\t\tNET SALARY     : ',x[8] )
            print('')
            print('\t\tINCREMENT      : ',x[9] )
            print('\n\n\n')

            print('MOTIVATIONAL LINES FOR YOU:\n')
            
            if (x[5]>=170):
                print('\t',random.choice(emp_good_performance_quotes))
                print('\n')
            else:
                print('\t',random.choice(emp_underpeforming_quotes))
                print('\n')
                
    elif len(myresult)==0:
            print('')
            print('PERSONAL/PROFESSIONAL DETAILS OF THIS EMPLOYEE N0T FOUND')


def emp_recomendation():
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="aryan",
      database="emp_database"
    )

    mycursor = mycon.cursor()

    global ID

    sql_select_query = "select * from emp_payroll where empid = %s"
    
    mycursor.execute(sql_select_query, (ID, ))
    
    myresult = mycursor.fetchall()

    if len(myresult)!=0:

        for x in myresult:
            hour=x[5]
        diff=int(hour-40)

        if (diff>=20):
            print('')
            print('***********************************EMPLOYEE GRADE-A1*********************************************')
            print('')
            print('YOUR PERFORMANCE HAS BEEN REALLY AMAZING. YOU ARE ONE OF THE STAR EMPLOYEE OF THE COMPANY. KEEP UP THE GOOD WORK.')
            print('')

        elif (diff<=20 and diff>=0):
            print('')
            print('***********************************EMPLOYEE GRADE-A2*********************************************')
            print('')
            print('YOUR WORK IS HIGHLY APPRECIATED. YOU ARE IN THE GOOD BOOKS OF YOUR BOSSES. KEEP UP THE GOOD WORK.')
            print('')

        elif (diff<=0 and diff>=-10):
            print('')
            print('***********************************EMPLOYEE GRADE-B1*********************************************')
            print('')
            print('YOUR PERFORMANCE HAS BEEN GOOD. CONTINUE TO YOUR HARDWORK AND AIM FOR HIGHER GOALS.')
            print('')
            
        elif (diff<=-20):
            print('')
            print('***********************************EMPLOYEE GRADE-C1*********************************************')
            print('')
            print('YOUR PERFORMANCE HAS BEEN EXTREMELY AVERAGE. YOU SHOULD INCREASE YOUR EFFORT AND FOCUS MORE ON YOUR WORK.')
            print('')

    elif len(myresult)==0:
            print('')
            print('PERSONAL/PROFESSIONAL DETAILS OF THIS EMPLOYEE N0T FOUND')

            
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#_main_
      
x=check_connection()
if x==1:
    create_database()
    create_table()
    create_table_personal()
else:
    print("Kindly check connection")
    print('')


print("                                                             ---------------------------------------------------------------")
print("                                                            |===============================================================|")
print("                                                            |======== Welcome To Employee Payroll Management System ========|")
print("                                                            |===============================================================|")
print("                                                             ---------------------------------------------------------------")

print('')
print('')
print('')

print('''
*****************************************************

*   WANT TO WORK AS ADMIN, THEN ENTER     1         * 

****************************************************

*   WANT TO WORK AS EMPLOYEE, THEN ENTER  2         *

*****************************************************''')

print('')

user=input('''ENTER YOUR CHOICE:\t''')

if (user=="1"):
    c=0
    while(c<=2):

        print('')
        password=input("ENTER PASSWORD:\t")
    
        
        if(password=='admin'):
               
            ans='y'
            while ans=='y' or ans=='Y':
                print('')
                print('')
                print("************************************************************************")
                print("*\t\tEMPLOYEE PAYROLL MANAGEMENT SYSTEM                    *")
                print("************************************************************************")
                print('')
                print("*\t\t1>  Add Offical Details          ||        1           *")
                print('')
                print("************************************************************************")
                print('')
                print("*\t\t2>  View Offical Details         ||        2           *")
                print('')
                print("************************************************************************")
                print('')
                print("*\t\t3>  Search Official Details      ||        3           *")
                print('')
                print("************************************************************************")
                print('')
                print("*\t\t4>  Delete Offical Details       ||        4           *")
                print('')
                print("************************************************************************")
                print('')
                print("*\t\t5>  Update Offical Details       ||        5           *")
                print('')
                print("************************************************************************")
                print('')
                print("*\t\t6>  Add Personal Details        ||         6           *")
                print('')
                print("************************************************************************")
                print('')
                print("*\t\t7>  View Personal Details        ||        7           *")
                print('')
                print("************************************************************************\n\n")
 
                ch=int(input("enter your choice\t"))
                print('')
                if ch==1:
                    add_new_record()       
                elif ch==2:
                    display_all_record()
                elif ch==3:
                    search_record()
                elif ch==4:
                    delete_record()
                elif ch==5:
                    update_record()
                elif ch==6:
                    add_new_record_personal_admin()
                elif ch==7:
                    display_record_personal()
                else:
                    print("Wrong Choice, Please enter values between 1-7")

                print('')
                ans=input("Wish to continue\t")
                if (ans!='y' or ans!='Y'):
                    c=4
            print("\t\t\t\t\t\t\t\tTHANK YOU FOR USING EMPLOYEE DATABASE MANAGEMENT SYSTEM")

        elif(password=='ADMIN'):
            print('\nWRONG PASSWORD ENTERED!!!')
            print('\nCAUTION:CAPS LOCK IS ON')
            c=c+1
        
        elif(password!='admin' and password!='ADMIN'):
            print('\nWRONG PASSWORD ENTERED!!!')
            c=c+1
             
    if (c==3):
        print('INCORRECT PASSWORD LIMIT REACHED')
        print('ACCESS DENIED!!!')
        
elif (user=="2"):
    
    a='y'
        
    while(a=='y' or a=='Y'):

        print('')
    
        ID=int(input('Enter Employee ID:\t'))
        
        print('')

        print('')
        print("************************************************************************")
        print("*\t\tEMPLOYEE PERSONAL DETAILS MANAGEMENT SYSTEM            *")
        print("************************************************************************")
        print('')
        print("*\t\t1>  Add Personal Details         ||        1           *")
        print('')
        print("************************************************************************")
        print('')
        print("*\t\t2>  Search Personal Details      ||        2           *")
        print('')
        print("************************************************************************")
        print('')
        print("*\t\t3>  Delete Personal Details      ||        3           *")
        print('')
        print("************************************************************************")
        print('')
        print("*\t\t4>  Update Personal Details      ||        4           *")
        print('')
        print("************************************************************************")
        print('')
        print("*\t\t5>  Print Payslip                ||        5           *")
        print('')
        print("************************************************************************")
        print('')
        print("*\t\t6>  Remarks From Admin           ||        6           *")
        print('')
        print("************************************************************************\n\n")

        a=int(input('Enter your Choice:\t'))

        if (a==1):
            add_new_record_personal()

        elif (a==2):
            search_record_personal()

        elif (a==3):
            delete_record_personal()

        elif (a==4):
            update_record_personal()

        elif (a==5):
            payroll_slip_data_from_personal_table(), payroll_slip()

        elif(a==6):
            emp_recomendation()

        else:
            print('WRONG ENTRY')
            
        print('')
        a=input('Wish to continue:\t')
    print('\t\t\t\t\t\t\t\tTHANK YOU FOR USING EMPLOYEE DATABASE MANAGEMENT SYSTEM')
else:
    print('WRONG OPTION ENTERED')



    
       

                   
                   
                   
                   
    




