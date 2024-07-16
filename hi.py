# print("Hello World")      #simple python print 

# '''list=[1,2,3,'yes']        #how to pass comment and list
# a=9
# b=10.9
# c='str'
# print(type(list))     # how to get the type of datatype
# print(type(a))
# print(type(b))
# print(type(c))

# x={1,2,9,6,"asmi",8,5,10}   #set
# print(x)

# school = {                     #dict
#     'stud_name':'Asmi',
#     'stud_no': 1143
# }
# print(type(school))


# a = 9              #arithmetic operators
# b = 7
# c=a+b
# d=a-b
# e=a*b
# f=a/b


# print("addition is",c,"subtraction is",d,"multiplication is",e,"division is ",f)     # print using coma

# print(f"add is {c} sub is {d} mul is {e} div is {f}")      #print using fetch {}

# a=9**73      #sqr /to get rasie to  value
# print(a)

# a=73//9                         # div 2 times
# print(a)

# a = 9     #not operator
# b = 3
# print(a!=b)
   
# x = 9              #or operator
# y = 19
# print(x or y)

# a=9                 #identity operator
# if a is 9 :
# print('a is 9')


# list=['asmi',1,2,4,5,'rohini']       #membership operator
# if 'asmi' in list :
# print("abc")'''

# '''a=68
# if 60>a>10:                   #if...else
#      print("a is > 10 and = 5")
# else:
#      print("a is greater than 60")'''

# '''str = int(input("enter val"))        #to pass arg or take arg from user
# print(type(str))'''

# '''a = int(input('enter value of a'))          #if...elif..else  ------calculator
# b = int(input('enter value of b'))
# c = int(input('enter value of c from 1-4'))
# if(c==1):
#     res=a+b 
#     print("addition is",res)
# elif (c==2):
#     res=a-b
#     print("subtraction is",res)
# elif (c==3):
#     res=a*b
#     print("mul is",res)
# elif (c==4):
#     res=a/b
#     print("div is",res)
# else :
#     print("invalid number")'''

# '''list=[1,9,3,2]             #to find median ,lengthof list,med 
# n=len(list)
# med=(n+1)/2
# a=int(med-1)
# median=list[a]
# print(median)'''
# '''sum=0
# for i in len(list):
#     sum= sum + list[i]         #sum=+list[i]
# print(sum)'''

# '''i=0
# passs = 123                  #to check password and unlock phone 
# user_input=int(input("enter password"))
# if ( passs == user_input) :              #condition 1
#     print("unlock")
# else :  
#     while (i<5):                         #condition 2
#         user_input=int(input("enter password"))
#         if ( passs == user_input):        #condition 1 in 2
#             print("unlock")
#             break
#         else :                            # condition else in 2 
#             print("phone lock")
#         i+=1'''


#methods
# '''list=[1,2,3]
# list.append(9)    #add to end
# print(list)
# b=list.copy()     #copy list
# print(b)'''
# '''
# list=[1,9,7]
# list.reverse()    #reverses the order of list 
# print(list)
# list=[1,9,7]
# list.sort()       #sort in asc 
# print(list)'''
# '''list=[1,9,7]
# list.sort(reverse=True)     #reverse the list first then sort it
# print(list)
# list=[1,9,7]
# list.remove(9)           #removes 9 from list
# print(list)
# list=[1,9,7]
# list.insert(4,8)         #insert 8 at 4 index
# print(list)'''
# '''a=4
# del a                 #delete 
# print(a)'''            #o/p will be empty
# '''list=list(set)         #type casting ----converting set into list
# list.copy()
# print(list)
# list.append(9)
# print(list)
# list.clear()              #clear list
# print(list)
# res=list.count('d')          #count how many d are there in list
# print(res)'''
        
# '''list=[1,9,7]
# list.pop(1)                #pop 1 from list
# print(list)'''          #o/p==9,7
# '''
# list=[1,9,7]
# list2=[1,4,7,6]
# list.extend(list2)   #[list1]+[list2]
# print(list2)'''

# '''list=[1,9,7]
# x=list.index(9)     #give index of 9
# print(x)'''


##-------------lecture 3(6/6/24)--------##
# a={1.0,"hello",(1,2,3)}
# print(a)
# print(type(a))
# list=list(a)
# print(list[0])
# print(type(list))

