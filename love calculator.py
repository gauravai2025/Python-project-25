# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
namef=name1+name2
length1=len(namef)


count1=0
count2=0

while length1>0:
  i=0
  if namef[i]=='T' or 'R' or 'U' or 'E' or 't' or 'r' or 'u' or 'e':
    count1+=1
  length1-=1
  i+=1
while length1>0:
  i=0
  if namef[i]=='L' or 'O' or 'V' or 'E' or 'l' or 'o' or 'v' or 'e':
    count2+=1
  length1-=1
  i+=1
counts1=str(count1)
counts2=str(count2)


score=counts1 + counts2
scoref=int(score)
if scoref >90 or scoref<10:
  print(f"Your score is {scoref}, you go  together like coke and mentos.\n")
 
elif scoref>40 and scoref<50:
  print(f"Your score is {scoref}, you are alright together.\n")
else:
  print(f"Your score is {scoref} \n")
  
  
  


