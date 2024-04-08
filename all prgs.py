'''#Random numbers
import random
def dice():
    cont='y'
    while cont in ('y','Y'):
        a=random.randint(1,6)
        print("You have got:",":",a)
        cont=input("do you want to continue? (y/n)")
dice()'''

'''#Textfile
Myfile=open("Newfile.txt","r")
line=" "
while line:
    line=Myfile.readline()
    for word in line.split():
        print(word,end="#")
        print()
Myfile.close()'''

'''#Character count in a text file
F=open("Newfile.txt","r")
vcount=ccount=uppercount=lowercount=0
x=F.read()
for i in x:
    if i.isalpha():
        if i in "AEIOUaeiou":
            vcount+=1
        else:
            ccount+=1
    if i.isupper():
        uppercount+=1
    if i.islower():
        lowercount+=1
print("Vowels:",vcount)
print("Consanants:",ccount)
print("uppercase:",uppercount)
print("lowercase:",lowercount)
F.close()'''

'''#stack operation
stack=[]
def push():
    while True:
        x=int(input("Enter the element you want to push:"))
        stack.append(x)
        ch=input("Do you want to push more elements? (y/n)")
        if ch in 'nN':
            break
        return
def pop():
    while True:
        if stack==[]:
            print("Empty stack UNDERFLOW!")
            break
        else:
            print("The popped element is:",stack[-1])
            stack.pop()
            ch=input("do you want to continue? (y/n)")
            if ch in 'nN':
                break
            return
def display():
    l=len(stack)
    print("The stack is:")
    for i in range(1-1,-1,-1):
        print(stack[i])
    return
def peek():
    print("The topmost element of the stack is:",stack[len(stack)-1])

#main program
while True:
    print("STACK OPERATION")
    print("1.PUSH")
    print("2.POP")
    print("3.DISPLAY")
    print("4.PEEK")
    print("5.EXIT")
    p=int(input("Enter your choice:"))
    if p==1:
        push()
    elif p==2:
        pop()
    elif p==3:
        display()
    elif p==4:
        peek()
    elif p==5:
        break'''

'''#search operation using binary file
import pickle
def write():
    F=open("student.dat","wb")
    Rec=[]
    while True:
        Rollnumber=int(input("Enter the rollnumber:"))
        name=input("Enter the name:")
        Data=[Rollnumber,name]
        Rec.append(Data)
        ch=input("do you want to continue? (y/n)")
        if ch in 'nN':
            break
        print("Record uploaded successfully")
    pickle.dump(Rec,F)
    F.close()
def search():
    Y=open("student.dat","rb")
    Found=0
    Data=pickle.load(Y)
    Rollnumber =int(input("Enter the rollnumber to be searched:"))
    for i in Data:
        if i[0]==Rollnumber:
            print("student name",i[1])
            break
        else:
            print("record not found")
            Y.close()
write()
search()'''

#csv file
import csv
with open("user_info.csv","w")as obj:
    fileobj=csv.writer(obj)
    fileobj.writerow(["user_id","password"])
    while(True):
        user_id=input("Enter the user_id:")
        password=input("Enter the password:")
        Data=[user_id,password]
        fileobj.writerow(Data)
        x=input("do you want to continue? (y/n)")
        if x in 'nN':
            break
with open("user_info.csv","r")as obj2:
    fileobj2=csv.reader(obj2)
    given=input("Enter the user_id to be searched: \n")
    for i in fileobj2:
        next(obj2)
        if i[0]==given:
            print(i[1])
            break
        
        
