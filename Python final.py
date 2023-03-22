import mysql.connector as connector
con=connector.connect(host='localhost', port=3306, user='root',password='tiger123', database='automobile_service_station')

def connect():
    query1='create table if not exists customer_details(Serial_no int primary key,C_name varchar(25), C_address varchar(30), C_pincode int)'

    query2='create table if not exists fuel(Serial_no int primary key,Fuel_refilled varchar(15), Amount float)'

    query3='create table if not exists repair(Serial_no int primary key, Amount float, Discount float, GrandTotal float, Description varchar(100))'
    cur=con.cursor()
    cur.execute(query1)
    cur.execute(query2)
    cur.execute(query3)
    print("Succefully Connected to D/atabase")

#Main Menu
def menu():
    print('\t\t\t\t**********************************')
    print('\t\t\t\t*** AUTOMOBILE SERVICE STATION ***')
    print('\t\t\t\t***                            ***')
    print('\t\t\t\t***         MAIN MENU          ***')
    print('\t\t\t\t**********************************\n')
    print('1. Customer info')
    print('2. Fuel')
    print('3. Repair')
    print('4. Total Charges')
    print()
    print('*  Exit\n')

# Customers Menu
def customer_menu():
    print("==========================")
    print('Customer Details Menu')
    print()
    print('1. Display all customers')
    print('2. Add new customer')
    print('3. Delete a customer')
    print('4. Search for a customer')
    print('5. Update Customer Info')
    print()
    print('9.  Back to main menu')
    print()

# Display Customers
def display_customers():
    query="select * from customer_details"
    cur=con.cursor()
    cur.execute(query)
    acc =  cur.fetchall()
    
    if acc:
        for row in acc:
            print("Serial_no: ",row[0])
            print("Customer_name: ",row[1])
            print("Customer_address: ",row[2])
            print("Customer_pincode: ",row[3])
            print()
            print()
    else:
        print("There is no Customer")
    
# New Customer
def new_Customer():
    serial_no=int(input("Enter Serial Number: "))
    c_name=input("Enter Customer Name: ")
    c_address=input("Enter Address: ")
    c_pincode=int(input("Enter PinCode: "))
    query="insert into customer_details(Serial_no,C_name,C_address,C_pincode) values('{}','{}','{}','{}')".format(serial_no,c_name,c_address,c_pincode)
    cur=con.cursor()
    cur.execute(query)
    con.commit()
    print("Customer Saved to DataBase")

# Remove Customer
def remove_Customer():
    serial_no=int(input("Enter Serial Number: "))
    query="delete from customer_details where Serial_no={}".format(serial_no)
    cur=con.cursor()
    cur.execute(query)
    con.commit()
    print("Customer Removed Successfully")
    print()

# Search Customer
def search_customer():
    print("Search Customer's Details Using:-")
    print("1. Serial number")
    print("2. Customer's Name")
    choice=int(input("Enter your choice: "))
    if choice==1:
        serial_no=int(input("Enter Serial Number: "))
        query="select * from customer_details where Serial_no='{}'".format(serial_no)
        cur=con.cursor()
        cur.execute(query)
        acc = cur.fetchall()  
        if acc:
            for row in acc:
                print("Serial_no: ",row[0])
                print("Customer_name: ",row[1])
                print("Customer_address: ",row[2])
                print("Customer_pincode: ",row[3])
                print()
        else:
            print("Customer with this serial number does not exists")
    elif choice==2:
        c_name=input("Enter Customer's Name: ")
        query="select * from customer_details where C_name='{}'".format(c_name)
        cur=con.cursor()
        cur.execute(query)
        acc = cur.fetchall()
        if acc:
            for row in acc:
                print("Serial_no: ",row[0])
                print("Customer_name: ",row[1])
                print("Customer_address: ",row[2])
                print("Customer_pincode: ",row[3])
                print()
        else:
            print("Customer with this name doesnot exists")
    else:
        print("Invalid Choice!")

