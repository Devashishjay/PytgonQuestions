# Python program to calculate the average of numbers in a given list

# Solution-1            # Normal Solution

# list=[85,90,65,75,89,75]
# sum=sum(list)
# average=sum/len(list)
# print(average)

# output= 79

#Solution-2                      # solution using if else

# list=[85,90,65,75,89,75]

# if len(list)>0:
#     averge=sum(list)/len(list)
# else:
#     averge=0
# print(averge)


#Solution-3                       # Solution using while loop

# list=[85,90,65,75,89,75]

# i=0
# sum=0
# while i<len(list):
#     
#     sum+=list[i]
#     i+=1
    
#     average=sum/i
# print(average)

# output=79


#Solution-4                     # Solution using for loop

# list=[85,90,65,75,89,75]

# sum=0
# for items in list:
#     sum+=items
    
# average=sum/len(list)
# print(average)

# output=79


# solution-5                   # Solution using function



# def calc_average(number):                   #Function defination
#     sum=0
#     i=0
#     while i<len(number):
#         sum+=number[i]
#         i+=1
#     return sum/i if i>0 else 0
    
    
    
# list=[85,90,65,75,89,75]                     #Function call
# average=calc_average(list)
# print(average)

# output=79
    




    
    
    