# a={"stu_name":"nimu",      #dic argument
#    "batch_no":"b3"}
# print(a)

# dict={"key":[1,2,3]}       #2d dic argument
# print(dict)

# def c():         #function declaration
#     print("hello")
# c()        #function call

# def c():
#     return("hello")   #return hello
# c()


# s={x:x**3 for x in range(11)}     # comprehension ---writing loop in one line
# print(s)

# x=8
# s={x:x**3 for i in range(1,11)}     # only cube part will be executed as i has been given value as 1 
# print(s)

# s={i:i**3 for i in range(1,11) if(i!=7)}     # comprehension ---writing loop in one line-- two loops(7 will not be executed bcuz of if condition)
# print(s.items())


# list=[x for x in range(2,9) if(x!=7)]    #comprehension with list
# print(list)


# y=5          #x*y using range 
# l=[x*y for x in range (101,121)]
# print(l)


# l=[x for x in range (1,10) if(x%2==0)]       #print even no,=. in given range --- if want sqr of x and also to print even no x*x will be used
# print(l)

# str=list(input("enter a no:"))        #input from user is shown in  list
# print(str)

# list=[]         #print user value by taking len
# n=int(input("enter the length of list:"))
# for i  in range (n):
#     u=int(input(f'{i+1} value'))
#     list.append(u)
# print(list)

# functions


# def green(name):  #print using ,
#     print("hello",name,". Good Morning")
# green("nimu")
    

# def s(x,y):
#     c=x*y
#     return c
#     c=x+y  #null after return
# p=s(2,3)
# print(p)

#add function with user input
# def add():
#     s=0
#     for i in range (0,5):
#         u=int(input(f'{i+1} value:'))
#         s+=u
#     print(s)
#     return s
#     print(s)
# add()

# def s(name,roll_no):           
#     print(f'{name} is roll_no {roll_no}')    #positional arg
# p=s(roll_no=56, name="nimu")                 #keyword arg
# print(p)

# def avg():                 # default argument
#     list=[]
#     n=int(input("enter no of student:"))
#     for i in range(n):
#         a=int(input('age:'))
#         list.append(a)
#         s=sum(list)
#         a=s/n
#         return a
# print(avg())

# def age(*b):      #arbitary argument it is used bcz we dk how many inputs will user give
#     print(b)
#     print(type(b))
# #age([2,3,4])   # answer comes as [2,3,4], as arbitary arg requires more than one value
# #age(2,3,4,5)  # answers comes as tuple (2,3,4,5) as no brackets are given and the bracket are given for the function age
# age([2,3,4],[23,45,6]) 

# def age(**b):      #arbitary keyword argument
#     print(b)
#     print(type(b))  
# age(a=2,b=3,c=4)  # keywords is used to give parameters so answer is in dict {'a': 2, 'b': 3, 'c': 4}

# def add(x,y):    #below code makes the function/operator in one line using lambda
#     c=x+y
#     print(c)
#     return c
# add(2,4)

#lambda                 #writing a function in one line
# add=lambda x,y:x+y   #function=lambda param1,param2: param1+param2     # 
# p=add(4,5)
# print(p)
# sub=lambda x,y:x-y   #function=lambda param1,param2: param1-param2 
# p=sub(4,5)
# print(p)
# mult=lambda x,y:x*y   #function=lambda param1,param2: param1*param2 
# p=mult(4,5)
# print(p)
# divi=lambda x,y:x/y   #function=lambda param1,param2: param1/param2 
# p=divi(4,5)
# print(p)

# def abs_no(num):
#     if num>0:
#         return num
#     else:
#         return -num
# #a=abs_no(4)
# a=abs_no(-2)
# print(a)


##-----------4th lecture(7/6/24)------------##

##list =(1,2,5,6,8)      #slicing method to take a desired part from the list
#list =[1,2,5,6,8]  
#print(list[:4])           #starting_value :(it is used to indicate starting to ending point) ending_value (if ending value is not given it will go till the last of the list same for starting_value)


#continue pass break

# list = [3,2,2,3]
# for i in range(len(list)):
#     print(list[i])
# for i in list:
#     pass     #when uh dont want to do anything just write pass 
#     print(i)

# for i in range(1,11):
#     if i!=7:
#         print(i)
#         break     #terminate the loop doesn't check if there is any instruction further
#     else:
#         continue           #skips the specific iteration


