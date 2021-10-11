Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import mysql.connector
from datetime import date
import time

def clear():
  for _ in range(65):
     print()

def introduction():
    msg = '''
          A L U M N I    I N F O R M A T I O N    S Y S T E M 
          
          - An Introduction
          
          Alumni are the most important part of any education system. Alumni database help us to recognize the best brains educated by the institute and every big education system keep a record of them. 

          This project is also trying to solve this simple but very useful information of their alumni. The whole Database is store in MySQL table alumni that stores their current position as well as some other useful Information like higher education, current position, pass out year etc.

          The whole project is divided into four major parts ie addition of data, modification, searching and reporting. All these part are further divided into menus for easy navigation'''

    for x in msg:
        print(x, end='')
        time.sleep(0.002)
    wait = input('Press any key to continue.....')


def made_by():
    msg = ''' 
        Alumni information system made by                                : Nidhi Verma
            Roll No                                                                  : 
            School Name                                   : Greenway Modern Sr Sec School
            Academic Session                                     : 2020-21
            
            \n\n\n
        '''

    for x in msg:
        print(x, end='')
        time.sleep(0.002)

  wait = input('Press any key to continue.....')

def create_database():
     mydb=mysql.connector.connect(host="localhost",user="root",passwd="root123")
     mycursor=mydb.cursor()
     mycursor.execute("create database if not exists alumni")
     mycursor.execute("use alumni")
     print("Creating Alumni table")
     s1 = "CREATE TABLE if not exists Alumni(id int(4) PRIMARY KEY NOT NULL AUTO_INCREMENT,name char(30),fname char(30),phone char(30),email char(30), Stream char(30), pass_year char(4),hqualification char(40), current_position char(30),dob date, c_city char(20), c_country char(30),employement char(30));"
     mycursor.execute(s1)
     
def db_mgmt( ):
    while True:
        print("\t\t\t 1. Database and Tables creation")
        print("\t\t\t 2. Back (Main Menu)")
        c = int(input("\t\t Enter Your Choice :"))
        if c == 1:
            create_database()
        if c == 2:
            break

def record_exists(name,fname,dob):
    conn = mysql.connector.connect(
    host='localhost', database='alumni', user='root', password='root123')
    cursor = conn.cursor()
    sql ='select * from alumni where name ="'+name +'" and fname ="'+fname+'"  and dob ="'+dob+'";'
    cursor.execute(sql)
    record = cursor.fetchone()
    return record

def add_alumni():
  conn = mysql.connector.connect(
      host='localhost', database='alumni', user='root', password='root123')
  cursor = conn.cursor()
  clear()
  name = input('Enter Alumni Name  : ').upper()
  fname = input('Enter Alumni Father Name  : ').upper()
  dob = input('Enter Alumni Date Of birth(yyyy/mm/dd) : ')
  phone = input('Enter Alumni Phone No  : ')
  email = input('Enter Alumni Email ID  : ')
  stream = input('Enter Alumni Stream(passed)  : ').upper()
  pass_year = input('Enter Alumni Pass Year : ')
  quali = input('Enter Alumni Highest Qualification : ').upper()
  position = input('Enter Alumni Current Position : ')
  city= input('Enter Alumni Current City : ').upper()
  country= input('Enter Alumni Current Country : ').upper()
  employ= input('Enter Alumni Currently employeed/Business : ')

  sql ='insert into alumni(name,fname,phone,email,stream,pass_year,hqualification,\
          current_position,dob,c_city,c_country,employement) values(\
          "'+name+'","'+fname+'","'+phone+'","'+email+'","'+stream+'","'+pass_year+'","'+quali+'","'+position+'","'\
          +dob+'","'+city+ '","'+country+'","'+employ+'");'
  result = record_exists(name,fname,dob)
  if result is None:
    cursor.execute(sql)
    conn.commit()
    print('\n\n\n Alumni information added successfully.....')
  else:
    print('\n\n\n Record already exist.....................')
  conn.close()
  wait = input('\n\n\n Press any key to continue....')