# Update
def Update_customer():
    serial_no=input("Enter Serial Number: ")
    print("What do you want to update:-")
    print("1.Serial Number")
    print("2. Name ")
    print("3. Address ")
    print("4. PinCode")
    choice=int(input("Enter your choice: "))

    if choice==1:
        s_no=int(input("Enter Customer's Updated Serial Number: "))
        query="update customer_details set Serial_no='{}' where Serial_no={}".format(s_no,serial_no)
        cur=con.cursor()
        cur.execute(query)
        con.commit()
        print("Records Updated Successfully")

    elif choice==2:
        c_name=str(input("Enter Customer's Updated Name: "))
        query="update customer_details set C_name='{}' where Serial_no={}".format(c_name,serial_no)
        cur=con.cursor()
        cur.execute(query)
        con.commit()
        print("Records Updated Successfully")

    elif choice==3:
        c_address=int(input("Enter Customer's Updated Address: "))
        query="update customer_details set C_address='{}' where Serial_no={}".format(c_address,serial_no)
        cur=con.cursor()
        cur.execute(query)
        con.commit()
        print("Updated")
    
    elif choice==4:
        c_pincode=int(input("Enter Customer's Updated PinCode: "))
        query="update customer_details set C_pincode='{}' where Serial_no={}".format(c_pincode,serial_no)
        cur=con.cursor()
        cur.execute(query)
        con.commit()
        print("Records Updated Successfully")
    
    else:
        print("Invalid Choice!")
    
# Fuel Menu
def fuel_menu():
    print('=======================\nFuel Menu')
    print('')
    print('1. Refill Gasoline')
    print('2. Refill Diesel')
    print('3. Display Records')
    print('4. Delete Record')
    print('9. Back to main menu')
    print()

# Refill
def refill_fuel(fuel):
    serial_no=int(input("Enter Serial Number: "))
    ltr=int(input("Enter Quantity In Liters: "))
    
    amt=0
    if fuel=='Gasoline':
        amt=amt+(ltr*95.41)
    elif fuel=='Diesel':
        amt=amt+(ltr*86.67) 
    query="insert into fuel(Serial_no,Fuel_refilled,Amount) values({},'{}',{})".format(serial_no,fuel,amt)
    
    cur=con.cursor()
    cur.execute(query)
    con.commit()
    print('Fuel filled successfully')

# Display_Fuel
def display_fuel():
    serial_no=int(input("Enter Serial Number: "))
    query="select * from fuel where Serial_no={}".format(serial_no)
    cur=con.cursor()
    cur.execute(query)
    print("Fuel filled successfully")
    
    acc =  cur.fetchall()    
    if acc:
        for row in acc:
            print("Serial_no: ",row[0])
            print("Fuel refilled: ",row[1])
            print("Amount: ₹",row[2])
            print()
            print()
    else:
        print("No Records Found")

# Delete Fuel
def delete_fuel():
    serial_no=int(input("Enter Serial Number: "))
    query="delete from fuel where Serial_no={}".format(serial_no)
    cur=con.cursor()
    cur.execute(query)
    con.commit()
    print("Records Deleted Successfully")
    print()

# Repair Menu
def repair_menu():
    print('=========================\nRepair Menu')
    print()
    print('1. Display All Records')
    print('2. Search For A Record')
    print('3. Add Record')
    print('4. Delete Record')
    print('9. Back To Main Menu')
    print()

# Display Repair
def display_repair():
    query="select * from repair"
    cur=con.cursor()
    cur.execute(query)
    acc =  cur.fetchall()
    
    if acc:
        for row in acc:
            print("Serial_no: ",row[0])
            print("Amount: ",row[1])
            print("Discount: ",row[2],"%")
            print("GrandTotal: ",row[3])
            print("Description: ",row[4])
            print()
            print()
    else:
        print("No Records Found")