#list=[x for x in range(1,11) if x!=7]   #x(the value which we want to return) for loop second loop  #comprehension
#print(list)

# a="apple"           #example for continue
# for i in a:
#     if a=="p":     
#         continue     #over here p is skipped and further string is printed

#     else:
#         print(i)

# def sam():
#     pass
# sam()

# list=[1,2,3,4,5,6,7,8,9,10,11]
# for i in range(1,11):
#     if i in list:
#         pass
#     else:
#         list.append()

# list.sort()
# print(list)

# name=["asb","ewd","ffr","effe","eeg","err","efr"]
# def search(name):
#     for i in name:
#         if i=="err":
#             print("found")
#         else:
#             print("not found")
# search(name)

#recursive
# list=["asb","ewd","ffr","effe","eeg","err","efr"]
# def find(name,list,i=0):
#     i1=i
#     if list[i]==name:
#         print("found")
#     else:
#         i1=i1+1
#         find(name,list,i1)
        
# find("err",list,0)

###opp

# replace name
# class stu:      #creation of class
#     name="nimu"   #parameters of class
#     r_no=122
#     rank=1
#     def all(self):          #self--default parameter of object---takes the avaliable argument/parameter
#         print(f"{self.name}'s roll no. is {self.r_no} ")    #self access the aavaliable argument from class

# #a=stu()      #object creation
# # #print(a.name,a.r_no)   #object access the class and print it
# # a.name="diksha"        #using object diff value is given to parameters
# # a.r_no=159

# a.all()               #using object function is called
# p=stu()
# p.all()
# p.name="kavya"
# p.all()


##inheritance

# class bird:       #simple inheritance
#     def init_(self):
#         print("bird is ready")
# class penguin(bird):
#     def init_(self):
#         super().init_()
#         print("penguin is ready")
# p=penguin()

# nums=[1,2,3,4,5,6,7,8,9,10]    #to extract list without 6 cpomprehension is used 
# val=6
# list=[nums[i] for i in range (len(nums)) if nums[i] !=val] # checking for ith place of nums by using for loop to take len of nums then if loop is checked where if ith place of nums is not equal to  value to be removed ---loop is executed
# print(list)     # print  nums without 6
# res=[2,4]

#--------------------------------5 lecture-------------------------------------10-6-24----------------

#default constructor---------does not accept any parameter
# class new:
#     def __init__(self):                                    #__init__ ==complies the code directly
#         print("this is default constructor")  

# a=new()           #function called after __init__ function

# #parameter constructor -------------------accept parameter
# class new2:
#     def __init__(self, n, r):
#         print("this is a parameter constructor")
#         self.name=n
#         self.r_no=r
#     def call(self):
#         print(f"{self.name} roll is {self.r_no}")

# b=new2("n",48)               #function called after __init__ function uses objectname=classname() to a class
# b.call()                      #function call() is called using object
# b.name="n"                   #function call normally
# b.r_no=4
# b.call()

#inheritance/encapsulation
# class base:                #base class
#     def __init__(self):           #it will be called when class is called
#         self._a=2       #protected argument is passed using single underscore (_)
# #        self.__a=2      #private argument is passed using double underscore(__)

# class derived(base):          # dervied class inheritance base class
#     def __init__(self):       
#         base.__init__(self)          #__init__ function of base class called in derived class using baseclass_name.function_name()
#         print("protected",self._a)
# #        print("protected",self._base__a)    #to see private argument from base class use this _base__variable_name

#         self._a=3          
#         print("modified protected",self._a)

# o=derived()              #object created for derived class, used for calling derived class
# o2=base()               #object created for base class, used for calling base class

#hierarchy/polymorphism---------------many forms 
# class vehicle:                 #base class
#     def __init__(self,brand,year):
#         self.brand=brand
#         self.year=year

# class car(vehicle):           #child class
#     def move(self):
#         print("move")

# class boat(vehicle):            #child2 classs
#     def move(self):
#         print("sail")

# class plane(vehicle):           #child3 class
#     def move(self):
#         print("fly")

# c=car("porche","2010")             #objects of class with parameter
# b=boat("speed","2020")
# p=plane("fighter","2022")

# for x in (c,b,p):      
#     print(x.brand)
#     print(x.year)
#     x.move()

