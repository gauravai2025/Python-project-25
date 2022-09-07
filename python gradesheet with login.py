from statistics import mean as m             #    login id: gaurav  password: 2020
                                             # login id : adarsh  passwod : 2021
admins={'gaurav':2020 , 'adarsh':2021}
students_list={'gauarav':98,'adarsh':96,'dhanraj':95}
def entergrades():
     enter_students=input('students name:')
     enter_grade=int(input('grade:'))
     if enter_students in students_list:
         print('adding grade...')
         students_list[enter_students].append(float(enter_grade))
     else:
         print('student does not exist')
     print(students_list)   
     
def removestudents():
     want_to_remove=input('enter students:')
     if want_to_remove in students_list:
          print('removing students')
          del  students_list[want_to_remove]
          print(students_list)
     else:
          print('no name matched')
def average():
     for eachstudent in students_list:
          gradelist=students_list(eachstudent)
          avg=m(gradelist)
          print(eachstudent,'average marks:',avg)
    
       
    
   
          
     
     

     
         
     
     
def main():

    print("""welcome to grade list
      
    [1]-enter grades
    [2]-remove students
    [3]-students average grades
    [4]-exit
    """)
    option =input("what would you like to do today?(choose an option) ")
    if option=='1':
        entergrades()
    elif option =='2':
        removestudents()
    elif option=='3':
        average()
    elif option=='4':
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
    
