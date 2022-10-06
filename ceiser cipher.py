alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(text,shift,choice):
   string=" "
   if choice==3:
    exit()
    print('existing')
   elif choice==4:
        print('enter valid choice')
   for i in text :
    index=alphabet.index(i)
    if choice==1:
        index=index+shift
        if index>25:
             index=index-26
    if choice==2:
        index=index-shift
        if index<0:
            index=index+26
    string+=alphabet[index]
   print(f'encrypted message is {string}')  
   
while(True):
    choice=int(input("enter choice \n 1.encode \n 2.decode\n 3.exit\n"))
    text1 = input("Type your message:\n").lower()
    shift1 = int(input("Type the shift number:\n"))
    encrypt(text1,shift1,choice)   
    



    



    