#overriding------------to change/update already defined argument
#overloading ----------same name, diff arg
#python does follow method overloading
#encapsulation----------private(__a),protected(_a),public(a)--------redundant(copy) data is collected

#super-----------it lies for only inheritance doesn't exist outside of it------calls immediate parent class------function,parameter,constructor

# class stu:
#     def __init__(self,name,id):        #__init__() of base class
#         self.name=name
#         self.id=id

# class branch(stu):
#     def __init__(self, name, id,b):          #__init__() of child class
#         super().__init__(name, id)            #super() is used to call already written function/parameters which lies in parent class
#         self.b=b

# i=branch("nimu",262,"SSC")             #i obj of child class
# print(i.name)
# print(i.id)
# print(i.b)

#multiple inheritance------------many parents, one child

# class mother:
#     def __init__(self,mname)->None:
#         self.name=mname

# class father:
#     def __init__(self,fname)->None:
#         self.name=fname

# class surname:
#     def __init__(self,sname)->None:
#         self.name=sname

# class child(mother,father,surname):
#     def __init__(self,name,fname,mname,sname)->None:
#         self.name=name
#         father.__init__(self,fname)
#         mother.__init__(self,mname)
#         surname.__init__(self,sname)
#         print(name,fname,mname,sname)
# c=child("o","n","e","e")

#decorator---------- a function that takes another function as an argument and returns a modified version of that function-------@
# def dec(func):
#     def process():
#         print("welcome")
#         func()
#         print("goodbye")
#     return process

# @dec
# def yes():
#     print("nimu")
# @dec
# def new():
#     print("continue")

# yes()
# new()

#file handling-=-=========have to revise

# file=open("demo.txt","w")    #normal method of file handling
# file.write("hello this is my file")
# file.close()

# with open("example.txt","w") as file:          # if we add path of a specific file with one / then it will not work but with double // it will work
# # #file write
# with open("C:\\Users\\Mahesh\\Desktop\\Python\\example.txt","w") as file:
#     file.write("hello")

# #file reading
# with open("example.txt","w") as file:      #output didnt came 
#     content=file.read()
#     print(content)


# #line strip
# with open("example.txt","r") as file:
#     print("\n reading line by line")         #\n is used for leaving line
#     for line in file:
#         print(line.strip())      #


# #append
# with open("example.txt","a") as file:
#     file.write("\n append line")

# with open("example.txt","r") as file:
#     file.seek(3)
#     print("\n reading from 3rd character onwards")
#     remaining_content=file.read()
#     print(remaining_content)
# with open("example.txt","r+") as file:
#     file.write("new content written in r+ mode")
#     file.seek(0)
#     con=file.read()
#     print(con)

# with open("demo.txt","a+") as file:
#     file.write("\n append")
#     file.seek(0)
#     con=file.read()
#     print(con)   




#-----------------------------6 lecture-----------------------------------------11-06-2024

#exception handling-------we use it when we know that error will come and we want to hide it from user 
#eh------------------------ the process of identifying and responding to errors in a program. 
#try,except are used for exception handling

#try,except,finally
# try:
#     a=input("enter:")
#     c=a+9
# #    print(y)
# #    c=9/0
# #    pass
# except Exception as e:  #------------as is used to avoid complex name of exception which can be written in short  
#     print(e)             #-------o/p--name 'y' is not defined/------division by zero

# try:
#     a=int(input("enter:"))
#     c=a+9
#     print(c)
# #    print(y)
# #    c=9/0
# #    pass
# except Exception as e:
#     print(e)
# ##  finally-------it is executed even if excepton is handled or not-----after try and exceptt
# finally:
#     print('y')

#types of exception(error)
#IOError--------if prblm occurs while openning,writing or manipulating file
#ValueError---------if input is diff from the datatype which is required
#ArithmeticError------error comes when the required Arithmetic opeartor is not used
#TypeError------------if datatype is not same as mentioned
#IndentationErrorr---------space not given or more spac is given
#ZeroDivisionError-----------cannot divide by zero
#FloatingPointError------------if the output exceed the float datatypes bits


# try:            #------------------content statement which has error
#     # with open("non.txt","r")as file:
#     #     con=file.read()
#     i=int("string")
# except IOError as e:    #except------content statement for error with exception type /exception handling code
#     print(f"Caught an i/o error:{e}")
# except ValueError as v:
#     print("valueerror ")
# finally:
#     print("sucessful")