def modify_alumni():
    conn = mysql.connector.connect(
        host='localhost', database='alumni', user='root', password='root123')
    cursor = conn.cursor()
    while True:
        clear()
        print('ALUMNI INFORMATION MODIFICATION MENU')
        print('*'*100)
        print('1.   Correction In Name')
        print('2.   Correction In Father Name')
        print('3.   Correction In Phone No')
        print('4.   Correction In Email ID')
        print('5.   Correction In Stream')
        print('6.   Correction In Pass Year')
        print('7.   Correction In Highest Qualification')
        print('8.   Correction In Current Position')
        print('9.   Correction In Current City')
        print('10.  Correction In Current Country')
        print('11.   Back to main Menu')
        choice = int(input('\n\nEnter your choice : '))
        field_name =''
        if choice ==1:
            field_name='name'
        if choice == 2:
            field_name = 'fname'
        if choice == 3:
            field_name = 'phone'
        if choice == 4:
            field_name = 'email'
        if choice == 5:
            field_name = 'stream'
        if choice ==6:
            field_name='pass_year'
        if choice ==7:
            field_name='hqualification'
        if choice ==8:
            field_name='current_position'
        if choice == 9:
            field_name = 'c_city'
        if choice == 10:
            field_name = 'c_country'
        if choice == 11:
          conn.close()
          break
        clear()
        print('Change Value for ',field_name)
   print('*'*100)
        idr= input('Enter alumni ID :')
        value = input('Enter new Value :')
        sql = 'update alumni set '+field_name +'="'+ value +'" where id = '+idr+';' 
        cursor.execute(sql)
        conn.commit()
        wait = input('\n\n\n Record updated.........Press any key to continue....')
    
    conn.close()
       
def search_menu():
    conn = mysql.connector.connect(
       host='localhost', database='alumni', user='root', password='root123')
    cursor = conn.cursor()
    while True:
      clear()
      print(' S E A R C H    M E N U')
      print('*'*100)
      print("\n1.   ID")
      print('\n2.   Name')
      print('\n3.   Father Name')
      print('\n4.   Phone No')
      print('\n5.   Email')
      print('\n6.   stream')
      print('\n7.   pass year')
      print('\n8.   Qualification')
      print('\n9.   Position')
      print('\n10.  City')
      print('\n11.  Country')
      print('\n12.  Employment')
      print('\n13.  Back to Main Menu')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      field_name=''
   
      if choice == 1:
        field_name ='id'
      if choice == 2:
        field_name ='name'
      if choice == 3:
        field_name = 'fname'
      if choice == 4:
        field_name = 'phone'
      if choice == 5:
        field_name = 'email'
      if choice == 6:
        field_name = 'stream'
      if choice == 7:
        field_name = 'pass_year'
      if choice == 8:
        field_name = 'hqualification'
      if choice == 9:
        field_name = 'current_position'
      if choice == 10:
        field_name = 'c_city'
      if choice == 11:
        field_name = 'c_country'
      if choice == 12:
        field_name = 'employement'
      if choice == 13:
        break
      msg ='Enter '+field_name+': '
      value = input(msg)
      if field_name=='id':
        sql = 'select * from alumni where '+field_name + ' = '+value+';'
      else:
        sql = 'select * from alumni where '+field_name +' like "%'+value+'%";'
      #print(sql)
      cursor.execute(sql)
      records = cursor.fetchall()
      n = len(records)
      clear()
      print('Search Result for ', field_name, ' ',value)
      print('-'*120)
      for record in records:
       print(record[0], record[1], record[2], record[3],
             record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11], record[12])
      if(n <= 0):
        print(field_name, ' ', value, ' does not exist')
      wait = input('\n\n\n Press any key to continue....')

    conn.close()
    wait=input('\n\n\n Press any key to continue....')

def report_alumni_list():
    conn = mysql.connector.connect(
        host='localhost', database='alumni', user='root', password='root123')
    cursor = conn.cursor()
    sql ="select * from alumni"
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Alumni List')
    print('_'*140)
    print('{:10s} {:30s} {:30s} {:15s} {:30s} {:20s}'.format(
        'ID', 'Name', 'Father Name','Email','Phone','Position'))
    print('_'*140)
    for record in records:
      print('{:010d} {:30s} {:30s} {:15s} {:30s} {:20s}'.format(
          record[0], record[1], record[2], record[4],record[3],record[8]))

    print('_'*140)

    conn.close()
    wait=input('\n\n\n Press any key to continue....')

