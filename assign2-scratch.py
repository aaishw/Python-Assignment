try:
    print("----------------------------------------------")
    print("#Question 1")

    double = lambda x: x * x * x
    a=0
    b=1
    c=0
    lam=[]
    lam.append(double(a))
    lam.append(double(b))
    for i in range(0,6):
        c = a + b
        lam.append(double(c))
        a = b
        b = c
    print("First 6 numbers' cube of fibonacci:", lam)

    print("----------------------------------------------")
    print("#Question 2")
    a =int(input("Enter an integer"))
    print("Entered interger is: ", a, " ", type(a))
    c =float(input("Enter a float"))
    print("Entered float is: ",c," ",type(c))
    d =input("Enter a string")
    print("Entered string is: ",d," ",type(d))
    e =complex(input("Enter COmplex number in format a+bj"))
    print("Entered complex is: ",e," ",type(e))

    print("----------------------------------------------")
    print("#Question 3")


    user = int(input("Enter negative number to exit"))
    while user >=0:
        user = int(input( "Enter negative number to exit"))

    print("----------------------------------------------")
    print("#Question 4")
    num=1
    count =1
    result = 1
    while count <= 10:
        if(num %2 == 0):
            result = result * num
            count = count +1
        num = num+1
    print("multiplication of first 10 even numbers are: ", result)

    print("----------------------------------------------")
    print("#Question 5")
    concatenate = ""
    i=0
    string = "innovationwithpython"
    while i != len(string):
        if(i %2 ==0):

            concatenate = concatenate + string[i]
        i = i+1
    print("Given string with innovationwithpython ")
    print(concatenate)

    print("----------------------------------------------")
    print("#Question 6")
    def multiple():
        mylist =[]
        for i in range(1,50):
            if(i%2 == 0 and i%6 == 0):
                mylist.append(i)
        return mylist

    print("------------Question: 6-------------------")
    mylist = multiple()
    print("Number which are multiple of both 2 and 6: ",mylist)
    print("Sum of last 3 values in list is: ",mylist[-3]+mylist[-2]+mylist[-1])

    print("----------------------------------------------")
    print("#Question 7")

    print("----------------------------------------------")
    print("#Question 8")

    #What will be the output of the following:

    new_list=[ 1 , 2 , 3 , 4 , 5 , 6 , [ "Riyaz" , "Ul" , "Haque" , 7 ] , 8 , 9 , 10 ]
    print(new_list [ -4 ],"new_list [ -4 ] ----->  [ 'Riyaz' , 'Ul' , 'Haque' , 7 ]")
    print(new_list [ 4 ],"new_list [ 4 ]  ----->  5")
    print(new_list [ 6 ] [ 1 ],"new_list [ 6 ] [ 1 ]  ----->     Ul")
    print(new_list.append(["new"]), "new_list.append(['new'])  -----> ['new'] list as an element will be added in the end of list after 10")
    print("--- new_list . sort( )  ----->  will have error as integer and string cannot be sorted in a single list")
    print(new_list)

    print("----------------------------------------------")
    print("#Question 9")

    def concat( a,b,c):
        print("Individual strings are: ",a,b,c)
        print("Concatenated string is: ", a+b+c)

    d = "Innovation"
    e = "With"
    f = "Python"
    concat(d,e,f)

    print("----------------------------------------------")
    print("#Question 10")
    print("what is negative indexing in python: ---------")
    print("Negative indexing is a way to access from the last element of a data structure like list or tuple.")
    print("So negative indexing moves from right to left instead of regular indexing( left to right) starting from 0")
    print("What is packing and unpacking---------")
    print("When we dont have the information regarding the number of arguments or variable to be passed")
    print("In packing we are passing individual values as a group or collection")
    print("In unpacking we are extracting those individual values  from that collection")
    print("What is mutable and immutable-----------")
    print(" A mutable object can be changed and altered after its creation. Immutable objects cannot be changed or altered after its creation")
    print("Append and extend----------------------")
    print("Extend accepts iterable object list another list. Append adds one element within z list. Extend concatenates list")
    z = [1, 2, 3]
    z.append(4)
    z.append([4, 5])
    z.extend([5, 6])
    print(z)
    print("Piclkling and unpickling")
    print("Pickling is a process of converting python object into byte stream to send over network.")
    print("Unpickling is a process of converting byte stream data into python object")

    print("----------------------------------------------")
    print("#Question 11")
    import module
    print("Calling multiply function in module.py")
    module.multiply(11,12,13)

    print("----------------------------------------------")
    print("#Question 12")

    my_dict={}
    n = int(input("Enter the value of n: "))
    for i in range(1,n+1):
        my_dict[i] = i*i
    print(my_dict)

    print("----------------------------------------------")
    print("#Question 13")

    print("What is split function in python")
    print("It parses the string and seperates it into different elements depending on the seperator symbol passed and stores in variable or list provided")

    print("----------------------------------------------")
    print("#Question 14")

    ip_string = input("Enter comma seperated numbers: ")
    ip_list=[]
    ip_list = ip_string.split(',')
    ip_tuple = tuple(ip_string.split(','))
    print("Generated list: ", ip_list)
    print("Generated Tuple:", ip_tuple)

    print("----------------------------------------------")
    print("#Question 15")

    reverse = input("Enter a string to be reversed: ")
    print("Reverse string using indexing is: ",reverse[::-1])
    print("Reverse string using for loop is: ", end="")
    j=-1
    for i in reverse:
        print(reverse[j],end="")
        j = j-1

    print("----------------------------------------------")
    print("#Question 16")

    string_one = "hello"
    string_two = "world"
    a = set()
    a = set(string_two)
    b = set(string_one)
    print("common character/s of two strings  'hello' and 'world' using set: ", a.intersection(b))

    print("----------------------------------------------")
    print("#Question 17")

    wordcount =[]
    sent_ip =input("Enter a sentence")
    splitlist = sent_ip.split(" ")
    for ele in splitlist:
        wordcount.append(len(ele))
    print(wordcount)

    print("----------------------------------------------")
    print("#Question 18")

    dic1= {1:'a', 2:'b'}
    dic2= {3:'c', 4:'d'}
    dic3= {5:'e', 6:'f'}
    dic4 = dic1.update(dic2)
    dic4 = dic1.update(dic3)
    print(dic1)

    print("----------------------------------------------")
    print("#Question 20")

    print("Difference between range and xrange----------------------")
    print("range returns a list object and xrange returns xrange object")
    print("there is no xrange syntax in python3 but range in python3 works same as  xrange in python2")
    #-------------------------------------------

except:
    print("Invalid input format")