# Add Record
def add_repair():
    serial_no=int(input("Enter Serial Number: "))
    amount=float(input("Enter Amount: "))
    discount=float(input("Enter Discount: "))
    grandtotal=amount*(1-discount/100)
    description=str(input("Enter Description: "))
    query="insert into repair(Serial_no,Amount,Discount,GrandTotal,Description) values({},'{}','{}','{}','{}')".format(serial_no,amount,discount,grandtotal,description)
    
    cur=con.cursor()
    cur.execute(query)
    con.commit()
    print("Records Added Successfully")

# Search Repair
def search_repair_record():
    serial_no=int(input("Enter Serial Number: "))
    query="select * from repair where serial_no={}".format(serial_no)
    cur=con.cursor()
    cur.execute(query)
    for row in cur:
        print("Serial_no: ",row[0])
        print("Amount: ",row[1])
        print("Discount: ",row[2])
        print("GrandTotal: ",row[3])
        print("Description: ",row[4])
        print()
        print()

# Delete Repair
def del_repair_record():
    serial_no=int(input("Enter Serial Number: "))
    query="delete from repair where Serial_no={}".format(serial_no)
    cur=con.cursor()
    cur.execute(query)
    con.commit()
    print("Records Deleted Successfully")
    print()

# Total charges
def Total_charges(serial_no):
    query="select * from repair where Serial_no={}".format(serial_no)
    cur=con.cursor()
    cur.execute(query)
    amt=0
    repair_charge=0
    discount=0
    grandtotal=0
    for row in cur:
        amt+=row[3]
        grandtotal+=row[3]
        repair_charge+=row[1]
        discount+=row[2]

    query="select * from fuel where Serial_no={}".format(serial_no)
    cur=con.cursor()
    cur.execute(query)
    fuel=0
    for row in cur:
        amt+=row[2]
        fuel+=row[2]

    return amt,repair_charge,discount,grandtotal,fuel
    

while True:
    connect()
    menu()
    choice=input(("Enter  your Choice :- "))
    
    if choice=='1':
        while True:
            customer_menu()
            
            choice1=input('Enter the choice:- ')
            
            if choice1=='1':
                display_customers()
            
            elif choice1=='2':
                new_Customer()
            
            elif choice1=='3':
                remove_Customer()
            
            elif choice1=='4':
                search_customer()
            
            elif choice1=='5':
                Update_customer()
            
            elif choice1=='9':
                break
            
            else:
                print('Enter a valid choice')
    
    elif choice=='2':
        while True:
                
                fuel_menu()
                
                choice1=input("Enter your choice: ")
                
                if choice1=='1':
                    refill_fuel('Gasoline')

                elif choice1=='2':
                    refill_fuel('Diesel')

                elif choice1=='3':
                    display_fuel()

                elif choice1=='4':
                    delete_fuel()

                elif choice1=='9':
                    break

                else:
                    print('Invalid Choice')
                
    elif choice=='3':
        while True:
            repair_menu()
            choice1=input('Enter Choice:- ')
            
            if choice1=='1':
                display_repair()
            
            elif choice1=='2':
                search_repair_record()
            
            elif choice1=='3':
                add_repair()
            
            elif choice1=='4':
                del_repair_record()
            
            elif choice1=='9':
                break
            
            else:
                print('Invalid Choice!') 
    
    elif choice=='4':
        serial_no=int(input("Enter Serial Number: "))
        amt,repair_charge,discount,grandtotal,fuel=Total_charges(serial_no)

        discnt_val=(discount/100)*repair_charge

        print("\n\nFuel Charge: {}".format(fuel))
        print("Repair Charge: {}".format(repair_charge))
        print("Discount In Repair: {}%".format(discount))
        print("Money Discounted In Repair: ₹{}".format(discnt_val))
        print("Repair Charge After Discount: ₹{}".format(grandtotal))
        print("Total Charge For Fuel And Repair: ₹{}".format(amt))
        print()
        print()
        
    elif choice=='0':
        break
    else:
        print('Invalid Choice! Please Enter a Valid Choice!')
