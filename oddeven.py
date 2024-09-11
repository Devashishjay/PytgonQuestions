#Question- Write a python program add even numbers into even_list and odd numbers in to odd_list.
# list=[11,21,13,7,14,6,19,17,8,2,4]
#odd_numbers=[]
#even_numbers[]


#Solution

# list=[11,21,13,7,14,6,19,17,8,2,4]

# odd_numbers=[]
# even_numbers=[]

# for items in list:
#     if items%2==0:
#         even_numbers.append(items)
#     else:
#         odd_numbers.append(items)
        
# print("odd_numbers: ",odd_numbers)
# print("even_numbers: ",even_numbers)


# output=odd_numbers:  [11, 21, 13, 7, 19, 17]
# even_numbers:  [14, 6, 8, 2, 4]

# def calc_list(numbers):
# odd_numbers=[] 
# even_numbers=[]

# for items in list:
#     if items%2==0:
#         even_numbers.append(items)
#     else:
#         odd_numbers.append(items)
        
# print("odd_numbers: ",odd_numbers)
# print("even_numbers: ",even_numbers)


#__________________________________________________________________________________

# Question) WAP to print all the even number between 1 to 100.Using for loop

# for i in range(1,100):
#     if i%2==0:
#         print(i)
    
    
# output= it is printed 

#Question) WAP to print all the even number between 1 to 100.Using while loop.

# i=1
# while ( i>=1 and i<=100):
#     if i%2==0:
#      print(i)
#     i+=1
    
    
# output= it is printed 
    
    
#Question) WAP to print all the even number between 1 to 100.Using function.

def calc_evenNum():  
 for i in range(1,100):
    if i%2==0:
     print(i)
     
     
calc_evenNum()
    