def year_wise_alumni():
    conn = mysql.connector.connect(
        host='localhost', database='alumni', user='root', password='root123')
    cursor = conn.cursor()
    year1 = input(' Enter passout year :')
    sql = 'select * from alumni where pass_year like "%'+ year1 +'%";'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Alumni List Passout Year : ',year1)
    print('_'*130)
    print('{:10s} {:30s} {:30s} {:15s} {:20s} {:20s}'.format(
        'ID', 'Name', 'Father Name', 'Email', 'Phone', 'Position'))
    print('_'*130)
    for record in records:
      print('{:010d} {:30s} {:30s} {:15s} {:20s} {:20s}'.format(
          record[0], record[1], record[2], record[3], record[4], record[8]))

    print('_'*130)

    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def alumni_email_list():
    conn = mysql.connector.connect(
        host='localhost', database='alumni', user='root', password='root123')
    cursor = conn.cursor()
    year1 = input(' Enter passout year :')
    sql = 'select * from alumni;'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Alumni Email List')
    print('_'*130)
    print('{:10s} {:30s} {:30s} {:15s} {:20s} {:20s}'.format(
        'ID', 'Name', 'Father Name', 'Email','Position'))
    print('_'*130)
    for record in records:
      print('{:010d} {:30s} {:30s} {:15s} {:20s} {:20s}'.format(
          record[0], record[1], record[2], record[3], record[8]))

    print('_'*130)

    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def alumni_phone_list():
    conn = mysql.connector.connect(
        host='localhost', database='alumni', user='root', password='')
    cursor = conn.cursor()
    sql = 'select * from alumni;'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Alumni Phone Numbers List')
    print('_'*130)
    print('{:10s} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
        'ID', 'Name', 'Father Name', 'Email','Phone','Position'))
    print('_'*130)
    for record in records:
      print('{:010d} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
          record[0], record[1], record[2], record[4],record[3] ,record[8]))

    print('_'*130)

    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def city_wise_alumni_list():
    conn = mysql.connector.connect(
        host='localhost', database='alumni', user='root', password='root123')
    cursor = conn.cursor()
    city = input(' Enter city Name :')
    sql = 'select * from alumni where c_city="'+city+'";'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Alumni City Wise List :',city )
    print('_'*130)
    print('{:10s} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
        'ID', 'Name', 'Father Name', 'Email', 'Position','City'))
    print('_'*130)
    for record in records:
      print('{:010d} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
          record[0], record[1], record[2], record[3], record[8],record[10]))

    print('_'*130)
    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def country_wise_alumni_list():
    conn = mysql.connector.connect(
        host='localhost', database='alumni', user='root', password='root123')
    cursor = conn.cursor()
    cntry = input(' Enter country Name :')
    sql = 'select * from alumni where c_country="'+cntry+'";'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Alumni City Wise List :',cntry )
    print('_'*130)
    print('{:10s} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
        'ID', 'Name', 'Father Name', 'Email', 'Position','Country'))
    print('_'*130)
    for record in records:
      print('{:010d} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
          record[0], record[1], record[2], record[3], record[8],record[11]))

    print('_'*130)

    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def position_wise_alumni_list():
    conn = mysql.connector.connect(
        host='localhost', database='alumni', user='root', password='root123')
    cursor = conn.cursor()
    pos = input(' Enter position Name :')
    sql = 'select * from alumni where position="'+pos+'";'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Alumni position List :',pos )
    print('_'*130)
    print('{:10s} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
        'ID', 'Name', 'Father Name', 'Email', 'Position','Country'))
    print('_'*130)
    for record in records:
      print('{:010d} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
          record[0], record[1], record[2], record[3], record[8],record[11]))

    print('_'*130)

    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def education_wise_alumni_list():
    conn = mysql.connector.connect(
        host='localhost', database='alumni', user='root', password='root123')
    cursor = conn.cursor()
    edu = input(' Enter education Name :')
    sql = 'select * from alumni where heducation="'+edu+'";'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Alumni Education List :',edu )
    print('_'*130)
    print('{:10s} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
        'ID', 'Name', 'Father Name', 'Email', 'Education','Country'))
    print('_'*130)
    for record in records:
      print('{:010d} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
          record[0], record[1], record[2], record[3], record[7],record[11]))

    print('_'*130)

    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def report_menu():
    while True:
      clear()
      print('A L U M N I    R E P O R T    M E N U ')
      print('*'*120)
      print("\n1.   Alumni List")
      print('\n2.   Year wise Alumni')
      print('\n3.   Alumni Email List')
      print('\n4.   Alumni Phone NO')
      print('\n5.   City wise')
      print('\n6.   Country Wise')
      print('\n7.   Position Wise Report')
      print('\n8.   Higher Qualification Wise Report')
      print('\n9.   Back to Main Menu')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      if choice == 1:
        report_alumni_list()
      if choice == 2:
        year_wise_alumni()
      if choice == 3:
        alumni_email_list()
      if choice == 4:
        alumni_phone_list()
      if choice == 5:
        city_wise_alumni_list()
      if choice == 6:
        country_wise_alumni_list()
      if choice == 7:
        position_wise_alumni_list()
      if choice == 8:
        education_wise_alumni_list()
      if choice == 9:
        break

def main_menu():
    clear()
    while True:
      clear()
      print(' A L U M N I   I N F O R M A T I O N   S Y S T E M')
      print('*'*100)
      print("\n1.  Add New alumni Account")
      print('\n2.  Modify Alumni Information')
      print('\n3.  Search Alumni Menu')
      print('\n4.  Report Alumni Menu')
      print("\n5.  Database and Table Creation ")
      print('\n6.  Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      if choice == 1:
        add_alumni()
      if choice == 2:
        modify_alumni()
      if choice ==3 :
        search_menu()
      if choice == 4:
        report_menu()
      if choice == 5:
        db_mgmt()
      if choice ==6:
        break
    made_by()

if __name__ == "__main__":
    main_menu()
