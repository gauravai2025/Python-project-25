from statistics import mean as m
admn1=input('enter 1st username\n')
pasw1=int(input('enter 1st integer password\n'))
admn2=input('enter 2nd username\n')
pasw2=int(input('enter 2nd  integer password\n'))
admins={admn1:pasw1 , admn2:pasw2}

students_list={'gaurav':[92],'adarsh':[96],'dhanraj':[95]}
def entergrades():
     enter_students=input('students name:')
     enter_grade=int(input('grade:'))
     if enter_students in students_list:
         print('adding grade...')
         students_list[enter_students].append(enter_grade)
     else:
         print('student does not exist')
     print(students_list)   
     
def removestudents():
     want_to_remove=input('enter students:')
     if want_to_remove in students_list:
          print('removing students...')
          del  students_list[want_to_remove]
          print(students_list)
     else:
          print('no name matched')

def average():
     for eachstudent in students_list:
          gradelist=students_list(eachstudent)
          avg=m(gradelist)
          print(eachstudent,'average marks:',avg)

def addstudents():
    newstd=input("enter name of student to add in list:")
    newgrd=input('enter grade of new students:')
    print("adding .....")
    students_list[newstd]=list(map(int,(newgrd+' ').split()))
    print(students_list)
          
def main():

    print("""welcome to grade list
      
    [1]-enter grades
    [2]-remove students
    [3]-students average grades
    [4]- add students
    [5]-exit
    """)
    option =input("what would you like to do today?(choose an option)\n ")
    if option=='1':
        entergrades()
    elif option =='2':
        removestudents()
    elif option=='3':
        average()
    elif option=='4':
         addstudents()
    elif option=='5':
        exit()
    else:
          print('please enter a valid number , try again')
          
          
login=input('username: ')
passw=int(input('password: '))
if login in admins:
    if admins[login]==passw:
        
          print("welcome, ",login)
          while True:
             main()      
      
    else:
        print('wrong password !, will detonate in 5 seconds')
         
else:
    print('inavalid username !')
    
