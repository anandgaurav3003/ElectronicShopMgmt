import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='gaurav',database='electronic_shop')
if conn.is_connected:
 cur=conn.cursor()
#cur.execute('create table items(s_no int(10),item varchar(50) primary key,availability_of_item int(10),price int(7))')
 conn.commit()            
#FOR CREATING OTHER TWO TABLES:
import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='gaurav',database='electronic_shop')
cur=conn.cursor()
#cur.execute('create table labours(name varchar(25) primary key,age int(10),place varchar(25),department varchar(25))')
#cur.execute('create table customer(customer_name varchar(50) primary key,age int(10),place varchar(25),item_bought varchar(25)')
conn.commit()
#MAIN SOURCE CODE :
import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='gaurav',database='electronic_shop')
cur=conn.cursor()
def entry_item():
                    s_no=int(input('enter the s_no of item:'))
                    item=input('enter the name of item:')
                    availability_of_item=int(input('availability of the item:'))
                    price=int(input('enter the price of item in rupees:'))
                    #cur.execute("insert into items (s_no,item,avilability_of_item,price)values(%s,%s,%s,%s)")
                    cur.execute("insert into items values ('"+str(s_no)+"' , '"+item+"' , '"+str(availability_of_item)+"' , '"+str(price)+"')")
                    print('entry succesful')
                    conn.commit()
def entry_labour():
                    name=input('enter the name of labour:')
                    age=int(input('enter the age:'))
                    place=input('enter the place of the labour:')
                    dept=input('enter the name of the department:')
                    cur.execute("insert into labours values('" + name + "','" + str(age) + "','" + place + "','" + dept + "')")
                    print('entry sucessful')
                    conn.commit()
def entry_customer():
                    name=input('enter the name of the customer:')
                    age=int(input('enter the age:'))
                    place=input('enter the place of the customer:')
                    item=input('enter the item bought:')
                    cur.execute("insert into customer values('" + name + "','" + str(age) + "','" + place + "','" + item + "')")
                    print('entry sucessful')
                    conn.commit()
def mainmenu():
                    print('1.entry for item')
                    print('2.entry for labour')
                    print('3.entry for customer')
            
                    choose=int(input('enter the choice for entry:'))
                    if choose==1:
                      entry_item()

                    elif choose==2:
                      entry_labour()

                    elif choose==3:
                      entry_customer()
                
def mainmenu2():
                print('1.Display of item list')
                print('2.Display of labour list')
                print('3.Display of customer list')
                ch=int(input('enter the choice:'))
                if ch==1:
                       print()
                       cur.execute("select * from items")
                       dataa=cur.fetchall()
                       print('list of items')
                       for row in dataa:
                           print()
                           print('s_no:',row[0])
                           print('item:',row[1])
                           print('availablity:',row[2])
                           print('price:',row[3])
                elif ch==2:
                    print()
                    cur.execute("select * from labours")
                    data=cur.fetchall()
                    print('list of labours')
                    for row in data:
                        print()
                        print('name:',row[0])
                        print('age:',row[1])
                        print('place:',row[2])
                        print('department:',row[3])
                elif ch==3:
                    print()
                    cur.execute("select * from customer")
                    datas=cur.fetchall()
                    print('list of customer')
                    for row in datas:
                        print()
                        print('name:',row[0])
                        print('age:',row[1])
                        print('place:',row[2])
                        print('item bought:',row[3])
def main2():
 while True:    
    print('======================================================================')
    print('**********************ELECTRONIC SHOP SYSTEM**************************')
    print('======================================================================')
    print('              1.admin')
    print('              2.customers')    
    choice=int(input('enter the choice:'))
    if choice==1:
                pw='gaurav'
                alp=input('enter password:')
                if alp==pw:
                     mainmenu()
                else :
                    print('wrong password! Please enter correct password')
                    
    elif choice==2:
                mainmenu2()
    else :
                print("wrong choice!  Choose correct option .")
                main2()

main2()
            


                        

