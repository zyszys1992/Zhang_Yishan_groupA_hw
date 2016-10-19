# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 19:12:21 2016

@author: zyszys1992
"""

'''question 1 '''

def Fibonacci_sequence(a):
    x={}#define x as empty set
    x[0]=1#give initial value
    x[1]=1
    for i in range(0,10**100):
    #for loop goes from 0  to 10*100    
        x[i+2]=x[i+1]+x[i]
        #add previous two values to the next one
        if len(str(x[i+2]))>=a :
            #distinguish the length of x 
            break
    print("the nth number's index: ", i+3)
    print("length: ", len(str(x[i+2])))
    print("number: ", x[i+2])
            
Fibonacci_sequence(100)



'''question 2'''

pyramid=[[75],
         [95, 64],
         [17, 47, 82],
         [18, 35, 87, 10],
         [20,  4, 82, 47, 65],
         [19,  1, 23, 75,  3, 34],
         [88,  2, 77, 73,  7, 63, 67],
         [99, 65,  4, 28,  6, 16, 70, 92],
         [41, 41, 26, 56, 83, 40, 80, 70, 33],
         [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
         [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
         [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
         [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
         [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
         [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]]


for i in range(1,len(pyramid))   :
    #for loop goes from the send row to the bottom 
    pyramid[i][i] +=pyramid[i-1][i-1]  
# add the adjacent values from above to the one below themost right line from 
    #top to the bottom
for a in range(1,len(pyramid)):
    #for row loop
    for b in range(0, a): 
        # for column loop
        if b<1:
        #the first entry in each row 
            pyramid [a][b] += pyramid[a-1][b]
                
        elif a>b:
            #the middle entries except the first and last
        #add the adjacent numbers to the one below them
                pyramid[a][b]+=max(pyramid [a-1][b-1], pyramid [a-1][b])
        
   
                
print (max(pyramid[14][0:14]))
#find the biggest value at the last row which have already added up



'''Question 3'''

def Collatzproblem(N,count=1):
    while N!=1:
#while loop         
        count+=1#count how many times it goes
        if N %2==0: #This means that N is an even number since there is no remainder
            N=N//2# do this operation to get next one 
        else:
            N=N*3+1 #This is the formula when N is an odd number
    return count # get how times it calculates



x=[0]*1001
for i in range (1,1000,1):
    x[i]=Collatzproblem(i)
         
print(x.index(max(x[1:1000])),max(x[1:1000]))
#this is for get the max length from 1 to 1000, and get its index by calling the 
#function from above
#do above first and then get the biggest length 179 and its index 871 


#then do the next step below
#Next define a function called Collatz
def Collatz(N,count=1):   
    #the parameter N to the function is what needs to be typed in
    while N!=1:
        print(N)
        count+=1
        if N %2==0: 
            N=N//2
        else:
            N=N*3+1 #This is the formula when N is an odd number
    print(N,'\n')
    
    return count


    
def ChainLength(): 
    # for printing the counts and cycling numbers
    print(Collatz(N))    
    if N==871:
        #distinguish if what has been typed in is the max length or not based
    #the number we entered
        print('This is the longest chain under one thousand!')
    else:
        print('This is not the longest chain under one thousand. Try again.')


N=int(input('Enter a Collatz value N: '))
#input the number that you test 
    
print(ChainLength())






'''Question 4'''

def recurring_cycle(n, d):
    # solve 10^s % d == 10^(s+t) % d
    # where t is length and s is start
    for t in range(1, d):
        if 1 == 10**t % d:
            return t
    return 0

longest = max(recurring_cycle(1, i) for i in range(2,501))
#give the value of cycle from i=2 to i=500 to the longest
print([i for i in range(2,501) if recurring_cycle(1, i) == longest][0])
    





'''QUESTION 5'''
ways = [0]*201  
#give 200 spaces for stroing numbers
ways[0] = 1  
#set the ways[0]=0 which is never changing and is for counting how many ways[0]
#that another ways has which means how many solutions it has for giving 200
for x in [1,2,5,10,20,50,100,200]:  
    for i in range(x, 201):  
        #for loop for recursion that after every time way[i] cut off way[i-x]
    #how many solutions to construct ways[i-x] by using previous x before i=x
    #where x is pence for different values and so on 
    #eg,ways[5] counts 4 when x=5, and when x=1, it counts 1, and when x=2, 
    #it counts 3 which contains the situtaion of  x=1 and x=2 
        ways[i] += ways[i-x]  
print (ways[200])




'''question 6'''


import math

def is_prime(num):
    return is_prime_recur(2, num)
#define a function to check if it is prime
def is_prime_recur(divisor, num):
    if num == 1:
        return False
        #the special case has to be distinguished first
    if num == 2:
        return True
    #the special case has to be distinguished first
    if divisor > int(math.sqrt(num)):
        return True 
 #when divisior bigger square root the number that has been typed in, return 
        #true
    if num % divisor == 0:
        #if the number divided by divisor getting a zero as remainder, return 
    #false
        return False
    else:
        return is_prime_recur(divisor + 1, num)
    #make divisor increase by i every time when it cannot be distinguished 
print(is_prime(1))
print(is_prime(2))  
print(is_prime(9))
print(is_prime(15))
print(is_prime(37))





'''question 7'''
# We define the function that sorts a list of strings. We want to sort with 
# order that number 0-9 first and then letter a-z (regardless of lowercase or
# uppercase). When the first character is the same, we compare the second, 
# the third and so on until it is different. If first few characters are the 
# same for two strings, then the shorter one comes first (e.g. "to" and "today"
# will give "to" first)
def sort_list(strings):

    # Here we want to compare two adjacent strings. If the former one is bigger
    # than the later one, exchange them. We will get the biggest one to the end
    # of the list, while the rest of the list not sorted. We continue the 
    # process until the list is sorted.
    
    # We set i that counts backword.
    for times in range(1,len(strings)):
        for i in range(len(strings)-times):
            
            # Since we can only compare when both string has character in 
            # position i, we get n which is the length or shorter string.
            # We set "flag" for later when the two string has the same first 
            # few characters.
            n = min(len(strings[i]),len(strings[i+1]))
            flag = 0
            
            # Loop.
            for j in range(n):
                
                # If the character is not the same, we put the bigger one in 
                # the later position and break the loop.
                if strings[i][j] != strings[i+1][j]:
                    if strings[i][j]>strings[i+1][j]:
                        temp = strings[i]
                        strings[i] = strings[i+1]
                        strings[i+1] = temp
                    break
                
                # If the characters for position i are the same, add 1 to "flag".
                elif strings[i][j] == strings[i+1][j]:
                    flag +=1
                    
            # If flag is equal to n, then it means the first n characters of the
            # two string are the same. Then we put the shorter one in the 
            #former position.
            if flag == n and len(strings[i])>len(strings[i+1]):
                strings[i] = strings[i+1]
    print(strings)
    
# check
strings = ['banana','watermelon','orange','juice','coconut','pear','peach']            
sort_list(strings)  
       
       
        
        
'''question 8'''




# Define the function that does the calculation, with x being the intial value
# and n being the number of time the function is run.
def calculation(x,n):
    
    # e1, e2, e3 are the results of 3 expressions respectively. i is the 
    # counter of times the function has run.
    e1 = x
    e2 = x
    e3 = x
    i  = 0
    
    # We keep running the function until it has run the required n times.
    while i < n:
        
        # The three expression are given
        e1 = 3.95*e1*(1-e1)
        e2 = 3.95*e2-3.95*e2**2
        e3 = 3.95*(e3-e3**2)
        
        # Output the result of e1, e2, e3 each time the function is run.
        print(e1,e2,e3)
        
        # Add 1 to the counter.
        i += 1
        
# Calculate the required x = 0.9, n = 100.
calculation(.9,100)