# try:
#     result=10/0
# # except Exception as e:
# except ZeroDivisionError as e:
#     print("Caught error",e)

# try:
#     result="2"+2
# except TypeError as t:
#     print("Caught error",t)  #Caught error can only concatenate str (not "int") to str


#in-built packages/lib
# import math------log exponential value
# import random---------kuch bhi uthana
# import hashlib--------cyber security(blockchain)
# import pathlib-------write,read, enhance
# import os----------to check os files to write or read 
# import sys----------

# # packages/lib---- the one which we installed on pc
# import pandas
# import numpy
# import matplotlib.pyplot

 

# import math
# def test_floating_point():
#     try:
#         math.log(round(26.344 / 3.5, 4))
#     except FloatingPointError as e:
#         math.log_f(e)


## module------to access already defined features from one class\file to another------means the file which we want to import
# package----when many modules are collected in a format

# from mod import xy
# import mod
# print(xy(9,6))

# import math
# print(math.sqrt(64))

# from package import mod1
## from package import mod1.mul # we cannot call the file directly 
# print(mod1.mul(4,6))    # to call function from a package---- packagename.functionname(para1,...)

## from package import mod1 as m
# from package.pack1 import *     #to access all file from packages
# print(m.mul(4,2))

# from package.pack1 import mod2   # to call package from another package which has another package
# print(mod2.div(4,2))

#simple calculator using try and except
# n=0
# try:
#     while(n!=5):
#         n = int(input("Enter your choice from 1-5: "))
#         a = int(input("Enter the First Number: "))
#         b = int(input("Enter the Second Number: "))
#         def add(a,b):
#             return a+b
#         def sub(a,b):
#             return a-b
#         def mul(a,b):
#             return a*b
#         def div(a,b):
#             return a/b
        
#         if n==1:
#             print(add(a,b))
#         elif n==2:
#             print(sub(a,b))
#         elif n==3:
#             print(mul(a,b))
#         elif n==4:
#             print(div(a,b))
#         elif n==5:
#             exit(0)
        
# except Exception as e:
#     print(e)






# ----------------------------12-06-2024------------------------ 


# # streamlit-----user defined interface ready ho jata hai
# NaN----- null

# # lifecycle 
# import----------pandas,numpy
# dataset-----------files in excel,csv,etc
# eda(Exploratory Data Analysis)------visualaize pattern
# Split(train, test, validation)
# 80:10:10
# training
# model test
# operationalize------deployment

# numpy------- Numeric python----to perform a wide variety of mathematical operations on arrays----to convert an image to array---can perform basic arithmetic operation of math

# np.zero((2,4))     #o/p----array([[0., 0., 0., 0.],
#                          #        [0., 0., 0., 0.]])

# np.ones((2,4))     #o/p----array([[1., 1., 1., 1.],
#                              #    [1., 1., 1., 1.]])

# np.eye (5)       #array([[1., 0., 0., 0., 0.],
#                             [0., 1., 0., 0., 0.],
#                             [0., 0., 1., 0., 0.],
#                             [0., 0., 0., 1., 0.],
#                             [0., 0., 0., 0., 1.]])

# np.reshape(new,(2,3))       #to have different dimenision

# pandas--------used for data sets---data visualtation, manipulation, anaylsis data------
# df-----dataframe
# df.shape-------shows dimenision
# df.head()--------default 5 parameter or we can give parammeter from above to get value
# read_file_extension-------to read that file using that extension
# df.tail()-----------default 5 parameter or we can give parammeter from below to get value
# df.isnull()/pd.isnull(df)----- shows null values ---0 is not null
# df.info()-------provides some info
# pca--principle component analysis------value which is not required can be removed
#df.dropna(inplace = True)------as inplace is true all false value will be deleted
#pd.isnull(df).sum()/df.isnull().sum()----------total value of false value is given
#df.columns----shows all the columns name
#type casting-----df['avg_rating'] = df['avg_rating'].astype('int')
#                 df['avg_rating'].dtypes         ---o/p---dtype('int64')
#df.describe()---count,mean,std,min,max,% of columns
#df.drop([colname,..],axis=1,inplace = true)----to drop specific columns
#axis=1--column-----default rows for drop
#axis=0----row


#to change datatype from float to int
#for col in df.columns:
#   if df[col].dtype == 'float':
#     df[col]=df[col].astype('int')





































