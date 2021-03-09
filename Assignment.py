
#Calculator Program

print("This is a calculator!!!!")

n1 = int( input("Enter the first number: "))
n2 = int( input("Enter the second number: "))
choice=1;		

def add(n1,n2):
	return n1+n2

def mul(n1,n2):
	return n1*n2

def div(n1,n2):
	return n1/n2

def diff(n1,n2):
	if(n1>n2):
		return n1-n2
	else:
		return n2-n1 

def rem(n1,n2):
	return n1/n2

def power(n1,n2):
	return n1**n2
	
while choice!=0:
	print("1. For addition")
	print("2. For Multiplication")
	print("3. For Division")
	print("4. For Difference")	
	print("5. For Power first number^second number")
	print("6. For Remainder of the Two numbers")
	print("7. Exit")
	
	choice = int( input("Enter your choice: "))
	if choice == 1:
		ans= add(n1,n2)
		print("Answer is: ",ans)
	elif choice == 2:
		ans= mul(n1,n2)
		print("Answer is: ",ans)
	elif choice == 3:
		ans= div(n1,n2)
		print("Answer is: ",ans)
	elif choice == 4:
		ans= diff(n1,n2)
		print("Answer is: ",ans)
	elif choice == 5:
		ans= power(n1,n2)
		print("Answer is: ",ans)
	elif choice == 6:
		ans= rem(n1,n2)
		print("Answer is: ",ans)
	elif choice == 7:
		break;


#Programs on Strings

#1.Check String for Palindrome
print("\nCheck String for Palindrome")
string = input("Enter your string : ")
ans = ""

def palindrome(string):
	s = ""
	for ch in string:
		s= ch+s
	if string == s:
		return print("It is a Palindrome")
	else:
		return print("It is not a Palindrome")
	
ans= palindrome(string)

#2.How to split strings on Multiple Delimiters or specified characters?
print("\nHow to split strings on Multiple Delimiters or specified characters?")
string = input("Enter your string : ")
ans = ""

def splitthis(string):
	limiters = [' ','@','!','.']
	
	result = string.split(limiters[0])
	
	for i in range(1, len(limiters)):
		for j in range(len(result)):
			subsplit = result[j].split(limiters[i])
			if len(subsplit) > 1:
				result = result[:j] + subsplit +result[j+1:]
	return result

ans= splitthis(string)
print(ans)

#3.Write a python program to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
print("\nWrite a python program to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.")
string = input("Enter your string : ")
ans = ""

def toupper(str1):
    count = 0
    for letter in str1[:4]: 
        if letter.upper() == letter:
            count += 1
    if count >= 2:
        return str1.upper()
    return str1

ans=toupper(string)
print(ans)

#Programs on lists

#1.Program to get a list sorted in increasing order.
print("\nProgram to get a list sorted in increasing order.")
lst = [] 
n = int(input("Enter number of elements : ")) 
 
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele) 
      
lst.sort()
print(lst)

#2.Program to find the lists of words longer than n from a given list of words
print("\nProgram to find the lists of words longer than n from a given list of words")

def find_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	

string=input("Enter your String : ")
n=int(input("Enter your threshold length : "))

print(find_words(n, string))

#3.Program that takes two lists and returns true if they have at least one common member.
print("\nProgram that takes two lists and returns true if they have at least one common member.")
def common_element(list1, list2): 
    result = False
    for x in list1: 
        for y in list2: 
            if x == y: 
                result = True
                return result  
                  
    return result 
      
			 
lst1 = [] 
n = int(input("Enter number of elements : ")) 
print("Enter the elements") 
for i in range(0, n): 
    ele = int(input()) 
  
    lst1.append(ele)

lst2 = [] 
n = int(input("Enter number of elements : ")) 
print("Enter the elements") 
for i in range(0, n): 
    ele = int(input()) 
  
    lst2.append(ele)
	
print(common_element(lst1, lst2)) 

#4.Write a program to print the numbers of a specified list after removing even numbers from it.eg-(1,2,3,4,5,6,7,8)
print("\nWrite a program to print the numbers of a specified list after removing even numbers from it.eg-(1,2,3,4,5,6,7,8)")

def deleteeven(lst):
	for x in lst:
		if x%2==0:
			lst.remove(x)
	return lst
	
lst1 = [] 
n = int(input("Enter number of elements : ")) 
print("Enter the elements") 
for i in range(0, n): 
    ele = int(input()) 
  
    lst1.append(ele)
	
print(deleteeven(lst1))

#5.Write a python program to generate all the permutations of a list.
from itertools import permutations 

print("\n5.Write a python program to generate all the permutations of a list.")

def allPermutations(str): 
       
	   
     permList = permutations(str) 
  
     
     for perm in list(permList): 
         print (''.join(perm)) 
        

if __name__ == "__main__": 
    str = 'Jyot'
    allPermutations(str) 

#Programs on Dictionary

#1.create two dictionaries and merge them.
print("\nCreate two dictionaries and merge them.")

dict1 = {'Tesla': 'Model 3',
      'Ford': 'Mustang',
      'Lamborghini': 'Aventador'}
dict2 = {'Jaguar': 'XJ',
      'BMW': '7 series'}

dict3 = dict1.copy()
dict3.update(dict2)
print(dict1)
print(dict2)
print("On merging: ")
print(dict3)

#2.Create a new dictionary by extracting the keys from a below dictionary
#Sampledic={‘’name”:”kelly”,”age”:25,”salary”:8000,”city”:”new york”}
#Keys=[“name”,”salary”]
print("\nCreate a new dictionary by extracting the keys")
Sampledic = {'name':'kelly','age':25, 'salary':8000,'city':'new york'} 
  
print("\nOriginal dictionary : ", Sampledic )

resultant = {key: Sampledic[key] for key in Sampledic.keys() 
                               & {'name', 'salary'}} 

print("Filtered dictionary is : " ,resultant) 

#Programs on Tuples

#1.Swap the following two tuples
#Tuple1=(11,22,33)
#Tuple2=(99,88,77)
print("\nSwap two Tuples")
tuple1=(11,22,33)
tuple2=(99,88,77)
print("Tuple 1 is: ",tuple1)
print("Tuple 2 is: ",tuple2)
tupletemp=tuple1
tuple1=tuple2
tuple2=tupletemp			
print("Tuple 1 is: ",tuple1)
print("Tuple 2 is: ",tuple2)

#2.Modify the first item (22) of a list inside a following tuple to 222
#      Tuple1=(11,[22,33],44,55)
#      Expected output= Tuple1=(11,[222,33],44,55)

Tuple1=(11,[22,33],44,55)
print("\nModify Tuples")
print("Original Tuple is :", Tuple1)
lst = list(Tuple1)
lst[1]= [222,33]
TupleUpdated = tuple(lst)

print("Updated  Tuple is :",TupleUpdated)

